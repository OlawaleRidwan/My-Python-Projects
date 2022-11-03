def admission_program(score):
    """
    This program calculate the aggregate score
    and tell the students the faculty and department he or she 
    is likely to be admiitted to

    """
    if(score <= 49):
        return "No admission"
    elif(score >= 50 and score <=54):
        return "Agric Science Department"
    elif(score >= 55 and score <=60):
        return "Botany or Zoology"
    elif(score >= 61 and score <= 70):
        return "Psychology or statistics"
    elif(score >= 71 and score <=74):
        return "Pharmacology or nursing"
    elif(score >= 75 and score <= 79):
        return "Insurance or Banking"
    elif(score >= 80):
        return "Medicine or Law"

print(admission_program(48))
print(admission_program(50))
print(admission_program(60))
print(admission_program(63))
print(admission_program(73))
print(admission_program(77))
print(admission_program(80))