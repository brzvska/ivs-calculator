PY = py
APP = app.py
ZIP = xberez04_xvinog00_xmazur08

.PHONY: all pack clean test doc run profile setup test-basic test-advanced

test: test-basic test-advanced

test-basic:
	$(PY) -m unittest -v test-basic.py

test-advanced:
	$(PY) -m unittest -v test-advanced.py

run:
	$(PY) calculator/$(APP)

setup: requirements.txt
	pip install -r $<

