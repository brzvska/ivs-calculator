APP = calculator/app.py
ZIP = xberez04_xvinog00_xmazur08

ifeq ($(OS), Windows_NT)
	PY = py
else
	PY = python3.10
endif

.PHONY: all pack clean test doc run profile setup test-basic test-advanced test-expr

test: test-basic test-advanced test-expr

test-basic:
		$(PY) -m unittest -v test-basic.py

test-advanced:
		$(PY) -m unittest -v test-advanced.py

test-expr:
		$(PY) -m unittest -v test-expression.py

run: build
		$(PY) $(APP)

setup: requirements.txt
		pip install -r $<

build: setup
		pyinstaller --onefile --noconsole calculator/app.py

profile: profiling.py
		$(PY) -m profile -o ../profiling/output10_1 $< < ../profiling/10_1

clean:
		rm -rf ../src/build/ ../src/dist/
