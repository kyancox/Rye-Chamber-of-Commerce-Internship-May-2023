import pandas as pd
import openpyxl

# Reads both Excel files
currentMembers = pd.read_excel('/Users/kyancox/Developer/Random/Chamber Internship/COPY2022 Membership Address List copy.xlsx')
allMembers = pd.read_excel('/Users/kyancox/Developer/Random/Chamber Internship/COPY5.23.23 Current Member List Address copy.xlsx')

# Extracts only 'Business Name' columns
currentNames = currentMembers['Business Name']
allNames = allMembers['Business Name']

# Filter the 'allMembers' DataFrame to exclude current members
potentialMembers = allMembers[~allMembers['Business Name'].isin(currentNames)]

# Saves filtered DataFrame to new Excel file in Chamber Internship folder
potentialMembers.to_excel('/Users/kyancox/Developer/Random/Chamber Internship/Potential_Members.xlsx', index=False)

print(potentialMembers)

# Checks to see if pandas library missed any business names 
def check():
    missedNames = []
    for new in potentialMembers['Business Name']:
        for name in currentNames:
            if name == new:
                missedNames += new
    print(missedNames)

check()