import argparse
import fileinput
import os
import sys
import re

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-c', action='store', type=str, help='Choose character', default='\\')
my_parser.add_argument('revs', metavar='FILE', type=argparse.FileType('r+'), nargs='*', help='Files to read, if empty,'
                                                                                 ' stdin is used', default=sys.stdin)
my_parser.add_argument('--leading-spaces', action='store_true', help='delete leading spaces')
my_parser.add_argument('--spaces', action='store_true', help='delete additional spaces')

# my_parser.parse_args(['input.txt'])
args = my_parser.parse_args()

reg = r"<stdin>"
napis = str(args.revs)
m = re.search(reg, napis)
f = 0
if m:
    f = 1
l = napis.count(',')
l += 1

if f == 1:
    l = 1
    file = open('stdin.txt', 'w+')
    drag = args.revs.read()
    file.write(drag)
    file.close()
    file = open('stdin.txt', 'r+')
    lines = file.readlines()
    k = len(lines)
    file.seek(0)
    file.truncate()
else:
    l = len(args.revs)

c = args.c

wyr = r".*" + re.escape(c) + "\s*\n"
ww = r"(.*)" + re.escape(c) + "\s*\n"
# ff = open("res.txt", "w")

for i in range(l):

    if f == 0:
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

    if f == 1:
        file = open(str(file.name), 'r')
        print('-' * 40)
        print(file.read())
        os.remove(str(file.name))
