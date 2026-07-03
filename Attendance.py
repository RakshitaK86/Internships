present=int(input("Enter your total number of days present:"))
Total_Working_days=180
present_percent=(present/Total_Working_days)*100
if present_percent>=95:
    print("Your attendance is on safer side!!")
else:
    print("Your attendance is in losss!!")