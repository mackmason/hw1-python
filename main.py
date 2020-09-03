# Author: Mack Mason mjm8542@psu.print

courseOneGrade = input("Enter your course 1 letter grade: ")
courseOneCredit = input("Enter your course 1 credit: ")
courseOneCredit = float(courseOneCredit)
if (courseOneGrade == "A"):
  print(f"Grade point for course 1 is: 4.0")
  courseOneGradeFloat = 4.0
elif (courseOneGrade == "A-"):
  print(f"Grade point for course 1 is: 3.67")
  courseOneGradeFloat = 3.67
elif (courseOneGrade == "B+"):
  print(f"Grade point for course 1 is: 3.33")
  courseOneGradeFloat = 3.33
elif (courseOneGrade == "B"):
  print(f"Grade point for course 1 is: 3.0")
  courseOneGradeFloat = 3.0
elif (courseOneGrade == "B-"):
  print(f"Grade point for course 1 is: 2.67")
  courseOneGradeFloat = 2.67
elif (courseOneGrade == "C+"):
  print(f"Grade point for course 1 is: 2.33")
  courseOneGradeFloat = 2.33
elif (courseOneGrade == "C"):
  print(f"Grade point for course 1 is: 2.0")
  courseOneGradeFloat = 2.0
elif (courseOneGrade == "D"):
  print(f"Grade point for course 1 is: 1.0")
  courseOneGradeFloat = 1.0
else:
  print(f"Grade point for course 1 is: 0.0")  
  courseOneGradeFloat = 0.0

courseTwoGrade = input("Enter your course 2 letter grade: ")
courseTwoCredit = input("Enter your course 2 credit: ")
courseTwoCredit = float(courseTwoCredit)
if (courseTwoGrade == "A"):
  print(f"Grade point for course 2 is: 4.0")
  courseTwoGradeFloat = 4.0
elif (courseTwoGrade == "A-"):
  print(f"Grade point for course 2 is: 3.67")
  courseTwoGradeFloat = 3.67
elif (courseTwoGrade == "B+"):
  print(f"Grade point for course 2 is: 3.33")
  courseTwoGradeFloat = 3.33
elif (courseTwoGrade == "B"):
  print(f"Grade point for course 2 is: 3.0")
  courseTwoGradeFloat = 3.0
elif (courseTwoGrade == "B-"):
  print(f"Grade point for course 2 is: 2.67")
  courseTwoGradeFloat = 2.67
elif (courseTwoGrade == "C+"):
  print(f"Grade point for course 2 is: 2.33")
  courseTwoGradeFloat = 2.33
elif (courseTwoGrade == "C"):
  print(f"Grade point for course 2 is: 2.0")
  courseTwoGradeFloat = 2.0
elif (courseTwoGrade == "D"):
  print(f"Grade point for course 2 is: 1.0")
  courseTwoGradeFloat = 1.0
else:
  print(f"Grade point for course 2 is: 0.0")  
  courseTwoGradeFloat = 1.0

courseThreeGrade = input("Enter your course 3 letter grade: ")
courseThreeCredit = input("Enter your course 3 credit: ")
courseThreeCredit = float(courseThreeCredit)
if (courseThreeGrade == "A"):
  print(f"Grade point for course 3 is: 4.0")
  courseThreeGradeFloat = 4.0
elif (courseThreeGrade == "A-"):
  print(f"Grade point for course 3 is: 3.67")
  courseThreeGradeFloat = 3.67
elif (courseThreeGrade == "B+"):
  print(f"Grade point for course 3 is: 3.33")
  courseThreeGradeFloat = 3.33
elif (courseThreeGrade == "B"):
  print(f"Grade point for course 3 is: 3.0")
  courseThreeGradeFloat = 3.0
elif (courseThreeGrade == "B-"):
  print(f"Grade point for course 3 is: 2.67")
  courseThreeGradeFloat = 2.67
elif (courseThreeGrade == "C+"):
  print(f"Grade point for course 3 is: 2.33")
  courseThreeGradeFloat = 2.33
elif (courseThreeGrade == "C"):
  print(f"Grade point for course 3 is: 2.0")
  courseThreeGradeFloat = 2.0
elif (courseThreeGrade == "D"):
  print(f"Grade point for course 3 is: 1.0")
  courseThreeGradeFloat = 1.0
else:
  print(f"Grade point for course 3 is: 0.0")  
  courseThreeGradeFloat = 0.0

GPA = (courseOneGradeFloat*courseOneCredit + courseTwoGradeFloat*courseTwoCredit + courseThreeGradeFloat*courseThreeCredit) / (courseOneCredit + courseTwoCredit + courseThreeCredit)
print(f"Your GPA is: {GPA}")