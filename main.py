import sys
import re
import string
import talk
import DefconParse
import ConHelp
import ConSchedule

DEBUGGING = False

try:
    html = open(sys.argv[1], 'r') #Open the file
    masterSchedule = DefconParse.Parse(html) #Send the file to the parser
    userSchedule = [] #Initialize the user schedule
except:
    sys.exit("EXITING WITH ERROR CODE 1:\nEither no file was given or file was unreadable.")

if DEBUGGING: #PRINT STUFF
    i = 0
    while i < masterSchedule.__len__():
        print str(masterSchedule[i].day)
        i += 1

#Greet the user
print "Welcome to ConditionOne, the DEFCON scheduling tool."
print "After scanning " + html.name + ", " + str(masterSchedule.__len__() ) + " talks were loaded."
print "Please enter a command, or type 'help' for a list of available commands."


#This is where the magic happens
userInput = raw_input() #get input
while userInput.lower() != "quit" and userInput.lower() != "exit": #Typing 'exit' or 'quit' stops the program
    if userInput.lower().__contains__("help"): #Get help
        print userInput.lower()
        ConHelp.ShowHelp(userInput.lower())

    elif userInput.lower().__contains__("info"): #Short form info
        nums = re.findall('\d+', userInput)
        for num in nums:
            if int(num) > masterSchedule.__len__():
                print "Talk " + str(num) + " not found."
                continue
            masterSchedule[int(num)].ShowInfo()

    elif userInput.lower().__contains__("describe"): #Full Description
        nums = re.findall('\d+', userInput)
        for num in nums:
            if int(num) > masterSchedule.__len__():
                print "Talk " + str(num) + " not found."
                continue
            masterSchedule[int(num)].ShowDescription()

    elif userInput.lower().__contains__("add"): #add talk to schedule by id
        nums = re.findall('\d+', userInput)
        for num in nums:
            for talk in masterSchedule:
                if talk.idNum == int(num):
                    userSchedule.append(talk)
                    print "Added talk " + str(num) + " to schedule."

    elif userInput.lower().__contains__("remove"):
        nums = re.findall('\d+', userInput)
        for num in nums:
            for talk in userSchedule:
                if talk.idNum == int(num):
                    userSchedule.remove(talk)
                    print "Removed talk " + str(num) + " from schedule."

    elif userInput.lower()[:8] == "schedule":
        day = userInput[8:]
        ConSchedule.schedule(userSchedule, day)

    elif userInput.lower()[:5] == "talks":
        idNum = 0
        while idNum < len(masterSchedule):
            print str(idNum) + "\t" + str(masterSchedule[idNum].title)
            idNum += 1

    else:
        print "Command not recognized"
    userInput = raw_input()