# Monthly Revenue Report 

monthly_revenue = [75000,50000,65500,80000,90000,100000,120000,110000,95000,105000,115000,130000]
print("Monthly Revenue Report:", monthly_revenue)

first_quarter_revenue = monthly_revenue[0:3]
print("First Quarter Revenue:", first_quarter_revenue)

last_quarter_revenue = monthly_revenue[9:12]
print("Last Quarter Revenue:", last_quarter_revenue)

peak_season_revenue = first_quarter_revenue + last_quarter_revenue
print("Peak Season Revenue:", peak_season_revenue)