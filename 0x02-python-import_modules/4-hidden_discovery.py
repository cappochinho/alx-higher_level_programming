#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h
    for l in dir(h):
        if l[:2] != "__":
            print("{:s}".format(l))
