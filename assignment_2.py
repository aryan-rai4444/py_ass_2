def get_integer_list():#first function for getting input from user
    """Function to get a list of integers from user input."""
    while True:
        try:
            num_values = int(input("How many values would you like to enter? "))
            if num_values < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    integer_list = []
    
    for i in range(num_values):
        while True:
            try:
                value = int(input(f"Enter value {i + 1}: "))
                integer_list.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    return integer_list

def compute_statistics(numbers):
    #second function for computing average minimum,sum and cumulative 
    
    if not numbers:
        return None, None, None, None

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    minimum = min(numbers)
    cumulative_sum = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative_sum.append(current_sum)
    
    return average, minimum, total_sum, cumulative_sum

if __name__ == "__main__":
    user_list = get_integer_list()
    avg, min_val, total_sum, cum_sum = compute_statistics(user_list)
    
    print("Statistics of the entered list:")
    print(f"Average: {avg}")
    print(f"Minimum: {min_val}")
    print(f"Sum: {total_sum}")
    print(f"Cumulative Sum: {cum_sum}")
