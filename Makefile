# Define variables
INPUT = ?code.txt
PYTHON_SCRIPT = cmp1.py

# Default target to run the program
all: run

# Rule to run the Python script with the input file as argument
$(INPUT): $(PYTHON_SCRIPT)
	python3 $(PYTHON_SCRIPT) $(INPUT)

# Rule to generate output.ll from cmp1.py using the input file
output.ll: $(PYTHON_SCRIPT) $(INPUT)
	python3 $(PYTHON_SCRIPT) $(INPUT)

# Detect the platform and set the correct clang target
OS := $(shell uname)
ARCH := $(shell uname -m)

# Set the target based on the OS and architecture
ifeq ($(OS),Darwin)
    TARGET = aarch64-apple-darwin
else ifeq ($(OS),Linux)
    ifeq ($(ARCH),x86_64)
        TARGET = x86_64-w64-mingw32
    else
        $(error Unsupported architecture)
    endif
else
    $(error Unsupported OS)
endif

# Rule to generate the program from output.ll using the correct clang target
program: output.ll
	clang --target=$(TARGET) output.ll -o program

# Rule to run the program
run: program
	./program

# Rule to clean up generated files
# clean:
# 	rm -f output.ll program
