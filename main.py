import sys
import re
import string
import talk
import DefconParse
import ConHelp
import ConSchedule
import Search
import conflicts
import FreeBooked
import os
import platform

DEBUGGING = False

logoLine1 = "   _____                _ _ _   _              ____             "
logoLine2 = "  / ____|              | (_) | (_)            / __ \            "
logoLine3 = " | |     ___  _ __   __| |_| |_ _  ___  _ __ | |  | |_ __   ___ "
logoLine4 = " | |    / _ \| '_ \ / _` | | __| |/ _ \| '_ \| |  | | '_ \ / _ \\"
logoLine5 = " | |___| (_) | | | | (_| | | |_| | (_) | | | | |__| | | | |  __/"
logoLine6 = "  \_____\___/|_| |_|\__,_|_|\__|_|\___/|_| |_|\____/|_| |_|\___|"


try:
    html = open(sys.argv[1], 'r') #Open the file
    masterSchedule = DefconParse.Parse(html) #Send the file to the parser
    userSchedule = [] #Initialize the user schedule
except:
    sys.exit("EXITING WITH ERROR CODE 1:\n"
             "Either no file was given or file was unreadable.\n"
             "ConditionOne must be run in the following way:\n"
             "python main.py [PATH/TO/DEFCON_WEBSITE.HTML]\n"
             "If you don't have the website, download it here:\n"
             "https://www.defcon.org/html/defcon-25/dc-25-speakers.html")

if DEBUGGING: #PRINT STUFF
    i = 0
    while i < masterSchedule.__len__():
        print str(masterSchedule[i].day)
        i += 1

#Greet the user
print logoLine1 + "\n" + logoLine2 + "\n" + logoLine3 + "\n" + \
logoLine4 + "\n" + logoLine5 + "\n" + logoLine6 + "\n"
print "Welcome to ConditionOne, the DEFCON scheduling tool."
print str(masterSchedule.__len__()) + " Talks loaded from " + html.name + "."
print "Please enter a command, or type 'help' for a list of available commands."


#This is where the magic happens
userInput = raw_input(">") #get input
while userInput.lower().strip(" ") != "quit" and userInput.lower().strip(" ") != "exit": #Typing 'exit' or 'quit' stops the program
    if userInput.lower().__contains__("help"): #Get help
        ConHelp.ShowHelp(userInput.lower())

    elif userInput.lower()[:4] == "info": #Short form info
        nums = re.findall('\d+', userInput)
        for num in nums:
            if int(num) > masterSchedule.__len__():
                print "Talk " + str(num) + " not found."
                continue
            masterSchedule[int(num)].ShowInfo()

    elif userInput.lower()[:8] == "describe" or userInput.lower()[:2] == "d ": #Full Description
        nums = re.findall('\d+', userInput)
        for num in nums:
            if int(num) > masterSchedule.__len__():
                print "Talk " + str(num) + " not found."
                continue
            masterSchedule[int(num)].ShowDescription()

    elif userInput.lower()[:3] == "add": #add talk to schedule by id
        nums = re.findall('\d+', userInput) #get all numbers with regex
        if nums.__len__() == 0:
            print "No talk ID supplied."
        validNums = []
        for num in nums:
            if int(num) >= masterSchedule.__len__():
                print "Talk " + str(num) + " does not exist."
                nums.remove(num)
            for talk in masterSchedule:
                if talk.idNum == int(num):
                    validNums.append(num)
        validNums = list(set(validNums))
        for num in validNums:
            for talk in userSchedule:
                if talk.idNum == int(num):
                    print "Talk " + str(num) + " is already on schedule."
                    validNums.remove(num)
        for num in validNums:
            talk = masterSchedule[int(num)]
            userSchedule.append(talk)
            print "Added talk " + str(num) + " to schedule."

    elif userInput.lower()[:6] == "remove": #Remove talk from schedule by id
        nums = re.findall('\d+', userInput)
        if userSchedule.__len__() == 0:
            print "No talks on schedule to remove."
        elif userInput.lower().__contains__("all"):
            userSchedule = []
            print "All talks removed from schedule."
        elif nums.__len__() == 0:
            print "No talk ID supplied."
        nums = list(set(nums))
        for num in nums:
            for talk in userSchedule:
                if talk.idNum == int(num):
                    userSchedule.remove(talk)
                    print "Removed talk " + str(num) + " from schedule."
                    nums.remove(num)
        for num in nums:
            if userSchedule.__len__() > 0:
                print "Talk " + str(num) + " was not on schedule."

    elif userInput.lower()[:5] == "talks":
        idNum = 0
        while idNum < len(masterSchedule):
            print str(idNum) + "\t" + str(masterSchedule[idNum].title)
            idNum += 1

    elif userInput.lower()[:6] == "search":
        Search.TalkSearch(userInput, masterSchedule)

    elif userInput.lower()[:9] == "conflicts":
        conflicts.FindConflicts(userSchedule, True)

    elif userInput.lower()[:5] == "clear":
        if platform.system() == "Windows":
            os.system("cls")  # Clear terminal on windows systems
        else:
            os.system("clear")  # Clear terminal on unix systems

    elif userInput.lower()[:7] == "outline":
        FreeBooked.Outline(userSchedule)

    elif userInput.lower()[:9] == "happening":
        try:
            day = userInput.split(" ")[1]
            time = userInput.split(" ")[2]
            try:
                test = int(day)
                print "Error: command format is \"happening [DAY] [TIME]\""
            except:
                FreeBooked.happening(masterSchedule, day, time)
        except:
            print "Error: command format is \"happening [DAY] [TIME]\""

    elif userInput.lower()[:6] == "export":
        FreeBooked.export(userSchedule)
        print "User schedule exported to \"DEFCON 25 Schedule.txt\" in project directory."

    elif userInput.lower()[:5] == "about":
        print "ConditionOne is a personal DEFCON scheduling tool written by Jack Potter and licensed under the MIT open source license."
        print "It schedules talks that're listed on the website for regular conference times in the regular tracks."
        print "If you'd like to contribute to the development of ConditionOne, swing by " \
              "github.com/hackpotter/ConditionOne and fork the project."
        print "Also, thanks to patorjk (patorjk.com) for the ASCII art generator."
        print "Anyway, enjoy DEFCON, and remember the 3-2-1 rule."

    else:
        print "Command not recognized"

    userInput = raw_input(">")
if platform.system() == "Windows":
    os.system("cls") #Clear terminal on windows systems
else:
    os.system("clear") #Clear terminal on unix systems
