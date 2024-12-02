def calculate_safe_reports(input_file: str) -> int:
    
    def is_safe_report(report):
        """Check if a single report is safe based on the two conditions."""
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        
        # Check if all differences are within the range of 1 to 3 (absolute value)
        if not all(1 <= abs(diff) <= 3 for diff in differences):
            return False
        
        # Check if the report is strictly increasing or decreasing
        if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
            return True
        
        return False

    try:
        with open(input_file, 'r') as file:
            reports = [list(map(int, line.strip().split())) for line in file if line.strip()]
        
        # Count the number of safe reports
        safe_reports = sum(1 for report in reports if is_safe_report(report))
        
        return f"Number of safe reports: {safe_reports}"

    except FileNotFoundError:
        return f"Error: The file '{input_file}' was not found."
        

    except ValueError:
        return f"Error: The file '{input_file}' contains invalid data."


if __name__ == "__main__":
    is_test = False
    input_file = './data/input-sample.txt' if is_test else './data/input.txt'
    print(calculate_safe_reports(input_file))
