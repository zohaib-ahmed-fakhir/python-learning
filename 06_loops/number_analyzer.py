n = int(input("Enter a number: "))

total = 0
even_count = 0
odd_count = 0

even_numbers = ""
odd_numbers = ""

for i in range(1, n + 1):

    total = total + i

    if i % 2 == 0:
        even_numbers = even_numbers + str(i) + " "
        even_count = even_count + 1
    else:
        odd_numbers = odd_numbers + str(i) + " "
        odd_count = odd_count + 1

print("Total:", total)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
