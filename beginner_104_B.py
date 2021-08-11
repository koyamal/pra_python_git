S = input()

outputFlag = True
if S[0] == "A":
    tempS = S[2:len(S)-1]
    if tempS.count("C") == 1:
        for i in S:
            if i == "A" or i == "C" or i.islower():
                pass
            else:
                outputFlag = False
    else:
        outputFlag = False
else:
    outputFlag = False

if outputFlag:
    print("AC")
else:
    print("WA")
