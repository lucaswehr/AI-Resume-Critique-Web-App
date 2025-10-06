# from flask import Flask, render_template
# import pdfplumber, csv, os
# from resumeWebApp.app import extract_emails, extract_phoneNumbers, extract_skills, extract_education

# app = Flask(__name__)

# @app.route("/")

# def index():
#    return render_template("index.html")

# if (__name__ == "__main__"):
#    app.run(debug=True)

# #print("Hello World")

# #for i in range(10):
#    # print(i)

# name = "Elephant"

# name2 = name[:5]  #prints out half of the string

# name3 = name[:-2] #prints out the whole string except for the last two letters

# name4 = name[-2:] #prints out only the last two letters

# name5 = name[:4]  #prints out the first four letters

# #print(name5.upper())

# numbers = [1,2,3,4,5]

# numbers.append(6)

# numbers.pop()

# #for n in numbers:
#    # print(n)


# searchExample = "guardPost"
# splitExample = "The man walked down the road"

# #if "post" in searchExample.lower(): # detects if the substring "post" is in the text and checks if the word found is uppercase or lowercase
#     #print("found!")

# answer = searchExample.replace("guard", "banana")

# answer2 = splitExample.split() #splits the string into substrings based off spaces i.e "im in a river" will be split by ['im','in','a','river']

# #print(answer2)

# splitLinesExample = """Name: Lucas
# Skills: Python, C++
# Experience: 2 years"""

# lines = splitLinesExample.splitlines() # = ['Name: Lucas', 'Skills: Python, C++', 'Experience: 2 years']

# #for line in lines:
#     #if "name" in line.lower():
#      #   print("found line at: ", line)



# #FILE WORK //////////////////////////////
# #with open("example.txt", "r") as f: #reading a file
#     #text = f.read()

# #with open("example.txt", "a") as g: #write in
#    # g.write("Texting in example file")


# resume_data = {
#     "Name": "Lucas",
#     "Email": "lucas@example.com",
#     "Skills": ["Python", "C++", "SQL"]
# }

# #print(resume_data["Skills"]) #prints out ["Python", "C++", "SQL"]

# resume_data["Name"] = "Bob"

# #for key, value in resume_data.items():
#  #   print(key, ":", value)

# all_resumes = {
#     "resume1": {"Name": "Lucas", "Skills": ["Python", "C++"]},
#     "resume2": {"Name": "Alice", "Skills": ["Java", "SQL"]}
# }

# #for key, data in all_resumes.items():
#  #   print(data["Name"], "has skills:", data["Skills"])

# import re

# #finding emails in a string /////////////////
# text = "Email me at lucas.wehr@wsu.edu or lucaswehr26@gmail.com or at my work: lucas.wehr@gprep.com"

# email = re.findall(r"\S+@\S+", text) #finds emails based off of the @ symbol

# #print(email) # = ['lucas.wehr@wsu.edu', 'lucaswehr26@gmail.com', 'lucas.wehr@gprep.com']

# #finding phone numbers in a string /////////////////////

# string = "Contact me at 509-601-0556 or 509-385-7516"

# pattern = r"\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}"

# #phoneNumber = re.findall(pattern,string)

# #print(phoneNumber) # = ['509-601-0556', '509-385-7516']

# # example with finding data in a file

# skillsToCheck = ["C++","C","Python", "Java", "SQL", "HTML", "Linux"]
# resumeFolder = "resumeWebApp/resumes"
# allResumes = []

# #@app.route("/analyze", methods=["POST"])



# for filename in os.listdir(resumeFolder):

#         if (filename.endswith("Zone.Identifier")):
#           continue

#         if filename.endswith(".txt"):
#           with open(os.path.join(resumeFolder, filename), "r") as f:
#               text2 = f.read()
#         elif filename.endswith(".pdf"):
#           try:         
#              with pdfplumber.open(os.path.join(resumeFolder, filename)) as pdf:
#                  text2 = ""
#                  for page in pdf.pages:
#                      text2 += page.extract_text() + '\n'
#           except Exception as e:
#             print(f"Could no load file {filename} : {e}")
#             continue
                 
        
#         newEmail = extract_emails(text2)
#         newPhone = extract_phoneNumbers(text2)
#         newSkills = extract_skills(text2, skillsToCheck)
#         education = extract_education(text2)

#         matchedSkills = [skill for skill in newSkills if skill in skillsToCheck]
#         score = len(matchedSkills)
#         percentage = (score / len(skillsToCheck)) * 100

#         allResumes.append({
#         "File": filename,
#         "Emails": ", ".join(newEmail),
#         "Phonenumber(s)": ", ".join(newPhone),
#         "Degree": ", ".join([f"{edu['Degree']} ({edu['Status']})" for edu in education]),
#         "Skills Found": ", ".join(matchedSkills),
#         "Score": f"{score}/{len(skillsToCheck)}",
#         "Percentage": f"{percentage:.1f}%"
#     })
#     #return render_template("index.html", results=allResumes)
    


# all_resumes_sorted = sorted(allResumes, key=lambda x: float(x['Percentage'].replace('%','')), reverse=True)

# for key in allResumes:
#     print(key['File'])

# with open("resumeResults.csv", "w", newline="") as csvfile:
#     fieldnames = ["File", "Emails", "Phonenumber(s)", "Skills Found", "Degree", "Score", "Percentage"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(all_resumes_sorted)



