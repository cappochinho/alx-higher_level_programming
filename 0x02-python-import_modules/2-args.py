#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv) - 1
    print("{:d} {:s}{:s}".format(l, "argument" if l == 1 else "arguments",
                                 "." if l == 0 else ":"))
    for d, s in enumerate(argv):
        if d > 0:
            print("{:d}: {:s}".format(d, s))
