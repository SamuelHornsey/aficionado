# Makefile
# Author: Samuel Hornsey
MODULE=aficionado

# Run tests with coverage
test:
ifdef specific
	pytest -k "$(specific)" tests/ -s
else
	pytest --cov=$(MODULE) tests/ -s
endif

report:
	pytest --cov-report html --cov=$(MODULE) tests/

# Clean distributions
clean:
	rm -rf dist *.egg-*
	rm -rf htmlcov