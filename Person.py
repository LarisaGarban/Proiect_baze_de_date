import os


class Person:

    def __init__(self, peopleID, people_name, people_height, people_mass,
                 people_hair_color, people_skin_color, people_eye_color, people_birth_year,
                 people_gender, people_homeworld_id, people_species_id):
        self.peopleID = peopleID
        self.people_name = people_name
        self.people_height = people_height
        self.people_mass = people_mass
        self.people_hair_color = people_hair_color
        self.people_skin_color = people_skin_color
        self.people_eye_color = people_eye_color
        self.people_birth_year = people_birth_year
        self.people_gender = people_gender
        self.people_homeworld_id = people_homeworld_id
        self.people_species_id = people_species_id
        self.vehicles = ()
        self.starships = ()

    def add_vehicles(self, vehicles):
        self.vehicles = vehicles

    def add_starships(self, starships):
        self.starships = starships

    def adauga_spatii_inainte_de_fiecare_linie(self, str):
        text = ""
        for chr in str:
            if chr is os.linesep:
                text += "     " + os.linesep
            else:
                text += chr

        return text

    def __str__(self):
        text = ""

        text += "peopleID: " + str(self.peopleID) + os.linesep
        text += "people_name: " + self.people_name + os.linesep
        text += "people_height: " + str(self.people_height) + os.linesep
        text += "people_mass: " + str(self.people_mass) + os.linesep
        text += "people_hair_color: " + self.people_hair_color + os.linesep
        text += "people_skin_color: " + self.people_skin_color + os.linesep
        text += "people_eye_color: " + self.people_eye_color + os.linesep
        text += "people_birth_year: " + str(self.people_birth_year) + os.linesep
        text += "people_gender: " + self.people_gender + os.linesep
        text += "people_homeworld_id: " + str(self.people_homeworld_id) + os.linesep
        text += "people_species_id: " + str(self.people_species_id) + os.linesep

        if self.vehicles != None:
            text += "The vehicles of this person are: " + os.linesep
            for vehicle in self.vehicles:
                text += self.adauga_spatii_inainte_de_fiecare_linie(str( vehicle )) + os.linesep
        else:
            text += "This person has no any vehicle" + os.linesep

        if self.starships != None:
            text += "The starships of this person are: " + os.linesep
            for starship in self.starships:
                text += self.adauga_spatii_inainte_de_fiecare_linie(str( starship )) + os.linesep
        else:
            text += "This person has no any starship" + os.linesep

        return text