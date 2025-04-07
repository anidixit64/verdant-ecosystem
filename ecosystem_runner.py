from verdant.ecosystem import Ecosystem
from verdant.species import Species

eco = Ecosystem("Verdant Valley")

eco.add_species(Species("Deer", 100, 10.0))
eco.add_species(Species("Rabbits", 50, 25.0))
eco.add_species(Species("Wolves", 10, 5.0))

print(eco)
for day in range(1, 4):
    print(f"\nDay {day}:")
    eco.simulate()
    for s in eco.species:
        print(s)
