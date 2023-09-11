InfoDb = []

# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "Temecula",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars": ["4Runner"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Shane",
    "LastName": "Lopez",
    "DOB": "February 27",
    "Residence": "San Diego",
    "Email": "???@powayusd.com",
    "Owns_Cars": ["2021-Insight"]
})

InfoDb.append({
    "FirstName": "Eric",
    "LastName": "Yu",
    "DOB": "January 40",
    "Residence": "GERMANY",
    "Email": "eroxisbald@gmail.com",
    "Owns_Cars": ["BUGATTI"]
})

InfoDb.append({
    "FirstName": "Hanlun",
    "LastName": "Li",
    "DOB": "November 30",
    "Residence": "San Diego",
    "Email": "hanlunli.007@gmail.com",
    "Owns_Cars": ["none"]
})

for i in range(len(InfoDb)):
    print(InfoDb[i])
print("---------------------------------------------------")
for i in range(len(InfoDb)-1,-1,-1):
    print(InfoDb[i])
print("---------------------------------------------------")
for i in range(len(InfoDb)):
    for j in InfoDb[i]:
        print(j, InfoDb[i][j])
    print('==============')
print("---------------------------------------------------")

def putInfo():
    temp = {}
    temp["FirstName"] = input('GIMME YO NAME: ')
    temp["LastName"] = input('GIMME YO LAST NAME: ')
    temp["DOB"] = input('GIMME YO BDAY: ')
    temp["Residence"] = input('GIMME YO ADDRESS (the city im not a creep): ')
    temp["Email"] = input('GIMME YO EMAIl: ')
    temp["Owns_Cars"] = input('GIMME YO CARS, seperated by a space: ').split()
    InfoDb.append(temp)

flag = input('Do you want to add to dictionary? (y/n): ')
if flag == 'y':
    putInfo()
else:
    print("ur gross")
print("---------------------------------------------------")

import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_with_response("Are you ready to take a test?")

questions = [{"What command is used to include other functions that were previously developed?":"import"},{"What command is used to evaluate correct or incorrect response in this example?":"if"},{"Each 'if' command contains an '_________' to determine a true or false condition?":"expression"},
             {"What tag in html allows you to put images on your website": "<img>"}]
for i in range(len(questions)):
    for j in questions[i]:
        rsp = question_with_response(j)
        if rsp == questions[i][j]:
            print(rsp + " is correct!")
            correct+=1
        else:
            print(rsp + " is incorrect!")


print(getpass.getuser() + " you scored " + str((correct/len(questions) * 100)//1) + '% of the questions correct' )
print("---------------------------------------------------")

