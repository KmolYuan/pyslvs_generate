all: build

# into package folder
build: *.pyx
ifeq ($(OS),Windows_NT)
	python setup.py build_ext --inplace
else
	python3 setup.py build_ext --inplace
endif

test: build
ifeq ($(OS),Windows_NT)
	python test.py
else
	python3 test.py
endif

clean:
ifeq ($(OS),Windows_NT)
	del *.pyd /q
	rd .\build /s /q
	del *.c /q
else
	rm -f *.so
	rm -f -r build
	rm -f *.c
endif
