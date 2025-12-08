import os 
from input_generate import generate
from efficient import efficient
from basic import basic,process_memory
INPUT = "../CSCI570_Project_Minimum_Jul_14/Datapoints/in13.txt"
OUTPUT = "../mem/efficient/10/out13.txt"
MODE = 'basic'

def main():
    directory = os.path.dirname(OUTPUT)
    os.makedirs(directory,exist_ok=True)
    
    s1, s2 = generate(INPUT)
    mem = 0
    if MODE == 'efficient':
        _,_,_, mem = efficient(s1,s2,10)  # alter this last arg for performance testing
        if mem < 0 :
            return
    
    else:
        mem_s = process_memory()
        align_cost, matching_1, matching_2 = basic(s1,s2)
        mem_e = process_memory()
        mem = mem_e - mem_s
    
    with open(OUTPUT,'w+') as f:
        line = f.readline()
        line.strip()
        if line == '':
            line = '0.0'
        new_mem = float(line) + mem
        data = [str(new_mem),'\n']
        f.writelines(data)
        


if __name__ == '__main__':
    main()