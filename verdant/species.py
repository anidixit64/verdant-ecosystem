class Species:
    def __init__(self, name, population, growth_rate):
        self.name = name
        self.population = population
        self.growth_rate = growth_rate  # as a percentage, e.g., 5.0 for 5%

    def simulate_growth(self):
        self.population += int(self.population * (self.growth_rate / 100))

    def __str__(self):
        return f"{self.name}: {self.population} individuals"
