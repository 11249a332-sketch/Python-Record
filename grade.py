def grade_calc(assignments,midterm,final_exam):
    #calculate weighted average
    final_score = (assignments*0.4)+(midterm*0.3)+(final_exam*0.3)
    #Determine grade based on scale
    if 90<=final_score<=100:
        grade='A'
    elif 80<=final_score<=90:
        grade='B'
    elif 70<=final_score<=80:
        grade='C'
    elif 60<=final_score<=70:
        grade='D'
    else:
        grade='F'
    return f"Final score:{final_score:2f},Grade: {grade}"
#Example usage
print(grade_calc(85,78,92)) # Example input
