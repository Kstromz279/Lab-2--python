# Author: Khalil Stroman
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12
def getLetterGrade():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  if grade >= 93:
    print("Your letter grade for CMPSC 131 is A.")
  elif grade >= 90 and grade < 93:
    print("Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87 and grade < 90:
    print("Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83 and grade < 87:
    print("Your letter grade for CMPSC 131 is B.")
  elif grade >= 80 and grade < 83:
    print("Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77 and grade < 80:
    print("Your letter grade for CMPSC 131 is C+.")
  elif grade >= 70 and grade < 77:
    print("Your letter grade for CMPSC 131 is C.")
  elif grade >= 60 and grade < 70:
    print("Your letter grade for CMPSC 131 is D.")
  else:
    print("Your letter grade for CMPSC 131 is F.")

def run():
  getLetterGrade()
if __name__ == "__main__":
  run()