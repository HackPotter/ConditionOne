def FindConflicts(givenSchedule, printing):
    userSchedule = []
    for talk in givenSchedule:
        userSchedule.append(talk)
    if userSchedule.__len__() == 0:
        if printing:
            print "No talks currently in schedule."
        return 0

    conflicts = 0
    conflictingTalks = []
    index = 0

    while index < userSchedule.__len__():
        for talk in userSchedule[(index+1):]:
            if talk.day == userSchedule[index].day and talk.time[:2] == userSchedule[index].time[:2]:
                conflictingTalks.append([talk, userSchedule[index]])
                conflicts += 1
        index += 1

    if conflicts > 0:
        if printing:
            print "Warning: " + str(conflicts) + " conflicting talks found."
            print "\nTime  Day ID  Title"
            printedTalks = [] #quick and dirty hack, I know. This should be done differently
            for conflict in conflictingTalks:
                for talk in conflict:
                    if not printedTalks.__contains__(talk):
                        print talk.time + " " + talk.day[:3] + " " + "%03d" % int(talk.idNum) + " " + talk.title
                        printedTalks.append(talk)
                conflictingTalks.remove(conflict)
            print""
    return conflicts