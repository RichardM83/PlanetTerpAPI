import planetterp

def printReviews(reviews):
    for i, review in enumerate(reviews):
        print("-----------------")
        print("Review " + str(i) + ": " + review["course"] + " With " + review["professor"] + " at " + review["created"])
        print("Student received a: " + review["expected_grade"])
        print("Rating: " + str(review["rating"]))
        print("Response: " + review["review"])

def printCourseInfo(course):
    print("==========================================")
    print("Course: " + course["department"] + course["course_number"])
    print("Professors: " + ", ".join(sorted(list(set(course["professors"])))))
    print("Average GPA: " + str(course["average_gpa"]))
    print("Description: " + course["description"])
    print("General Education Credits: " + (course["geneds"] if course["geneds"] is not None else "None"))
    print("-------------------------------------")
    print("Reviews: " + printReviews(course["reviews"] if printReviews(course["reviews"]) is not None else "None"))
    print("==========================================")

def printCoursesInfo(courses):
    for course in courses:
        printCourseInfo(course)

def printProfInfo(prof):
    print("==========================================")
    print("Name: " + prof["name"])
    print("Rating: " + str(prof["average_rating"]))
    print("Courses Taught: " + "[" + ", ".join(prof["courses"]) + "]")
    print("Reviews: " + printReviews(prof["reviews"] if printReviews(prof["reviews"]) is not None else "None"))
    print("==========================================")

def printProfsInfo(profs):
    for prof in profs:
        printProfInfo(prof)
    

def main():
    course = planetterp.course(name="CMSC430", reviews=False)
    courses = planetterp.courses(department="CMSC", limit=1)
    prof = planetterp.professor(name="Herve Franceschi", reviews=True)
    # profs = planetterp.professors(type_="ta", limit=2)
    # grades = planetterp.grades(course="MATH140", professor="Jon Snow")
    # course["professors"] = list(set(course["professors"]))
    # course["professors"] = list(set(course["professors"]))
    # printCoursesInfo([course])
    # print(course)
    printProfInfo(prof)
    # print(prof)
    # print(grades)
    

if __name__ == "__main__":
    main()


