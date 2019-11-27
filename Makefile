# Makefile
# Author: Samuel Hornsey
MODULE=aficionado

# Run tests with coverage
test:
	pytest --cov=$(MODULE) tests/

# Clean distributions
clean:
	rm -rf dist *.egg-*