import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from verdant.ecosystem import Ecosystem
from verdant.species import Species

def test_ecosystem_initialization():
    eco = Ecosystem("Green Valley")
    assert eco.name == "Green Valley"
    assert eco.weather == "temperate"
    assert eco.species == []

def test_add_species():
    eco = Ecosystem("Green Valley")
    deer = Species("Deer", 100, 10.0)
    eco.add_species(deer)
    assert deer in eco.species
