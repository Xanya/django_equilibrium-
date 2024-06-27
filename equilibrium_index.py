def get_input_as_integer_list(prompt="Enter integers separated by space: "):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            # Split input by space and convert to list of integers
            try:
                input_list = [int(item) for item in user_input.split()]
                return input_list
            except ValueError:
                print("Error: Input must be integers separated by space. Please try again.")
        else:
            print("Input cannot be empty. Please try again.")

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]
    
    # returns -1 if there's no index
    return -1

if __name__ == "__main__":
    arr = get_input_as_integer_list()
    result = find_equilibrium_index(arr)
    if result == -1:
        print("There's no equilibrium index in this array.")
    else:
        print("Equilibrium Index is:", result)