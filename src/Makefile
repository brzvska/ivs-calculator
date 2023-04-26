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
		$(MOVE) dist/Calculator.* ../

profile: profiling.py
		$(PY) -m profile -o ../profiling/output10_1 $< < ../profiling/10_1

clean:
		$(CLEANUP) $(BUILDDIRS)

pack: $(ZIP)
		mkdir -p ../../$</doc
		mkdir -p ../../$</install
		mkdir -p ../../$</repo

		cp -r ../doc/* ../../$</doc
		cp ../src/dist/* ../../$</install
		cp -r ../* ../../$</repo

		rm -rf ../../$</repo/doc
		cd ../..
		zip -r $(ZIP).zip $(ZIP)

