def check_grade(grade):
    if grade <= 100 and grade >= 80:
        return "You did a great job!"
    elif grade <= 79 and grade >= 70:
        return "Keep it up!"
    elif grade <= 69 and grade >= 60:
        return "You passed, bit thre's room for improvement."
    elif grade <= 59:
        return "Better luck next time"
    
userGrade = int(input("Enter Grade : "))
print(check_grade(userGrade))
