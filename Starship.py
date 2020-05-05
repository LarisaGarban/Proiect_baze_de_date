import os


class Starship:
    def __init__(self, peopleID, starshipID, people_starship_description):
        self.peopleID = peopleID
        self.starshipID = starshipID
        self.people_starship_description = people_starship_description


    def __str__(self):
        text  = ""
        text += "peopleID: " + str(self.peopleID) + os.linesep
        text += "starshipID: " + str(self.starshipID) + os.linesep
        text += "people_starship_description: " + self.people_starship_description + os.linesep

        return text
