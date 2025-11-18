"""implementation of the memory efficient solution"""

# import modules
import os
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

# D&C algorithm
def efficient(s1,s2,base_len):
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

        """ Finding the optimal split point """
        dp = min_cost(s1_left,s2[start_2:end_2+1])
        dp_T = min_cost(s1_right_reversed,s2[end_2:start_2:-1]+s2[start_2])   
        n = len(dp)

        split_point = 0
        cost = math.inf
        
        for i in range(n):
            if dp[i] + dp_T[n-i-1] < cost:
                cost = dp[i] + dp_T[n-i-1]
                split_point = start_2 + i-1
        

        # solve the problem recursively 
        cost_left, m_1_left, m_2_left = recur(start_1,mid,start_2,split_point)
        cost_right, m_1_right, m_2_right = recur(mid+1,end_1,split_point+1,end_2)


        return cost_left+cost_right, m_1_left+m_1_right, m_2_left+m_2_right
    
    

    total_c, m1, m2 = recur(0,n-1,0,m-1)    
    return total_c, m1, m2
            



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
            align_cost, matching_1, matching_2 = efficient(s1,s2,2)  # alter this last arg for performance testing
            with open(os.path.join(args.output,file.replace('in','output')), 'w') as f:
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n']
                f.writelines(data)
            print('Reading ',file, 'completed')

    # add time & memory assessment here
    # time_calc()
    # memory_calc()

    #efficient(args.input)

if __name__ == '__main__':
    main()
    #s1= 'ATGGCGCGTTA'
    #s2 = 'AACATGGCCGATT'

    #efficient(s1,s2,2)
    #a,b,c = basic(s1,s2)
    #print(a)
    #print(b)
    #print(c)