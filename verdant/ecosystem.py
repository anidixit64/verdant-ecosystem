class Ecosystem:
    def __init__(self, name, weather="temperate"):
        self.name = name
        self.weather = weather
        self.species = []

    def add_species(self, species_name):
        self.species.append(species_name)
