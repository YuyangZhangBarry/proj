"""implementation of the basic DP solution"""

# import modules
import os
import argparse
import time
import psutil, tracemalloc
import math
from input_generate import parse_file as generate

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
    parser.add_argument("--input",required=True,type=str,help="path to datapoint file")
    parser.add_argument("--output",required=True,type=str,help="path to output files")
    parser.add_argument("--mode",required=False,default="psutil",type=str,help="memory measuring mode")
    

    args = parser.parse_args()
    directory = os.path.dirname(args.output)
    os.makedirs(directory,exist_ok=True)

    if args.mode == "psutil":
        if args.input.endswith('.txt'):
            print('Reading ',args.input)
            s1, s2 = generate(args.input)
            print(len(s1),len(s2))
            start_time = time.time()
            mem_s = process_memory()
            #tracemalloc.start()
            align_cost, matching_1, matching_2 = basic(s1,s2)
            mem_e = process_memory()
            #_, mem = tracemalloc.get_traced_memory()
            #tracemalloc.stop()
            #mem = mem/1024
            end_time = time.time()
            time_taken_ms = (end_time - start_time) * 1000
            mem = mem_e - mem_s
            print('mem: ',mem)
            print('Reading complete!')

            with open(args.output, 'w') as f:
                print('Writing to:',args.output)
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n',
                        str(time_taken_ms),'\n',
                        str(mem),'\n']
                f.writelines(data)
            print('Writing complete!')
            
    else:
        if args.input.endswith('.txt'):
            print('Reading ',args.input)
            s1, s2 = generate(args.input)
            print(len(s1),len(s2))
            start_time = time.time()
            #mem_s = process_memory()
            tracemalloc.start()
            align_cost, matching_1, matching_2 = basic(s1,s2)
            #mem_e = process_memory()
            _, mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            mem = mem/1024
            end_time = time.time()
            time_taken_ms = (end_time - start_time) * 1000
            #mem = mem_e - mem_s
            print('mem: ',mem)
            print('Reading complete!')

            with open(args.output, 'w') as f:
                print('Writing to:',args.output)
                data = [str(align_cost),'\n',
                        matching_1,'\n',
                        matching_2,'\n',
                        str(time_taken_ms),'\n',
                        str(mem),'\n']
                f.writelines(data)
            print('Writing complete!')

if __name__ == '__main__':
    main()
