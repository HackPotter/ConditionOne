import talk
def schedule(userSchedule, givenDay):

    thursday = []
    friday = []
    saturday = []
    sunday = []


    for talk in userSchedule:
        if talk.day == "Thursday":
            thursday.append(talk)
        elif talk.day =="Friday":
            friday.append(talk)
        elif talk.day == "Saturday":
            saturday.append(talk)
        elif talk.day == "Sunday":
            sunday.append(talk)

    scheduleText = open("schedule.txt", 'w') #Creates the actual text file

    #Standardize day based on input
    day = str(givenDay).lower()
    day = day.strip(" ")
    if day == "th" or day == "thurs" or day == "thursday":
        day = "Thursday"
    elif day == "f" or day == "fri" or day == "friday":
        day = "Friday"
    elif day == "sat" or day == "saturday":
        day = "Saturday"
    elif day == "sun" or day == "sunday":
        day = "Sunday"
    else:
        print "Invalid day entered"

    scheduleText.write(day.upper() + "\n")

    if day == "Thursday":
        WriteSchedule(thursday, scheduleText)
    elif day == "Friday":
        WriteSchedule(friday, scheduleText)
    elif day == "Saturday":
        WriteSchedule(saturday, scheduleText)
    elif day == "Sunday":
        WriteSchedule(sunday, scheduleText)

    scheduleText.close()
    scheduleText = open("schedule.txt", "r")
    print "\n" + scheduleText.read()


def WriteSchedule(day, textFile): #ONLY WORKS PROPERLY IF THERE ARE NO CONFLICTS
    tracks = "     | 1 | 2 | 3 | 4 |101|"
    dividingLine = "     |---|---|---|---|---|"
    empty = "|   |   |   |   |   |"
    trackOne = "| X |   |   |   |   |"
    trackTwo = "|   | X |   |   |   |"
    trackThree = "|   |   | X |   |   |"
    trackFour = "|   |   |   | X |   |"
    track101 = "|   |   |   |   | X |"

    time = [0, 0, 0, 0, 0, 0, 0, 0] #10, 11, 12, 13, etc

    for talk in day:
        if str(talk.time).__contains__("10:"):
            time[0] = talk.track
        if str(talk.time).__contains__("11:"):
            time[1] = talk.track
        if str(talk.time).__contains__("12:"):
            time[2] = talk.track
        if str(talk.time).__contains__("13:"):
            time[3] = talk.track
        if str(talk.time).__contains__("14:"):
            time[4] = talk.track
        if str(talk.time).__contains__("15:"):
            time[5] = talk.track
        if str(talk.time).__contains__("16:"):
            time[6] = talk.track
        if str(talk.time).__contains__("17:"):
            time[7] = talk.track

    textFile.write(tracks + "\n")
    textFile.write(dividingLine + "\n")

    timeInt = 10

    for slot in time:
        slot = int(slot)
        if slot == 0:
            textFile.write(str(timeInt) + ":00" + empty + "\n")
            textFile.write(dividingLine + "\n")
        else:
            if slot == 1:
                textFile.write(str(timeInt) + ":00" + trackOne + "\n")
            elif slot == 2:
                textFile.write(str(timeInt) + ":00" + trackTwo + "\n")
            elif slot == 3:
                textFile.write(str(timeInt) + ":00" + trackThree + "\n")
            elif slot == 4:
                textFile.write(str(timeInt) + ":00" + trackFour + "\n")
            elif slot == 101:
                textFile.write(str(timeInt) + ":00" + track101 + "\n")
            textFile.write(dividingLine + "\n")
        timeInt += 1
