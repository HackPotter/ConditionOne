def ShowHelp(userInput):
    userInput = str(userInput).lstrip("help ") #removes help from beginning of string
    print userInput
    if userInput == "info": #Show help page for info command
        print "Usage: info $ID"
    elif userInput == "describe":
        print "Usage: describe $ID"
    elif userInput == "add":
        print "Usage: add $ID"
    elif userInput == "remove":
        print "Usage: remove $ID"
    else:
        print "Available commands: info, describe, add, remove, schedule, talks"
        print "Type help $COMMAND for help with a specific command"
    return
