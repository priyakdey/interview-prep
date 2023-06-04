#!/usr/bin/env python3
import os
import sys


if len(sys.argv) < 2:
    print('ERROR: missing filename. usage - ./mkfile.py "<input_problem_summary>"')
    exit(1)

input_problem_summary = sys.argv[1].strip().lower()

tokens = []
token = []
for ch in input_problem_summary:
    if ch == "." or ch == " " or ch == "-":
        if len(token) != 0:
            tokens.append("".join(token))
            token = []
    else:
        token.append(ch)

if len(token) != 0:
    tokens.append("".join(token))

filename = "_".join(tokens) + ".py"
print(filename)

# create the file
with open(filename, "w") as fp:
    pass
