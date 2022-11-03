print("Hello World!")
"""
Iterating over lists.
"""
def print_items(alist) :
    """
Iterate over alist and print all items.
    """
    for item in alist:
        print(item)



numbers = list(range(5,82,3))
strings = ["python", "is", "fun", "!"]


print("Iterate over lists and print items")
print("")

print_items(numbers)
print_items(strings)

def count_items(alist):
    """
    Count number of items in alist
    """
    count = 0
    for item in alist:
        count = count + 1
    return count

print("")
print("Iterate over lists and process them")
print("")

print(count_items(numbers))
print(count_items(strings))


def count_odd_items(numlist):
    """
    Count number of odd numbers in numlist.
    """
    count = 0
    for num in numlist:
        if num % 2 == 1:
            count += 1
    return count


print(count_odd_items(numbers))

years = list(range(20 , 0, 5))
print(years)