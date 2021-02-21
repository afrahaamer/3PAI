from std_sub_class import student,subject

s1 = subject(nameosub="Math")
S1 = student(name= "Bilal Aamer", chosen_subjects=[s1])

print(S1.chosen_subjects[0].nameosub, S1.name)