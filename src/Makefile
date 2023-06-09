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

build:
		pyinstaller app.spec

profile: profiling.py
		printf "## Statistics for input size of 10\n\n" >> ../profiling/vystup.txt
		$(PY) -m profile $< < ../profiling/10_1 >> ../profiling/vystup.txt
		printf "\n## Statistics for input size of 1000\n\n" >> ../profiling/vystup.txt
		$(PY) -m profile $< < ../profiling/10_3 >> ../profiling/vystup.txt
		printf "\n## Statistics for input size of 1000000\n\n" >> ../profiling/vystup.txt
		$(PY) -m profile $< < ../profiling/10_6 >> ../profiling/vystup.txt

clean:
		$(CLEANUP) $(BUILDDIRS)
		rm -rf __pycache__/
		rm -rf calculator/__pycache__/
		rm -rf calculator/calclib/__pycache__/

pack:
		mkdir -p ../../$(ZIP)/doc
		mkdir -p ../../$(ZIP)/install
		mkdir -p ../../$(ZIP)/repo

		cp -a ../doc/* ../../$(ZIP)/doc
		cp ../src/dist/* ../../$(ZIP)/install
		cp ../src/profiling.py ../../$(ZIP)/install
		cp -a ../. ../../$(ZIP)/repo

		rm -rf ../../$(ZIP)/repo/doc ../../$(ZIP)/repo/src/build/ ../../$(ZIP)/repo/src/dist/
		cd ../.. && zip -r $(ZIP).zip $(ZIP)

doc: Doxyfile
		rm -rf ../doc/*
		doxygen
