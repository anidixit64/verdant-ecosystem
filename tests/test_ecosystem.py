import sys
import os

# Add the root project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from verdant.ecosystem import Ecosystem

def test_ecosystem_initialization():
    eco = Ecosystem("Green Valley")
    assert eco.name == "Green Valley"
    assert eco.weather == "temperate"
    assert eco.species == []

def test_add_species():
    eco = Ecosystem("Green Valley")
    eco.add_species("Deer")
    assert "Deer" in eco.species
