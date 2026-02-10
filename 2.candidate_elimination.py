import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv('enjoysport.csv')
concepts = np.array(data.iloc[:, 0:-1])
target = np.array(data.iloc[:, -1])

print("Concepts:")
print(concepts)
print("Target:")
print(target)

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] 
                 for _ in range(len(specific_h))]

    print("\nInitial Specific Hypothesis:")
    print(specific_h)
    print("Initial General Hypothesis:")
    print(general_h)

    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        elif target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print(f"\nStep {i+1}")
        print("Specific Hypothesis:")
        print(specific_h)
        print("General Hypothesis:")
        print(general_h)

    # Remove overly general hypotheses
    general_h = [g for g in general_h if g != ['?'] * len(specific_h)]

    return specific_h, general_h

# Run algorithm
s_final, g_final = learn(concepts, target)

print("\nFinal Specific Hypothesis:")
print(s_final)

print("\nFinal General Hypothesis:")
print(g_final)
