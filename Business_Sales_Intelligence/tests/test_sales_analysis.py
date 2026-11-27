from src.sales_analysis import classify_sales, calculate_sales_summary

sales = [
    {"customer": "C101", "amount": 2500},
    {"customer": "C102", "amount": 800},
    {"customer": "C103", "amount": 3200},
    {"customer": "C104", "amount": 1200}
]

print("Sales Classification:")
print(classify_sales(sales))

print("\nSales Summary:")
print(calculate_sales_summary(sales))
print("\nEmpty Data Test:")
print(calculate_sales_summary([]))

print("\nInvalid Transactions Test:")
test_sales = [
    {"customer": "C101", "amount": 1000},
    None,
    {"customer": "C102", "amount": 0},
    {"customer": "C103", "amount": -500},
    {"customer": "C104", "amount": 2000}
]

print(calculate_sales_summary(test_sales))