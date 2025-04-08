.PHONY: all clean run

all: run

output.ll: cmp1.py code.txt
	python cmp1.py

program: output.ll
	clang --target=x86_64-w64-mingw32 output.ll -o program.exe

run: program
	./program.exe

clean:
	rm -f output.ll program
