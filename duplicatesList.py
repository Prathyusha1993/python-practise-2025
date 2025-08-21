
# find duplicates in list:
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates([1,2,3,2,4,5,1]))

# remove duplicates while preserving order:
def remove_duplicates(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

print(remove_duplicates([1,2,3,2,1,4, 5, 6, 3]))