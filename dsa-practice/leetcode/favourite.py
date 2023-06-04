#!/usr/bin/env python3

# script to list the names of the problems which are tagged favourite

import os


for filename in os.listdir("./"):
    if os.path.isfile(filename):
        with open(filename) as fp:
            first_line = fp.readline().strip("\n")
            if first_line.__contains__("tag: favourite") or first_line.__contains__(
                "tag:favourite"
            ):
                print(filename)
