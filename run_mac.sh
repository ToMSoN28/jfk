#!/bin/bash

# Check if the input file exists
if [ ! -f output.ll ]; then
  echo "Error: output.ll file not found."
  exit 1
fi

# Step 1: Compile LLVM IR to object file
llc output.ll -filetype=obj -o out.o

# Step 2: Link the object file to create an executable
clang out.o -o out

# Check if the output executable is created
if [ -f out ]; then
  echo "Executable 'out' has been successfully created."
else
  echo "Error: Failed to create executable."
  exit 1
fi

# Step 3: Run the executable
./out
