def length(lst):
    """
    Returns the number of elements in the list.
    :param lst: List of elements.
    :return: Integer count of elements.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of a list.
    :param lst: List of numeric elements.
    :return: Arithmetic mean as a float.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the max and min values in the list.
    :param lst: List of numeric elements.
    :return: Difference between max and min as a float or integer.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    return max(lst) - min(lst)

def median(lst):
    """
    Calculates the median of a list.
    :param lst: List of numeric elements.
    :return: Median as a float or integer.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    """
    Calculates the standard deviation of a list.
    :param lst: List of numeric elements.
    :return: Standard deviation as a float.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def list_statistics(lst):
    """
    Creates a dictionary with statistics of a list.
    :param lst: List of numeric elements.
    :return: Dictionary containing length, mean, range, median, and standard deviation.
    """
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst),
    }

# Example Usage
numbers = [1, 2, 3, 4, 5]
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))
print("Standard Deviation:", standard_deviation(numbers))
print("Statistics:", list_statistics(numbers))

# Test Cases
print("Empty List Test:")
try:
    print(mean([]))
except ValueError as e:
    print(e)

print("Single Element Test:", list_statistics([42]))
print("Negative Numbers Test:", list_statistics([-5, -3, -10, 0, 4]))
print("Floating Point Test:", list_statistics([1.5, 2.3, 3.7, 4.1, 5.0]))
