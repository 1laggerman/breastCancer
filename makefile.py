import pandas as pd

def numStage(stringStage):
    if ("Stage 0" == stringStage):
        return 0
    elif ("Stage I" == stringStage):
        return 1
    elif ("Stage IA" == stringStage):
        return 2
    elif ("Stage IB" == stringStage):
        return 3
    elif ("Stage II" == stringStage):
        return 4
    elif ("Stage IIA" == stringStage):
        return 5
    elif ("Stage IIB" == stringStage):
        return 6
    elif ("Stage III" == stringStage):
        return 7
    elif ("Stage IIIA" == stringStage):
        return 8
    elif ("Stage IIIB" == stringStage):
        return 9
    elif ("Stage IIIC" == stringStage):
        return 10
    elif ("Stage IV" == stringStage):
        return 11
    elif ("Stage X" == stringStage):
        return 12
    else:
        return -1
    
    
    

readfile = pd.read_csv("lnXi.csv")

readfile = readfile.iloc[:17003, 5:-3]

X = readfile.iloc[3:, :]
Y = readfile.iloc[0, :]

for i in range(Y.size):
    num = numStage(Y.iloc[i])
    if (num == -1):
        print("Error at ", i)
        print("stage: ", "Stage 0" in Y.iloc[i])
        exit(1)
    Y.iloc[i] = num

# print(X)
# print(Y)

X.loc[len(X) + 3] = Y

print(X)

# X.to_csv("Raw_ln.csv")

# .to_csv("lnXi.csv")