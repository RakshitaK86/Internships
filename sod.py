def sod(a):
    ts = 0
    a = abs(a)
    
    while a > 0:
        ld = a % 10
        ts += ld
        a = a // 10
        
    return ts

# Main Program Execution
num = int(input("Enter the number for finding digit sum: "))
print(f"The sum of digits of {num} is {sod(num)}")