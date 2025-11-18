"""implementation of the basic DP solution"""

# import modules
import os
import argparse
import math
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
def basic(s1,s2):
    # code goes here
    n , m = len(s1), len(s2)
    dp = [[math.inf] * (m+1) for _ in range(n+1)] # m+1 columns, n+1 rows
    
    """bottom-up"""
    # initialization
    for i in range(m+1):
        dp[0][i] = i * DELTA
    for i in range(n+1):
        dp[i][0] = i * DELTA

    if n == 0:
        return m * DELTA, '_' * m, s2
    if m == 0:
        return n * DELTA, s1, '_' * n

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = min(dp[i-1][j-1] + ALPHA[(s1[i-1],s2[j-1])], dp[i-1][j] + DELTA, dp[i][j-1] + DELTA)

    
    """top-down"""
    matching1 = matching2 = ''
    i,j = n,m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + ALPHA[(s1[i-1],s2[j-1])]:
            # match!
            matching1 = s1[i-1] + matching1
            matching2 = s2[j-1] + matching2
            i -= 1
            j -= 1

        elif i > 0 and dp[i][j] == dp[i-1][j] + DELTA:
            # s1 gap
            matching1 = s1[i-1] + matching1
            matching2 = '_' + matching2
            i -= 1

        else :
            # s2 gap
            matching1 = '_' + matching1
            matching2 = s2[j-1] + matching2
            j -= 1


    return dp[n][m], matching1, matching2

""" The dp solution which uses only two rows and only does a bottom-up pass """
def min_cost(s1,s2):  
    n , m = len(s1), len(s2)
    dp = [] # m+1 columns
    
    # initialization
    for i in range(m+1):
        dp.append(i * DELTA)

    for i in range(1,n+1):
        new_dp = [math.inf] * (m+1) 
        new_dp[0] = i * DELTA
        for j in range(1,m+1):
            new_dp[j] = min(dp[j-1] + ALPHA[(s1[i-1],s2[j-1])], dp[j] + DELTA, new_dp[j-1] + DELTA)
        dp = new_dp

    return dp



# main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required=True,type=str,help="path to datapoints")
    parser.add_argument("--output",required=True,type=str,help="path to output files")

    args = parser.parse_args()

    os.makedirs(args.output,exist_ok=True)

    for file in os.listdir(args.input):
        if file.endswith('.txt'):
            print('Reading ',file)
            s1, s2 = generate(os.path.join(args.input,file))
            align_cost, matching_1, matching_2 = basic(s1,s2)
            with open(os.path.join(args.output,file.replace('in','output')), 'w') as f:
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n']
                f.writelines(data)
            print('Reading ',file, 'completed')


    # add time & memory assessment here
    # time_calc()
    # memory_calc()

    # for data in datapoints:
        # generate()
        #basic(args.input)

if __name__ == '__main__':
    main()
    #s1= 'ATC'
    #s2 = 'ATGGCT'

    #min_cost(s1,s2)
    #basic(s1,s2)