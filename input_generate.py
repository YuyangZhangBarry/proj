"""The input generator"""

def generate(input_path):
    # code goes here
    assert input_path.endswith('.txt')

    s1 = s2 = ''

    with open(input_path,'r') as f:
        lines = [line.strip() for line in f if line.strip() != ""]
        n = len(lines)

        s1 = lines[0]
        i = 1
        while lines[i].isdecimal():
            index = int(lines[i])
            s1 = s1[:index+1] + s1 + s1[index+1:]
            i += 1

        s2 = lines[i]
        i += 1
        while i < n and lines[i].isdecimal():
            index = int(lines[i])
            s2 = s2[:index+1] + s2 + s2[index+1:]
            i += 1
    
    return s1, s2
        

        
