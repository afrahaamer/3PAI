class student:
    def __init__(self, name = str(), ocean = [0,0,0,0,0], riasec = [0,0,0,0,0,0], chosen_subjects = []):
        self.name = name
        self.ocean = ocean
        self.riasec = riasec
        self.chosen_subjects = chosen_subjects

class subject:
    def __init__(self, nameosub = str(), cei = 0, blooms = ()):
        self.nameosub = nameosub
        self.cei = cei
        self.blooms = blooms

s1 = subject(nameosub="Math")
s2 = subject(nameosub="Chem")
s3 = subject(nameosub="Phy")
s4 = subject(nameosub="Bio")

S1 = student(name= "Bilal Aamer", chosen_subjects=[s1, s2,s3,s4])


print(S1.chosen_subjects[0].nameosub, S1.name)