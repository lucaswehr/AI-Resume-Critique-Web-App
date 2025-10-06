import re
from flask import Flask, render_template, request # request allows flask to acess data that the user sends over
import pdfplumber, csv, os
from critic import readability, passiveVoiceRatio, grammarChecker, analyzeWithAI, extractPDF
import markdown # allows the ai text to appear more structured in HTML

app = Flask(__name__)

uploadFolder = "uploads"

os.makedirs(uploadFolder, exist_ok=True) # creates the uploadfolder, if it already exists then dont touch it

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/upload", methods = ["POST"])
def upload():
    f = request.files['resume'] # 'resume' is the name I will be using in HTML which will the user uploaded file name
    path = os.path.join(uploadFolder, f.filename)
    f.save(path)
    text = extractPDF(path) 
          
    results = {
        "readability": readability(text),
        "passiveVoiceRatio": passiveVoiceRatio(text),
        "Grammar": grammarChecker(text),
        "aiAdvice": markdown.markdown(analyzeWithAI(text)) # markdown is used to structure the AI text in a clean manner
    }

    if results['readability']['flesch'] > 100:
         results['readability']['flesch'] = 100
    elif results['readability']['flesch'] < 0:
         results['readability']['flesch'] = 0

    if results['readability']['grade'] < 0:
      results['readability']['grade'] = 0
   
    # result can be any variable, the name of that variable will be used in HTML
    return render_template("results.html", result=results) 

if __name__ == "__main__":
    app.run(debug=True)


# def extract_emails(text):
#     return re.findall(r"\S+@\S+", text)

# def extract_phoneNumbers(text):
#     pattern = r"\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}"
#     return re.findall(pattern, text)

# def extract_skills(text, skills):
#     found_skills = []
#     textLower = text.lower()
#     for skill in skills:
#         if skill.lower() in textLower:
#             found_skills.append(skill)

#     return found_skills

# def extract_education(text):

#     status = "Unknown"
#     foundWords = []
#     education = [
#         "High school",
#         "Associate",
#         "Bachelor",
#         "Master",
#         "Phd",
#         "B.sc",
#         "M.sc",
#         "Ba",
#         "Bs",
#         "Mba",
#         "Doctorate"
#     ]

#     keywords = ["ongoing","expected","pursuing", "candidate"]

#     for educationKey in education:
#         if educationKey.lower() in text.lower():
#             status = "Completed"  
#             break

#     for key in keywords:
#         if key.lower() in text.lower():
#             status = "In Progress"  
#             break

#     foundWords.append({"Degree": educationKey, "Status" : status})
#     return foundWords
