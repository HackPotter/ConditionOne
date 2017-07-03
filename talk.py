class talk:
    def __init__(self, GivenDay, GivenTime, GivenTrack, GivenTitle, GivenSpeakers, GivenDescription, GivenIDNum):
        self.day = GivenDay
        self.time = GivenTime
        self.track = GivenTrack
        self.title = GivenTitle
        self.speakers = GivenSpeakers
        self.description = GivenDescription
        self.idNum = GivenIDNum

    def ShowInfo(self):
        print "Talk " + str(self.idNum) + " On " + self.day + " at " + self.time + " in track " + str(self.track) + ": " + self.title

    def ShowDescription(self):
        print self.title
        print self.description