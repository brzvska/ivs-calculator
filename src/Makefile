APP = calculator/app.py
ZIP = xberez04_xvinog00_xmazur08

ifeq ($(UNAME), Linux)
PY = python3.10
else
PY = py
endif


.PHONY: all pack clean test doc run profile setup test-basic test-advanced

test: test-basic test-advanced

test-basic:
	$(PY) -m unittest -v test-basic.py

test-advanced:
	$(PY) -m unittest -v test-advanced.py

run:
	$(PY) $(APP)

setup: requirements.txt
	pip install -r $<

profile: profiling.py
	$(PY) -m profile -o ../profiling/output10_1 $< < ../profiling/10_1.txt