import sys

def main(args=None):
    """The main routine."""
    
    if args is None:
        args = sys.argv[1:]
    
    # Parse args
    # TODO ...

    hest = 5
    mis = 3

    missekat = hest + mis
    print('The sum of {0} and {1} is {2}'.format(hest,mis,missekat))

if __name__ == "__main__":
    main()
