# ANGEL GRACE MAMMAG
# 8-ADELFA

header = "STUDENT PERFORMANCE EVALUATOR"
def display_header():
    print (header)

def get_student_info(): #Asks the user for their input on 3 assessments & the student's name
    global student_name, assessment1, assessment2, assessment3
    student_name = input("Enter student name: ")
    assessment1 = int(input("Enter assessment 1: "))
    assessment2 = int(input("Enter assessment 2: "))
    assessment3 = int(input("Enter assessment 3: "))

def evaluate_performace(): #Calculates the average score & determines the performance level of the student
    global average_score, performance
    average_score = ((assessment1 + assessment2 + assessment3)/3)
    if average_score <= 100 and average_score >= 90:
        performance = "Outstanding"
    elif average_score < 90 and average_score >= 85:
        performance = "Very Satisfactory"
    elif average_score < 85 and average_score >= 80:
        performance = "Satisfactory"
    elif average_score < 80 and average_score >= 75:
        performance = "Fairly Satisfactory"
    elif average_score < 75:
        performance = "Needs Improvement"
def display_report(): #Displays full report of student's report
    print("STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {student_name}")
    print(f"Assessment Scores: {assessment1}, {assessment2}, {assessment3}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Performance Level: {performance}")

display_header()
get_student_info()
evaluate_performace()
display_report()