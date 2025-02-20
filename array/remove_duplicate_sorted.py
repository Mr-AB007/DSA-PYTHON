
def remove_duplicates(lst: list) -> int:
    if not lst:
        return 0  # Return 0 for an empty list

    k = 0  # Pointer for unique elements

    for i in range(1, len(lst)):
        if lst[i] != lst[k]:  # If current element is different from the last unique element
            k += 1
            lst[k] = lst[i]  # Move the unique element to the correct position

    return k + 1  # Unique count


def remove_duplicates_set(lst: list) -> int:
    unique_values = sorted(set(lst))  # Remove duplicates and sort again //set conatain uniques aonlt
    lst[:len(unique_values)] = unique_values  #len(unique_values) = 6, so lst[:6] = [1, 2, 3, 4, 5, 6] # Modify in-place
    return len(unique_values)

if __name__ == "__main__":
    # Driver code to test the function
    nums = [1, 1, 2, 3, 3, 4]
    unique_count = remove_duplicates(nums)

    print("Number of unique elements:", unique_count)
    print("Modified list:", nums[:unique_count])  # Print only the unique elements
