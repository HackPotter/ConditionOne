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
                conflictingTalks.append(talk)
                conflictingTalks.append(userSchedule[index])
                conflicts += 1
        index += 1

    if conflicts == 1:
        conflicts = 2

    if conflicts > 0:
        if printing:
            print "Warning: " + str(conflicts) + " conflicting talks found."
            print "\nTime  Day ID  Title"
            conflictingTalks = list(set(conflictingTalks))
            for talk in conflictingTalks:
                print talk.time + " " + talk.day[:3] + " " + "%03d" % int(talk.idNum) + " " + talk.title
            print""

    elif conflicts == 0:
        print "You have scheduled " + str(userSchedule.__len__()) + " talk(s) with 0 conflicts."
    return conflicts