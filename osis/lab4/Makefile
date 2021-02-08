BUILD_DIR = build
TESTS_DIR = tests

all: build
	gcc main.c inverser.c -o ${BUILD_DIR}/program -Wall

main:
	gcc main.c -o ${BUILD_DIR}/main -Wall

inverser:
	gcc inverser.c -o ${BUILD_DIR}/inverser -Wall

tests: clean_tests all
	./run_tests.sh

clean_tests:
	rm -f ${TESTS_DIR}/output[0123456789]*.txt

build:
	mkdir build

clean: clean_tests
	rm -rf build