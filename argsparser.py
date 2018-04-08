def parseArgs(args):
    opts = {}
    optsLen = len(args)

    i = 0

    try:
        while i < optsLen:
            opts[args[i]] = args[i+1]
            i = i+2
    except IndexError:
        print("ERROR: Supplied an argument without value. \n")

    return opts