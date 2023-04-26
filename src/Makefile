ZIP = xberez04_xvinog00_xmazur08
APP = Calculator

ifeq ($(OS), Windows_NT)
	PY = py
	CLEANUP = rd /S /Q
	BUILDDIRS = "build" "dist"
else
	PY = python3.10
	CLEANUP = rm -rf
	BUILDDIRS = ../src/build/ ../src/dist/
endif

.PHONY: all pack clean test doc run profile setup test-basic test-advanced test-expr

test: test-basic test-advanced test-expr

test-basic: test-basic.py
		$(PY) -m unittest -v $<

test-advanced: test-advanced.py
		$(PY) -m unittest -v $<

test-expr: test-expression.py
		$(PY) -m unittest -v $<

run: calculator/app.py
		$(PY) $<

setup: requirements.txt
		pip install -r $<

build: setup
		pyinstaller app.spec

profile: profiling.py
		$(PY) -m profile -o ../profiling/output10_1 $< < ../profiling/10_1

clean:
		# $(CLEANUP) $(BUILDDIRS)
		rm -rf __pycache__/
		rm -rf calculator/__pycache__/
		rm -rf calculator/calclib/__pycache__/
		rm calculator/.DS_Store

pack:
		mkdir -p ../../$(ZIP)/doc
		mkdir -p ../../$(ZIP)/install
		mkdir -p ../../$(ZIP)/repo

		cp -a ../doc/* ../../$(ZIP)/doc
		cp ../src/dist/* ../../$(ZIP)/install
		cp -a ../. ../../$(ZIP)/repo

		rm -rf ../../$(ZIP)/repo/doc ../../$(ZIP)/repo/src/build/ ../../$(ZIP)/repo/src/dist/
		cd ../.. && zip -r $(ZIP).zip $(ZIP)

