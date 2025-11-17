"""implementation of the memory efficient solution"""

# import modules
import argparse
from input_generate import generate
from basic import basic
import math

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
def efficient(s1,s2, size=2):
    l1, l2 = len(s1), len(s2)

    if l1 <= size or l2 <= 1:
        return basic(s1, s2)

    dp1 = [[0] * 2 for _ in range(l2 + 1)]
    dp2 = [[0] * 2 for _ in range(l2 + 1)]
    s1_left = s1[:(l1 // 2)]
    s1_right = s1[(l1 // 2):]
    s1_right_R = s1_right[::-1]
    s2_R = s2[::-1]

    # dp tables initialization
    for j in range(l2 + 1):
        dp1[j][0] = j * DELTA
        dp2[j][0] = j * DELTA
    
    # filling up dp tables
    for i in range(1, len(s1_left) + 1):
        idx = i % 2
        dp1[0][idx] = i * DELTA
        dp2[0][idx] = i * DELTA
        for j in range(1, l2 + 1):
            if idx == 1:
                dp1[j][idx] = min(dp1[j - 1][idx - 1] + ALPHA[(s1_left[i - 1], s2[j - 1])],
                                  dp1[j][idx - 1] + DELTA,
                                  dp1[j - 1][idx] + DELTA)
                dp2[j][idx] = min(dp2[j - 1][idx - 1] + ALPHA[(s1_right_R[i - 1], s2_R[j - 1])],
                                  dp2[j][idx - 1] + DELTA,
                                  dp2[j - 1][idx] + DELTA)
            else:
                dp1[j][idx] = min(dp1[j - 1][idx + 1] + ALPHA[(s1_left[i - 1], s2[j - 1])],
                                  dp1[j][idx + 1] + DELTA,
                                  dp1[j - 1][idx] + DELTA)
                dp2[j][idx] = min(dp2[j - 1][idx + 1] + ALPHA[(s1_right_R[i - 1], s2_R[j - 1])],
                                  dp2[j][idx + 1] + DELTA,
                                  dp2[j - 1][idx] + DELTA)
    if l1 % 2 != 0:
        idx = len(s1_right_R) % 2
        for j in range(l2 + 1):
            if idx == 1:
                dp2[j][idx] = min(dp2[j - 1][idx - 1] + ALPHA[(s1_right_R[-2], s2_R[j - 1])],
                                  dp2[j][idx - 1] + DELTA,
                                  dp2[j - 1][idx] + DELTA)
            else:
                dp2[j][idx] = min(dp2[j - 1][idx + 1] + ALPHA[(s1_right_R[-2], s2_R[j - 1])],
                                  dp2[j][idx + 1] + DELTA,
                                  dp2[j - 1][idx] + DELTA)
            
    # finding split point
    split = 0
    min_cost = math.inf
    for j in range(l2 + 1):
        c = dp1[j][len(s1_left) % 2] + dp2[l2 - j][len(s1_right_R) % 2]
        if c < min_cost:
            min_cost = c
            split = j

    cost_l, matching1_l, matching2_l = efficient(s1_left, s2[:split + 1], size)
    cost_r, matching1_r, matching2_r = efficient(s1_right, s2[split + 1:], size)

    return cost_l + cost_r, matching1_l + matching1_r, matching2_l + matching2_r


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
    s1= 'ACACTGACTACTGACTGGTGACTACTGACTGG'
    s2 = 'TATTATACGCTATTATACGCGACGCGGACGCG'

    cost, m1, m2 = efficient(s1,s2)
    print(cost)
    print(m1)
    print(m2)