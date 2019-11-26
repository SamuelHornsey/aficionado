# Makefile
# Author: Samuel Hornsey
MODULE=aficionado

test:
	pytest --cov=$(MODULE) tests/
