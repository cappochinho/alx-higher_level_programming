#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 2:
        print("{:d} argument:".format(l - 1))
        print("{:d}: {:s}".format(l - 1, argv[l - 1]))
    else:
        if l == 1:
            print("{:d} arguments.".format(l - 1))
        else:
            print("{:d} arguments:".format(l - 1))
            i = 1
            while (i <= l - 1):
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1
