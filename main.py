x = input('>>>')

numbers = x.split(',')

numbers = list(map(int, numbers))

print(sum(numbers))

print(sum(numbers) / len(numbers))


print(numbers * 2)