def ocean_calc():
    '''
    The Ten Item Personality Inventory was administered (see Gosling, S. D., Rentfrow, P. J., & Swann, W. B., Jr. (2003). A Very Brief Measure of the Big Five Personality Domains. Journal of Research in Personality, 37, 504-528.):

    \nTIPI1	Extraverted, enthusiastic.
    \nTIPI2	Critical, quarrelsome.
    \nTIPI3	Dependable, self-disciplined.
    \nTIPI4	Anxious, easily upset.
    \nTIPI5	Open to new experiences, complex.
    \nTIPI6	Reserved, quiet.
    \nTIPI7	Sympathetic, warm.
    \nTIPI8	Disorganized, careless.
    \nTIPI9	Calm, emotionally stable.
    \nTIPI10	Conventional, uncreative.

    \nThe following input items are to be rated within the following range:

    \n1 = Disagree strongly
    \n2 = Disagree moderately
    \n3 = Disagree a little
    \n4 = Neither agree nor disagree
    \n5 = Agree a little
    \n6 = Agree moderately
    \n7 = Agree strongly

    '''
    ocean = []
    print("The following input items are to be rated within the following range:")
    print("1 = Disagree strongly")
    print("2 = Disagree moderately")
    print("3 = Disagree a little")
    print("4 = Neither agree nor disagree")
    print("5 = Agree a little")
    print("6 = Agree moderately")
    print("7 = Agree strongly\n")

    TIPI = [
        "TIPI1 (Extraverted, enthusiastic)",
        "TIPI2 (Critical, quarrelsome)",
        "TIPI3 (Dependable, self-disciplined)",
        "TIPI4 (Anxious, easily upset)",
        "TIPI5 (Open to new experiences, complex)",
        "TIPI6 (Reserved, quiet)",
        "TIPI7 (Sympathetic, warm)",
        "TIPI8 (Disorganized, careless)",
        "TIPI9 (Calm, emotionally stable)",
        "TIPI10 (Conventional, uncreative)"
    ]
    

    for i in range(10):
        ocean.append(int(input("Enter " + TIPI[i] + " score: ")))

    oceanVals = [0,0,0,0,0]
    
    oceanVals[0] = ((ocean[4] + (8 - ocean[9]))/2) * (100/7)
    oceanVals[1] = ((ocean[2] + (8 - ocean[7]))/2) * (100/7)
    oceanVals[2] = ((ocean[0] + (8 - ocean[5]))/2) * (100/7)
    oceanVals[3] = ((ocean[6] + (8 - ocean[1]))/2) * (100/7)
    oceanVals[4] = ((ocean[8] + (8 - ocean[3]))/2) * (100/7)
    return oceanVals

print(ocean_calc())