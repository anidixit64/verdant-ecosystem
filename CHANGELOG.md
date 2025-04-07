# CHANGELOG

## [v0.1.0-dev] - 2025-05-07
Initial development milestone

### Added
- CLI entry point with Verdant banner
- Modular `Ecosystem` class with `add_species()` and `simulate()`
- Modular `Species` class with growth logic
- `simulation_runner.py` script to simulate growth over time
- Unit tests for Ecosystem, Species, and integration logic
- GitHub Actions CI for:
  - Running tests
  - Enforcing Black code formatting
