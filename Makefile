PYTHON := python3

.PHONY: build
build:
	$(PYTHON) setup.py build

.PHONY: dist
dist:
	$(PYTHON) setup.py sdist

.PHONY: install
install:
	$(PYTHON) setup.py install --user

.PHONY: clean
clean:
	rm -rf \
		build \
		dist \
		src/*.egg-info
