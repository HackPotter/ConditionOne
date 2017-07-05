def ShowHelp(userInput):
    userInput = str(userInput).replace("help", " ")
    userInput = str(userInput).lstrip(" ") #removes help from beginning of string
    userInput = str(userInput).lower() #Makes things easier later
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
        print "\"remove all\" is also a valid command, and will remove all talks from user schedule."
        print "If the talk(s) aren't on the user schedule, an error message will result."

    elif userInput == "schedule" and False: #Removed this bit for now since the visual schedule wasn't as good as the outline, imho
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

    elif userInput == "conflicts":
        print "Usage: conflicts"
        print "Checks user schedule for any conflicts, and displays any that are found."
        print "A conflict is defined as having multiple talks scheduled for the same time on the same day. "

    elif userInput == "about":
        print "Usage: about"
        print "Displays basic information about the program."

    elif userInput == "search":
        print "Usage: search [SEARCH STRING]"
        print "Displays all talks that have the given search string in their title."

    elif userInput == "clear":
        print "Usage: clear"
        print "Clears the screen of all text output."

    elif userInput == "outline":
        print "Usage: outline"
        print "Displays a simplified outline of all talks on user schedule."
        print "This outline can be exported with the \"export\" command."

    elif userInput == "export":
        print "Usage: export"
        print "Creates a text file with the user schedule outline in the project directory."
        print "The file will be called \"DEFCON 25 Schedule.txt\" and will be overwritten if export is run again."

    elif userInput == "happening":
        print "Usage: happening [DAY] [TIME]"
        print "Displays all talks happening at a given day and time."
        print "[DAY] can be entered in several formats (capitalization independent), which are as follows:"
        print "Thursday: Th, Thurs, Thursday"
        print "Friday: F, Fri, Friday"
        print "Saturday: Sat, Saturday"
        print "Sunday: Sun, Sunday"
        print "[TIME] can also be entered is several ways."
        print "For example, \"10\", \"10:00\", and \"1000\" are all valid inputs."
        print "Remember to use 24-hour time, so 1400 instead of 2."

    else:
        print "Available commands: search, info, describe, add, remove, outline, export, conflicts, talks, clear, quit, about"
        print "Type help [COMMAND] for help with a specific command"
    return
