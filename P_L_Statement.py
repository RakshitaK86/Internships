print("----------Profit Loss Statement-----------")
Income=float(input("Enter your income:"))
Expenditure=float(input("Enter your Expenditure:"))
print("----------------------------")
Profit_loss=Income - Expenditure
if Profit_loss > Expenditure:
    print("Sales are in Profit!!!!!")
    print(f"Total profit made is:{Profit_loss}")
    
elif Profit_loss < Income:
    print("Sales are in Loss!!")
    print(f"Total loss made is:{Profit_loss}")
else:
    print("Sales are neither in Profit nor in Loss")
print("\n----------------------------------------")    

