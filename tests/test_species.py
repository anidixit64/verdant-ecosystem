import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from verdant.species import Species


def test_species_initialization():
    deer = Species("Deer", 100, 10.0)
    assert deer.name == "Deer"
    assert deer.population == 100
    assert deer.growth_rate == 10.0


def test_species_growth():
    deer = Species("Deer", 100, 10.0)
    deer.simulate_growth()
    assert deer.population == 110
