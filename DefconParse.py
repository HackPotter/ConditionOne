import string
import talk

DEBUGGING = False

masterSchedule = []

talkPRE = '<h3 class="talkTitle">'
talkPOST = '</h3>'

dayTimeTrackPRE = '<p class="abstract">'
dayTimeTrackPOST = '</p>'

speakerPRE = '<h4 class="speaker">'
speakerPOST = '<span'

descriptionPRE = '<p class="abstract">'
descriptionPOST = '</p>'

def Parse(html):
    htmlString = html.read()
    idNum = 0
    while len(htmlString) != 0 and string.find(htmlString, "day at") != -1: #crude, but that string existing means that there's another talk to parse
        #Get Talk Title
        start = string.find(htmlString, talkPRE) + len(talkPRE) # Establishes start index as first letter in title
        htmlString = htmlString[start:] #Trims down the file
        stop = string.find(htmlString, talkPOST) #Establishes stop index as last letter in title
        title = htmlString[:stop] #Establishes talk title
        htmlString = htmlString[stop:]

        #Get talk day
        start = string.find(htmlString, dayTimeTrackPRE) + len(dayTimeTrackPRE) #Establishes start as first letter in day / time / track string
        htmlString = htmlString[start:] #Trims down the file
        stop = string.find(htmlString, 'day') + 3 #Establishes stop as end of day
        day = htmlString[:stop]
        if len(day) > 8:
            continue
        htmlString = htmlString[stop:]

        #Get talk time
        start = string.find(htmlString, ':') - 2 #Set start index as 2 chars before ':' which will always work as earliest talk is at 10:00
        if start - stop > 25: #ugly hack to fix annoying bug
            continue
        htmlString = htmlString[start:] #Trims string
        time = htmlString[:5] #Establishes talk time

        #Get talk track
        if string.find(htmlString[:25], '101') != -1: #if '101' appears, making it the track
            track = 101
        else:
            track = htmlString[15] #Probably shouldn't be hardcoded but it's more efficient that hunting for the next digit
        if not str(track).isdigit(): #Special cases such as "20:00 - 22:00 in Modena Room" are rare and can be their own thing implemented later. They only come up ~4 times.
            continue

        #Get speaker
        start = string.find(htmlString, speakerPRE) + len(speakerPRE)
        stop = string.find(htmlString, speakerPOST)
        speaker = htmlString[start:stop] #sets speaker value
        htmlString = htmlString[stop:] #trims down file (I know I'm inconsistent with file vs string. Sorry.)

        #Get description - KNOWN BUG - LINE BREAKS (<br>) ARE STILL IN TEXT
        start = string.find(htmlString, descriptionPRE) + len(descriptionPRE)
        htmlString = htmlString[start:]
        stop = string.find(htmlString, descriptionPOST)
        description = htmlString[:stop]

        if DEBUGGING:
            print "Title: " + title
            print "Day: " + day
            print "Time: " + time
            print "Track: " + str(track)
            print "Speaker(s): " + speaker
            #print "Description: " + description

        masterSchedule.append(talk.talk(day, time, track, title, speaker, description, idNum)) #Add the talk to the list
        idNum += 1 #Increment identifier

    return masterSchedule