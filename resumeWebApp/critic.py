import textstat # used to measure how easy it is to read text (readability factor)
import spacy # analyzes sentence structure (passive voice, tone)
import language_tool_python # helps me find grammar issues 
import re
import os
import cohere # allows me to use AI to generate advice on the given resume
import pdfplumber
from dotenv import load_dotenv # --> I stored my api key in a seperate file so that its private and no one can see it. This allows me do that

load_dotenv() # --> gets my hidden api key

API_KEY = os.getenv("API_KEY")

co = cohere.ClientV2(API_KEY) # free API token I got off of Cohere

nlp = spacy.load("en_core_web_sm") # contains data like sentence structure and parts of speech for spacy to collect and use for analyzing text

tool = language_tool_python.LanguageTool('en-US') # checks for grammar and style in english

def readability(text):
    return {
        "flesch": textstat.flesch_reading_ease(text), # gives scoree 1-100 based off how readable the text is. Higher the better
        "grade": textstat.flesch_kincaid_grade(text), # gives the US grade level needed to understand the text
        "AvgSenLen": textstat.avg_sentence_length(text) # average number of words per sentence
    }

def passiveVoiceRatio(text):
    
    text = re.sub(r"^[\u2022●*]\s*", "", text, flags=re.MULTILINE) # takes out bullets points 

    doc = nlp(text) # converts the text so that spacy can understand it
    sentences = list(doc.sents) # splits the doc into a list of sentences

    passiveCount = 0
    
    for sent in sentences:

        if any(tok.dep_ == "auxpass" for tok in sent) or re.findall(r"\b(was|were|is|are|been|be)\b\s+\w+ed\b", sent.text, re.IGNORECASE):
            passiveCount += 1
         
    # loops through each sentence and counts how many times passive voice was used 
    # tok.dep == "auxpass" is used to see if theres any passive auxillary verbs like "was,be,were,been" in said sentence
    

    # returns ratio of how many times passive voice was used and the number of sentences in the text
    # max is used in case the number of sentences is 0 which we cant divide
    return passiveCount / max(len(sentences), 1) * 100

def grammarChecker(text):
    matches = tool.check(text) # gives a list of grammatical errors
    return {
        "count": len(matches), # finds how many grammar errors there are
        "examples": [ # list of dictionaries because we have a set number of grammar errors and we need to print them out
        {
            "message": (m.message),
            "error": text[m.offset : m.offset + m.errorLength] 

        } 
           for m in matches[:5]# gets a list of the first 5 errors
        ]
    }
    
    
def extractPDF(path):        
     with pdfplumber.open(path) as pdf:
           text = ""
           for page in pdf.pages:
             if page.extract_text():
                text += page.extract_text() + '\n'
     return text

def analyzeWithAI(text):
    
    response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": f"""You are a professional resume critic. 
                        I need you to critque the following resume. Make it short and concise and rate it out of 10. {text}""",
        }
    ],
    )

    return response.message.content[0].text