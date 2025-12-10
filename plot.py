# import modules 
import os
import matplotlib.pyplot as plt

def plot_time_p():
    basic_dir = "../basic_p"
    efficient_dir = "../efficient_p"

    basic_vals = []
    efficient_vals = []

    for i in range(1, 16):
        filename = f"out{i}.txt"

        # read the time in basic
        basic_path = os.path.join(basic_dir, filename)
        with open(basic_path, "r") as f:
            lines = f.readlines()
            val_basic = float(lines[3].strip())  # 第4行，下标3
            basic_vals.append(val_basic)

        # read the time in efficient
        eff_path = os.path.join(efficient_dir, filename)
        with open(eff_path, "r") as f:
            lines = f.readlines()
            val_eff = float(lines[3].strip())   # 第4行，下标3
            efficient_vals.append(val_eff)

    x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

    plt.figure(figsize=(8, 5))

    plt.plot(x, basic_vals, marker="o", label="basic")
    plt.plot(x, efficient_vals, marker="s", label="efficient")

    plt.xlabel("Datapoint index (out1 ~ out15)")
    plt.ylabel("Value from line 4")
    plt.title("Basic vs Efficient time")
    plt.xticks(x)             
    plt.ylim(0, 1400)          
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    plt.savefig('time_p.png')

def plot_time_t():
    basic_dir = "../basic_t"
    efficient_dir = "../efficient_t"

    basic_vals = []
    efficient_vals = []

    for i in range(1, 16):
        filename = f"out{i}.txt"

        # read the time in basic
        basic_path = os.path.join(basic_dir, filename)
        with open(basic_path, "r") as f:
            lines = f.readlines()
            val_basic = float(lines[3].strip())  # 第4行，下标3
            basic_vals.append(val_basic)

        # read the time in efficient
        eff_path = os.path.join(efficient_dir, filename)
        with open(eff_path, "r") as f:
            lines = f.readlines()
            val_eff = float(lines[3].strip())   # 第4行，下标3
            efficient_vals.append(val_eff)

    x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

    plt.figure(figsize=(8, 5))

    plt.plot(x, basic_vals, marker="o", label="basic")
    plt.plot(x, efficient_vals, marker="s", label="efficient")

    plt.xlabel("Datapoint index (out1 ~ out15)")
    plt.ylabel("Value from line 4")
    plt.title("Basic vs Efficient time")
    plt.xticks(x)             
    plt.ylim(0, 22000)          
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    plt.savefig('time_t.png')

def plot_mem_p():
    basic_dir = "../basic_p"
    efficient_dir = "../efficient_p"

    basic_vals = []
    efficient_vals = []

    for i in range(1, 16):
        filename = f"out{i}.txt"

        # read the time in basic
        basic_path = os.path.join(basic_dir, filename)
        with open(basic_path, "r") as f:
            lines = f.readlines()
            val_basic = float(lines[4].strip())  # line 4
            basic_vals.append(val_basic)

        # read the time in efficient
        eff_path = os.path.join(efficient_dir, filename)
        with open(eff_path, "r") as f:
            lines = f.readlines()
            val_eff = float(lines[4].strip())   # line 4
            efficient_vals.append(val_eff)

    #x = list(range(1, 16))
    x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

    plt.figure(figsize=(8, 5))

    plt.plot(x, basic_vals, marker="o", label="basic")
    plt.plot(x, efficient_vals, marker="s", label="efficient")

    plt.xlabel("Datapoint index (out1 ~ out15)")
    plt.ylabel("Value from line 4")
    plt.title("Basic vs Efficient mem using psutil")
    plt.xticks(x)             
    plt.ylim(0, 30000)          
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    plt.savefig('mem_p.png')

def plot_mem_t():
    basic_dir = "../basic_t"
    efficient_dir = "../efficient_t"

    basic_vals = []
    efficient_vals = []

    for i in range(1, 16):
        filename = f"out{i}.txt"

        # read the time in basic
        basic_path = os.path.join(basic_dir, filename)
        with open(basic_path, "r") as f:
            lines = f.readlines()
            val_basic = float(lines[4].strip())  # line 4
            basic_vals.append(val_basic)

        # read the time in efficient
        eff_path = os.path.join(efficient_dir, filename)
        with open(eff_path, "r") as f:
            lines = f.readlines()
            val_eff = float(lines[4].strip())   # line 4
            efficient_vals.append(val_eff)

    #x = list(range(1, 16))
    x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

    plt.figure(figsize=(8, 5))

    plt.plot(x, basic_vals, marker="o", label="basic")
    plt.plot(x, efficient_vals, marker="s", label="efficient")

    plt.xlabel("Datapoint index (out1 ~ out15)")
    plt.ylabel("Value from line 4")
    plt.title("Basic vs Efficient mem using tracemalloc")
    plt.xticks(x)             
    plt.ylim(0, 160000)          
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    plt.savefig('mem_t.png')

def main():
    plot_time_p()
    plot_mem_p()
    #plot_mem_t()

if __name__ == '__main__':
    main()