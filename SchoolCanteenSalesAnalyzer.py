foodcount = int(input("How many food items will you get? "))
met_target = 0
below_target = 0
total_sales = 0

for i in range(1, foodcount+1):
    sale = int(input(f"Enter sales for item {i} "))
    total_sales += sale

    if sale >= 500:
        met_target += 1
    elif sale < 500:
        below_target += 1

def calculate_average(total_sales, foodcount):
    average_sales = (total_sales/foodcount)
    return average_sales

average = calculate_average(total_sales, foodcount)

def canteen_analysis(average, met_target, below_target):
    print("CANTEEN SALES REPORT")
    print(f"Average sales = {average:.2f}| Meeting target: {met_target} | Below target: {below_target}")

calculate_average(total_sales, foodcount)
canteen_analysis(average, met_target, below_target)
