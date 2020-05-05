import os


class Vehicle:
    def __init__(self, peopleID, vehicle_id, people_vehicle_description):
        self.peopleID = peopleID
        self.vehicle_id = vehicle_id
        self.people_vehicle_description = people_vehicle_description


    def __str__(self) :
        text = ""
        text += "peopleID: " + str(self.peopleID) + os.linesep
        text += "vehicle_id: " + str(self.vehicle_id) + os.linesep
        text += "people_vehicle_description: " + self.people_vehicle_description + os.linesep

        return text