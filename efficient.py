"""implementation of the memory efficient solution"""

# import modules
import os
import argparse
import time
import psutil
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


def process_memory():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss   # bytes
    return mem / 1024       # KB


# D&C algorithm
def efficient(s1,s2,base_len):
    mem_start = process_memory()
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

    mem_end= process_memory()
    return total_c, m1, m2, mem_end-mem_start
            

# main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required=True,type=str,help="path to datapoint file")
    parser.add_argument("--output",required=True,type=str,help="path to output file")

    args = parser.parse_args()

    directory = os.path.dirname(args.output)
    os.makedirs(directory,exist_ok=True)

    if args.input.endswith('.txt'):
        print('Reading ',args.input)
        s1, s2 = generate(args.input)
        start_time = time.time()
        mem_start = process_memory()
        align_cost, matching_1, matching_2, mem = efficient(s1,s2,2)  # alter this last arg for performance testing
        mem_end = process_memory()
        end_time = time.time()
        time_taken_ms = (end_time - start_time) * 1000
        print('Reading complete!')

        with open(args.output, 'w') as f:
            print('Writing to:',args.output)
            data = [str(align_cost),'\n',
                    matching_1,'\n',
                    matching_2,'\n',
                    str(time_taken_ms),'\n',
                    str(mem),'\n',
                    str(mem_end-mem_start),'\n']
            f.writelines(data)
        print('memory usage: ', mem, 'outside mem: ',mem_end-mem_start)
        print('Writing complete!')


if __name__ == '__main__':
    main()
    #path = '../CSCI570_Project_Minimum_Jul_14/Datapoints/in1.txt'
    #s1, s2 = generate(path)
    #start = process_memory()
    #align_cost, matching_1, matching_2, inside_men = efficient(s1,s2,2)  # alter this last arg for performance testing
    #end = process_memory()
    #print(start,end,end-start,inside_men)
    #test_mem()

