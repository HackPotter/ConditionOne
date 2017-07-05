import conflicts

def Outline(userSchedule):
    #day    10 11 12 13 14 15 16 17
    thurs = [0, 0, 0, 0, 0, 0, 0, 0]
    fri = [0, 0, 0, 0, 0, 0, 0, 0]
    sat = [0, 0, 0, 0, 0, 0, 0, 0]
    sun = [0, 0, 0, 0, 0, 0, 0, 0]
    for talk in userSchedule:
        if talk.day == "Thursday":
            thurs[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Friday":
            fri[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Saturday":
            sat[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Sunday":
            sun[int(talk.time[:2]) - 10] = talk

    days = [thurs, fri, sat, sun]
    fullDay = ["Thursday", "Friday", "Saturday", "Sunday"]
    dayIndex = 0

    NumberOfConflicts = conflicts.FindConflicts(userSchedule, False)

    if NumberOfConflicts > 0:
        print "Error: " + str(NumberOfConflicts) + " conflicts detected."
        print "Outline cannot be generated until all conflicts are resolved."
        print "Run \"conflicts\" to see current conflicts that must be resolved."
        return


    print ""

    for day in days:
        hour = 10
        print fullDay[dayIndex]
        for time in day:
            if time == 0:
                print str(hour) + ":00\tFree"
            else:
                print str(hour) + ":00\t" + "Track " + str(time.track) + ", TalkID %03d: " % int(time.idNum) + str(time.title)
            hour += 1
        print ""
        dayIndex += 1

def happening(masterSchedule, day, time):

    if ["th", "thurs", "thursday"].__contains__(str(day).lower()): #standardize day format
        day = "Thursday"
    elif ["f", "fri", "friday"].__contains__(str(day).lower()):
        day = "Friday"
    elif ["sat", "saturday"].__contains__(str(day).lower()):
        day = "Saturday"
    elif ["sun", "sunday"].__contains__(str(day).lower()):
        day = "Sunday"

    notYetPrinted = True

    for talk in masterSchedule:
        if talk.day == day and int(talk.time[:2]) == int(time): #Add talks that match given date and time
            if notYetPrinted: #Column titles appear once if necessary
                print "\nTime  Day Track\tID  Title"
                notYetPrinted = False
            print talk.time + " " + talk.day[:3] + " " + "%03d\t" % int(talk.track)+ "%03d" % int(talk.idNum) + " " + talk.title

def export(userSchedule):
    # day    10 11 12 13 14 15 16 17
    thurs = [0, 0, 0, 0, 0, 0, 0, 0]
    fri = [0, 0, 0, 0, 0, 0, 0, 0]
    sat = [0, 0, 0, 0, 0, 0, 0, 0]
    sun = [0, 0, 0, 0, 0, 0, 0, 0]
    for talk in userSchedule:
        if talk.day == "Thursday":
            thurs[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Friday":
            fri[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Saturday":
            sat[int(talk.time[:2]) - 10] = talk
        elif talk.day == "Sunday":
            sun[int(talk.time[:2]) - 10] = talk

    days = [thurs, fri, sat, sun]
    fullDay = ["Thursday", "Friday", "Saturday", "Sunday"]
    dayIndex = 0

    NumberOfConflicts = conflicts.FindConflicts(userSchedule, False)

    exportFile = open("DEFCON 25 Schedule.txt", 'w')

    if NumberOfConflicts > 0:
        print "Error: " + str(NumberOfConflicts) + " conflicts detected."
        print "Outline cannot be generated until all conflicts are resolved."
        print "Run \"conflicts\" to see current conflicts that must be resolved."
        return

    for day in days:
        hour = 10
        exportFile.write("\n" + fullDay[dayIndex] + "\n")
        for time in day:
            if time == 0:
                exportFile.write( str(hour) + ":00\tFree\n")
            else:
                exportFile.write( str(hour) + ":00\t" + "Track " + str(time.track) + \
                                  ", TalkID %03d: " % int(time.idNum) + str(time.title) + "\n")
            hour += 1
        exportFile.write("")
        dayIndex += 1