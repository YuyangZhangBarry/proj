
def generate_string(base, insertions):
    current = base
    
    for index in insertions:
        current = current[:index + 1] + current + current[index + 1:]
    
    return current


def parse_file(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None
    
    if len(lines) < 2:
        print("Error: Input file must have at least 2 lines for base strings.")
        return None, None
    
    s0 = lines[0]
    j = 1
    s_insertions = []

    while j < len(lines):
        try:
            index = int(lines[j])
            s_insertions.append(index)
            j += 1
        except ValueError:
            break
    
    t0 = lines[j]
    j += 1
    
    t_insertions = []
    while j < len(lines):
        try:
            index = int(lines[j])
            t_insertions.append(index)
            j += 1
        except ValueError:
            print(f"Warning: Unexpected non-numeric line at position {j}: {lines[j]}")
            break
    
    X = generate_string(s0, s_insertions)
    Y = generate_string(t0, t_insertions)
    
    return X, Y


if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    X, Y = parse_file(input_file)
    print(X)
    print(Y)