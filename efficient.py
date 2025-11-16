"""implementation of the memory efficient solution"""

# import modules
import argparse
import math
from input_generate import generate
from basic import basic, min_cost

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
    n, m = len(s1), len(s2)


    def recur(start_1,end_1,start_2,end_2):
        if end_1 - start_1 + 1 <= base_len or end_2 - start_2 + 1 <= base_len:
            # solve this directly
            if end_2 < start_2:
                return basic(s1[start_1:end_1+1],'')
            return basic(s1[start_1:end_1+1],s2[start_2:end_2+1])
        
        # split s1 in half
        mid = (start_1+end_1)//2
        
        s1_left = s1[start_1:mid+1]
        s1_right_reversed = s1[end_1:mid:-1]

        dp = min_cost(s1_left,s2[start_2:end_2+1])
        dp_T = min_cost(s1_right_reversed,s2[end_2:start_2:-1]+s2[start_2])   
        n = len(dp)

        #print('left: ',s1[start_1:mid+1],'right: ',s1[end_1:mid:-1])
        #print('left: ',s2[start_2:end_2+1],'right: ',s2[end_2::-1])

        #print(dp)
        #print(dp_T)

        split_point = 0
        cost = math.inf
        
        for i in range(n):
            if dp[i] + dp_T[n-i-1] < cost:
                cost = dp[i] + dp_T[n-i-1]
                split_point = start_2 + i-1
        #print(split_point)
        
        cost_left, m_1_left, m_2_left = recur(start_1,mid,start_2,split_point)
        cost_right, m_1_right, m_2_right = recur(mid+1,end_1,split_point+1,end_2)


        return cost_left+cost_right, m_1_left+m_1_right, m_2_left+m_2_right
    
    

    total_c, m1, m2 = recur(0,n-1,0,m-1)
    #print(total_c)
    #print(m1)
    #print(m2)
            



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
    #main()
    s1= 'ATGGCGCGTTA'
    s2 = 'AACATGGCCGATT'

    efficient(s1,s2,2)
    #a,b,c = basic(s1,s2)
    #print(a)
    #print(b)
    #print(c)