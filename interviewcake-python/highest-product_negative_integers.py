def highest_product(arr):
    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])
    highest_of_two = highest * lowest
    lowest_of_two = highest * lowest
    max_product = highest_of_two * arr[2]

    for elem in arr:
        max_product = max( max_product, elem * highest_of_two, elem * lowest_of_two )
        highest_of_two = max( highest_of_two, elem * highest, elem * lowest )
        lowest_of_two = min( lowest_of_two, elem * highest, elem * lowest )
        highest = max( highest, elem)
        lowest = min( lowest, elem)
    return max_product

list_of_numbers = [1,3,9,6,9,-99,-1]
result = highest_product(list_of_numbers)
print result
