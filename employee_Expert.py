j=int(input("enter total employees:"))
employee=[]


def Insert_Employee():
    for i in range(j):
        employee_name=input("employee Name :")
        employee.append(employee_name)
    print(employee)
Insert_Employee()

    
def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation System")
    print("Please answer the following questions (1-5) for each criteria:")
    
    criteria = {
        "Quality of Work": 0,
        "Attendance/Punctuality": 0,
        "Communication Skills": 0,
        "Teamwork": 0,
        "Problem-solving Ability": 0
    }
    
    for criterion, _ in criteria.items():
        rating = int(input(f"Rate the employee's {criterion} (1-5): "))
        criteria[criterion] = rating
    
    total_score = sum(criteria.values())
    average_score = total_score / len(criteria)
    
    print("\nEmployee Performance Summary:")
    print("==============================")
    for criterion, rating in criteria.items():
        print(f"{criterion}: {rating}")
    print("==============================")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score:.2f}")
    
    if average_score >= 3:
        print("Overall Performance: Satisfactory")
    else:
        print("Overall Performance: Unsatisfactory")

evaluate_performance()