"""implementation of the memory efficient solution"""

# import modules
import argparse
import math
from input_generate import generate
from basic import basic

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
def efficient(s1,s2,base_len):
    # code goes here
    # base length should be higher than at least 1
    base_len = max(base_len,1)


    def recur(start_1,end_1,start_2,end_2):
        if end_1 - start_1 + 1 <= base_len or end_2 - start_2 + 1:
            # solve this directly
            return basic(s1[start_1:end_1+1],s2[start_2:end_2+1])
        
        # split s1 in half
        mid = (start_1+end_1)//2

        dp, _, _, _ = basic(s1[start_1,mid+1],s2[start_2,end_2+1])

        dp_T, _, _, _ = basic(s1[end_1,mid,-1],s2[end_2:start_2-1,-1])

        split_point = 0


        #for i in range(dp[0]):

            


  
        

 





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