def classify_sales(sales):
    high=0
    low=0
    equal=0
    for i in sales:
        if i["amount"]<1500:
            low=low+1
        elif i["amount"]>1500:
            high =high+1
        else :
            equal=equal+1
    return {"high":high,"low":low,"equal":equal}
sales = [
    {"customer": "C101", "amount": 2500},
    {"customer": "C102", "amount": 800},
    {"customer": "C103", "amount": 3200},
    {"customer": "C104", "amount": 1200}
]
print(classify_sales(sales))