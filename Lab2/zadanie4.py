import argparse
import os
import sys
import re

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-c', action='store', type=str, help='Choose character', default='\\')
my_parser.add_argument('revs', metavar='FILE', type=argparse.FileType('r+'), nargs='*', help='Files to change')
my_parser.add_argument('--leading-spaces', action='store_true', help='delete leading spaces')
my_parser.add_argument('--spaces', action='store_true', help='delete additional spaces')


args = my_parser.parse_args()

if not args.revs:
    print('Specify files names')
    exit(0)

c = args.c
l = len(args.revs)
wyr = r".*" + re.escape(c) + "\s*\n"
ww = r"(.*)" + re.escape(c) + "\s*\n"
# ff = open("res.txt", "w")

for i in range(l):

    file = args.revs[i]
    lines = file.readlines()
    k = len(lines)
    file.seek(0)
    file.truncate()
    for j in range(k):
        st = str(lines[j])
        m = re.search(wyr, st)
        if m:
            op = re.search(ww, lines[j])
            file.write(op.group(1))
        else:
            file.write(lines[j])
    file.close()

    if args.spaces:
        file = open(str(file.name), 'r+')
        spac = r"^( *.*?)  +(.*\n)"
        sss = r" +$"
        lines = file.readlines()
        k = len(lines)
        file.seek(0)
        file.truncate()
        for j in range(k):
            st = str(lines[j])
            m = re.search(spac, st)
            w = False
            if m:
                w = re.search(sss, m.group(1))
                if not w:
                    w = True
                else:
                    w = False
            while m and w:
                st = m.group(1) + m.group(2)
                m = re.search(spac, st)
                if m:
                    w = re.search(sss, m.group(1))
                    if not w:
                        w = True
                    else:
                        w = False
            file.write(st)
        file.close()

    if args.leading_spaces:
        file = open(str(file.name), 'r+')
        spac = r"^ *(.*\n)"
        lines = file.readlines()
        k = len(lines)
        file.seek(0)
        file.truncate()
        for j in range(k):
            m = re.search(spac, lines[j])
            file.write(m.group(1))
        file.close()



