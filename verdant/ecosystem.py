from verdant.species import Species


class Ecosystem:
    def __init__(self, name, weather="temperate"):
        self.name = name
        self.weather = weather
        self.species = []

    def add_species(self, species):
        if isinstance(species, Species):
            self.species.append(species)

    def simulate(self):
        for s in self.species:
            s.simulate_growth()

    def __str__(self):
        return (
            f"Ecosystem: {self.name} ({self.weather}) with {len(self.species)} species"
        )
