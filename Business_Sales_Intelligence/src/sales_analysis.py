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
def clean_sales_data(sales_data):
    clean_data=[]
    for i in sales_data:
        if i != None:
            if i["amount"]>0:
                clean_data.append(i)
    return clean_data
    
def calculate_total_sales(sales_data):
    sales=clean_sales_data(sales_data)
    total=0
    for i in sales:
        total=total+i["amount"]
    return total
def count_transactions(sales_data):
    sales=clean_sales_data(sales_data)
    tran=0
    for i in sales:
        tran=tran+1
    return tran
def calculate_average_sale(sales_data):
    sales=clean_sales_data(sales_data)
    total=calculate_total_sales(sales)
    transaction =count_transactions(sales)
    if transaction ==0:
        return "no valid transaction"
    average=total/transaction
    return average
def calculate_sales_summary(sales_data):
    sales=clean_sales_data(sales_data)
    total=calculate_total_sales(sales)
    transaction =count_transactions(sales)
    average=calculate_average_sale(sales)
    report={"total_sales":total,"transaction":transaction,"average_sales":average}
    return report
sales = [
    {"customer": "C101", "amount": 2500},
    {"customer": "C102", "amount": 800},
    {"customer": "C103", "amount": 3200},
    {"customer": "C104", "amount": 1200}
]
