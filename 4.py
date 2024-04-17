s = [1, 3, 5, 3, 5, 2, 6]
duplicates = []

for x in s:
    if s.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

if len(duplicates) > 0:
    print("Повторяющиеся элементы в списке:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("В списке нет повторяющихся элементов.")
