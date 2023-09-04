import pandas as pd
import openpyxl

currentMembers = pd.read_excel('/Users/kyancox/Developer/Random/Chamber Internship/COPY2022 Membership Address List copy.xlsx')
allMembers = pd.read_excel('/Users/kyancox/Developer/Random/Chamber Internship/COPY5.23.23 Current Member List Address copy.xlsx')

currentNames = currentMembers['Business Name']
allNames = allMembers['Business Name']

potentialMembers = allMembers[~allMembers['Business Name'].isin(currentNames)]

potentialMembers.to_excel('/Users/kyancox/Developer/Random/Chamber Internship/Potential_Members.xlsx', index=False)

print(potentialMembers)

def check():
    missedNames = []
    for new in potentialMembers['Business Name']:
        for name in currentNames:
            if name == new:
                missedNames += new
    print(missedNames)

check()