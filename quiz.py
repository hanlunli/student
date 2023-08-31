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

questions = [["What command is used to include other functions that were previously developed?","import"],["What command is used to evaluate correct or incorrect response in this example?","if"],["Each 'if' command contains an '_________' to determine a true or false condition?","expression"],
             ["What tag in html allows you to put images on your website", "<img>"]]
for i in questions:
    rsp = question_with_response(i[0])
    if rsp == i[1]:
        print(rsp + " is correct!")
        correct+=1
    else:
        print(rsp + " is incorrect!")


print(getpass.getuser() + " you scored " + str((correct/len(questions) * 100)//1) + '% of the questions correct' )