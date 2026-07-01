cp = "1499"  # Correct PIN
ta = 3       # Total Attempts Left

while ta > 0:
    ep = input("Please enter your 4-digit pin: ")
    
    if ep == cp:
        print("Correct pin!!")
        break
    else:
        ta -= 1
        if ta > 0:
            print(f"Incorrect pin. You have {ta} attempts left.")
        else:
            print("Account Blocked.")