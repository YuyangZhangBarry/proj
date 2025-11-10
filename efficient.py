"""implementation of the memory efficient solution"""

# import modules
import argparse
from input_generate import generate

# cost
ALPHA = {
    ('A','A') : 0,
    ('C','C') : 0,
    ('G','G') : 0,
    ('T','T') : 0,
    ('A','C') : 110,
    ('C','A') : 110,
    ('A','G') : 48,
    ('G','A') : 48,
    ('A','T') : 94,
    ('T','A') : 94,
    ('C','G') : 118,
    ('G','C') : 118,
    ('C','T') : 48,
    ('T','C') : 48,
    ('G','T') : 110,
    ('T','G') : 110
}
DELTA = 30

# dp algorithm
def efficient(s1,s2):
    # code goes here
    pass




# main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required=True,type=str,help="path to datapoints")

    args = parser.parse_args()

    # input generation
    #s1,s2 = generate(args.input)

    # add time & memory assessment here
    # time_calc()
    # memory_calc()

    #efficient(args.input)

if __name__ == '__main__':
    main()