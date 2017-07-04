def TalkSearch(userInput, masterSchedule):
    searchString = userInput[7:] #Eliminates "search " from string
    matches = []
    for talk in masterSchedule:
        if str(talk.title).lower().__contains__(str(searchString).lower()):
            matches.append(talk)
    print "Search for \"" + str(searchString) + "\" produced " + str(matches.__len__()) + " matches."

    print "\nTime  Day ID  Title"
    for talk in matches:
        print talk.time + " " + talk.day[:3] + " " + "%03d" % int(talk.idNum) + " " + talk.title