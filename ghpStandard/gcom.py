import sys
import os
import math
import random
filename = sys.argv[1]
open("write.c", "w").write("""
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

int main() {

""")
for liner in open(filename).readlines():
    line = liner.replace("\n", "")
    ls = line.split(" ")
    if ls[0] == "PRINTF":
        open("write.c", "a").write(f'printf("{ls[1]}\\n");')
open("write.c", "a").write('return 0;\n}')
os.system(f"gcc write.c -o {filename.replace(".gph", ".gpk")}")
os.remove(f"write.c")