name = input("Enter your fullname:\n")
total_score = 0
total_unit = 0
total_gradePoint = 0
course_grade = 0
if len(name) < 10:
    print("Enter Your Fullname\n")
else:
    level = input("Enter your level:\n")
    courses = int(input("Enter the number of courses you offered:\n"))
    for i in range(0, courses):
        course_title = input("Enter Your {0} course Title:\n".format(i+1))
        course_unit = int(input("Enter Your " + course_title + " course unit:\n"))
        course_score = int(input("Enter Your " + course_title + " course  score:\n"))
        if 70 >= course_score <= 100:
            course_grade = 5
        elif 60 >= course_score < 70:
            course_grade = 4
        elif 50 >= course_score < 60:
            course_grade = 3
        elif 45 >= course_score < 50:
            course_grade = 2
        elif 40 >= course_score < 45:
            course_grade = 1
        elif course_score < 40:
            course_grade = 0
        else:
            print("Error: Course Score must be more than 100 and not less than 0")

        course_gradePoint = course_grade * course_unit
        total_gradePoint += course_gradePoint
        total_unit += int(course_unit)

    gradePoint = total_gradePoint/total_unit
    print("Dear {0}".format(name))
    print("Your GradePoint for this semester is : {0}".format(gradePoint))
