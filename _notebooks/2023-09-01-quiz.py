import getpass
import sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = [
    {"question": "In what year was Yosemite National Park founded?", "answer": "1890"},
    {"question": "On average, around how many hundred thousand visitors does Crater Lake get annually?", "answer": "5"},
    {"question": "True or false: was Yellowstone the first national park founded?", "answer": "true"}
]

correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(len(questions)) + " questions.")

question_with_response("Are you ready to take a test?")

for question_data in questions:
    rsp = question_with_response(question_data["question"])
    if rsp.lower() == question_data["answer"]:
        print(rsp + " is correct!")
        correct += 1
    else:
        print(rsp + " is incorrect!")

print(getpass.getuser() + ", you scored " + str(correct) + "/" + str(len(questions)))