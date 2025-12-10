# Project description
This is the repository for the final project of CSCI-570 Analysis of Algorithms. The organization of the files is a little different than the requirements in the pdf, so please read this carefully before jumping into running. 

## Run the code
1. Change the input and output path in basic.sh and efficient.sh
2. Run `bash basic.sh` and `bash efficient.sh`
3. Change the output path in plot.py and run `python plot.py`

## Basic files description
1. input_generate.py : takes datapoint file path as input and returns the complete strings s1 and s2.
2. basic.py : the implementation of the basic **Dynamic Programming** solution.
3. efficient.py : the implementation of the memory-efficient **DP & DC** solution.
4. basic.sh: script to run the basic solution.
5. efficient.sh: script to run the efficient solution, takes an additional argument *baselength*, which specifies the base string length. When the input string length is less than or equal to *baselength*, stop dividing and solve the subproblem directly using **basic.py**. Default is 10.

## Advanced comparison
After noticing some outliers in the memory usage graph, we improved our code and provide an advanced option.

For both `basic.py` and `efficient.py`, we add an additional memory measurement method by utilizing the "tracemalloc" library. By specifying the measuring mode to be either `psutil`, which is the default value, or `trace`, we draw yet another comparison between two measurement methods. Here's how to use it.

1. Change the input and output path in basic_t.sh and efficient_t.sh
2. (Optional) Change the input and output path in basic_p.sh and efficient_p.sh (they are exactly the same as basic.sh and efficient.sh, since mode'p' is the default setting)
3. Run `bash basic_t.sh` and `bash efficient_t.sh`
4. Uncomment `plot_mem_t()` in the main function of `plot.py` and run `python plot.py`
