"""implementation of the memory efficient solution"""

# import modules
import os
import argparse
import time
import psutil,tracemalloc
import math
from input_generate import parse_file as generate
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


""" D&C algorithm """
# memory measure using psutil
def efficient_p(s1,s2,base_len): 
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

# memory mesure using tracemalloc
def efficient_t(s1,s2,base_len):
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
    parser.add_argument("--input",required=True,type=str,help="path to datapoint file")
    parser.add_argument("--output",required=True,type=str,help="path to output file")
    parser.add_argument("--baselength",required=False,type=int,default=10,help="base length which determines when wo solve the problem using dp directly")
    parser.add_argument("--mode",required=False,default="psutil",type=str,help="memory measuring mode")
    

    args = parser.parse_args()

    directory = os.path.dirname(args.output)
    os.makedirs(directory,exist_ok=True)

    if args.mode == "psutil":
        if args.input.endswith('.txt'):
            print('Reading ',args.input)
            s1, s2 = generate(args.input)
            #print(len(s1),len(s2))
            start_time = time.time()
            #tracemalloc.start()
            align_cost, matching_1, matching_2,mem = efficient_p(s1,s2,args.base_length)  # alter this last arg for performance testing
            #_, mem = tracemalloc.get_traced_memory()
            #tracemalloc.stop()
            #mem = mem / 1024
            end_time = time.time()
            time_taken_ms = (end_time - start_time) * 1000
            print('Reading complete!')

            with open(args.output, 'w') as f:
                print('Writing to:',args.output)
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n',
                        str(time_taken_ms),'\n',
                        str(mem),'\n']
                f.writelines(data)
            print('memory usage: ', mem)
            print('Writing complete!')
    
    else:
        if args.input.endswith('.txt'):
            print('Reading ',args.input)
            s1, s2 = generate(args.input)
            #print(len(s1),len(s2))
            start_time = time.time()
            tracemalloc.start()
            align_cost, matching_1, matching_2 = efficient_t(s1,s2,args.base_length)  # alter this last arg for performance testing
            _, mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            mem = mem / 1024
            end_time = time.time()
            time_taken_ms = (end_time - start_time) * 1000
            print('Reading complete!')

            with open(args.output, 'w') as f:
                print('Writing to:',args.output)
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n',
                        str(time_taken_ms),'\n',
                        str(mem),'\n']
                f.writelines(data)
            print('memory usage: ', mem)
            print('Writing complete!')      


if __name__ == '__main__':
    main()


