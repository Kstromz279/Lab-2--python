# Author: Khalil Stroman kzs5955@psu.edu
# Collaborator: Daniel Stebbins drs5972@psu.edu
# Collaborator: David Kim dkk5396@psu.edu
# Collaborator: Emanuel Bassill Chuckran eab6017@psu.edu
# Section: 12
# Breakout: 2
def getLetterGrade(grade):
  if grade >= 93:
    return "A"
  elif grade >= 90:
    return "A-"
  elif grade >= 87:
    return "B+"
  elif grade >= 83:
    return "B"
  elif grade >= 80:
    return "B-"
  elif grade >= 77:
    return "C+"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"


def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__ == "__main__":
  run()