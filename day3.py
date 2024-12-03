import re

def calculate_result(input_file: str) -> int:
    result = 0
    pattern = r"mul\((\d+),(\d+)\)"
    
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            matches = re.findall(pattern, line)
            for a, b in matches:
                result += int(a) * int(b)
                
    return result

if __name__ == "__main__":
    is_test = False
    input_file = './data/input-sample.txt' if is_test else './data/input.txt'
    result = calculate_result(input_file)
    print(result)
