def parse_args(args):
    opts = {}
    opts_len = len(args)

    i = 0

    try:
        while i < opts_len:
            opts[args[i]] = args[i+1]
            i = i+2
    except IndexError:
        print("ERROR: Supplied an argument without value. \n")

    return opts
