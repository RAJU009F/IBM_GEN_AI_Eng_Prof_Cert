def mean(numbers):
    """
    This function returns the mean of the given list of numbers.
    The mean is calculated as the sum of all numbers divided by the count of numbers.
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    This function returns the median of the given list of numbers.
    The median is the middle value when the numbers are sorted.
    If there is an even number of observations, it returns the average of the two middle numbers.
    """    
    numbers.sort()

    if len(numbers) == 0:
        median1 = numbers[len(numbers)//2]
        median2 = numbers(len(numbers)//2 -1)
        mymedian = median1 + median2
    else:
        mymedian = numbers[len(numbers)//2]
    return mymedian        
