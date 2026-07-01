a = int(input("Enter a number: "))
total_ts = 0

for i in range(1, a + 1):
    total_ts += i

print(f"The sum of the first {a} natural numbers is: {total_ts}")