from typing import List

def calculate_result(input_file: str) -> int:
    left_array: List[int] = []
    right_array: List[int] = []

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            left_array.append(int(parts[0]))
            right_array.append(int(parts[-1]))

    left_array.sort()
    right_array.sort()

    # calculeta sum of absolute diff
    return sum(abs(left - right) for left, right in zip(left_array, right_array))


if __name__ == "__main__":
    is_test = False
    input_file = './data/input-sample.txt' if is_test else './data/input.txt'
    result = calculate_result(input_file)
    print(result)
