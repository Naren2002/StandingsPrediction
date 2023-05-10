# A python file to show proof of concept
import os
from dotenv import load_dotenv

load_dotenv()
teams = None

with open(os.getenv("STANDINGS_FILE"), "r") as file:
    teams = [
        list(i.split(',')) for i in file.readlines()
    ]

for i in range(len(teams)):
    teams[i][0] = teams[i][0].strip().lower()
    teams[i][1] = int(teams[i][1].strip())
    teams[i][2] = int(teams[i][2].strip())
    teams[i][3] = int(teams[i][3].rstrip(r'\n').strip())

print(teams)

matches = None

with open(os.getenv("MATCHES_FILE"), "r") as file:
    matches = [
        list(i.split(',')) for i in file.readlines()
    ]

for i in range(len(matches)):
    matches[i][0] = matches[i][0].strip().lower()
    matches[i][1] = matches[i][1].strip().lower()

print(matches)

user_opinion = None

with open(os.getenv("USER_OPINION"), "r") as file:
    user_opinion = list(map(str.lower, list(map(str.strip, file.readline().split(',')))))
    temp_dict = {}
    itr = 0
    for i in user_opinion:
        temp_dict[i] = itr
        itr += 1
    user_opinion = temp_dict

print(user_opinion)


for i in matches:
    for j in range(len(teams)):

        # First team in the tuple matches with the list element
        if teams[j][0] == i[0]:

            # If the first team is ranked higher, the win count gets incremented else loss count gets incremented
            if user_opinion[i[0]] < user_opinion[i[1]]:
                print(f"{i[0]} wins against {i[1]}")
                teams[j][1] += 1
            else:
                print(f"{i[1]} wins against {i[0]}")
                teams[j][2] += 1

        # second team in the tuple matches with the list element
        elif teams[j][0] == i[1]:

            # If the first team is ranked higher, then the loss count is incremented else win count gets incremented
            if user_opinion[i[0]] < user_opinion[i[1]]:
                teams[j][2] += 1
            else:
                teams[j][1] += 1
            
def custom_sort_standings(item):
    return item[1]

teams.sort(key=custom_sort_standings)

print(teams[::-1])