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

    

def main():
    course = planetterp.course(name="CMSC430", reviews=False)
    courses = planetterp.courses(department="CMSC", limit=1)
    prof = planetterp.professor(name="Herve Franceschi", reviews=False)
    # profs = planetterp.professors(type_="ta", limit=2)
    # grades = planetterp.grades(course="MATH140", professor="Jon Snow")
    # course["professors"] = list(set(course["professors"]))
    # course["professors"] = list(set(course["professors"]))
    printCoursesInfo([course])
    # print(course)
    # print(prof)
    # print(profs)
    # print(grades)
    

if __name__ == "__main__":
    main()


