def ShowHelp(userInput):
    userInput = str(userInput).replace("help", " ")
    userInput = str(userInput).lstrip(" ") #removes help from beginning of string
    if userInput == "info": #Show help page for info command
        print "Usage: info [ID]"
        print "Displays basic information about talk with the given ID, with the following format:"
        print "Talk [ID] on [DAY] at [TIME] in [TRACK]: [TITLE]"

    elif userInput == "describe":
        print "Usage: describe [ID]"
        print "Displays talk title and full description about talk with the given ID, with the following format:"
        print "[TITLE]\n[DESCRIPTION]"

    elif userInput == "add":
        print "Usage: add [ID]..."
        print "Adds all talks with given IDs to user schedule."
        print "If the talk is already on the user schedule, no ID is given, or a talk with the given ID " \
              "doesn't exist at all, an error message will result."

    elif userInput == "remove":
        print "Usage: remove [ID]..."
        print "Removes all talks with given IDs from user schedule."
        print "If the talk(s) aren't on the user schedule, an error message will result."

    elif userInput == "schedule":
        print "Usage: schedule [DAY]"
        print "[DAY] can be entered in several formats (capitalization independent), which are as follows:"
        print "Thursday: Th, Thurs, Thursday"
        print "Friday: F, Fri, Friday"
        print "Saturday: Sat, Saturday"
        print "Sunday: Sun, Sunday"
        print "\"schedule [DAY]\" will show you your schedule as a simple grid for a given day."
        print "It will also export that day's schedule as \"schedule.txt\" in the program's directory."

    elif userInput == "talks":
        print "Usage: talks"
        print "Displays complete list of talk titles alongside IDs, making it easy to see all conference talks."

    elif userInput == "quit" or userInput == "exit":
        print "Usage: quit"
        print "Exits the program, clearing the user schedule."
        print "If \"schedule\" was used to generate \"schedule.txt\", the text file will not be affected."
        print "\"exit\" can be substituted for \"quit\" based on user preference."

    elif userInput == "about":
        print "Usage: about"
        print "Displays basic information about the program."

    else:
        print "Available commands: info, describe, add, remove, schedule, talks, quit, about"
        print "Type help [COMMAND] for help with a specific command"
    return
