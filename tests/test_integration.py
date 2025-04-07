import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from verdant.ecosystem import Ecosystem
from verdant.species import Species


def test_ecosystem_simulation_growth():
    eco = Ecosystem("Test Valley")
    deer = Species("Deer", 100, 10.0)
    eco.add_species(deer)
    eco.simulate()
    assert deer.population == 110
