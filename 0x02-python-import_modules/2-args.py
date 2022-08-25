#!/usr/bin/python3

if __name__ == "__main__":
    import sys as s
    l = len(s.argv) - 1
    if l == 1:
        print("{:d} argument:".format(l))
        print("{:d}: {:s}".format(l, s.argv[l]))
    else:
        if l == 0:
            print("{:d} arguments.".format(l))
        else:
            print("{:d} arguments:".format(l))
            i = 1
            while (i <= l):
                print("{:d}: {:s}".format(i, s.argv[i]))
                i += 1
