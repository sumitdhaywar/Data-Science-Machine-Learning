product_name=input("enter the product name")
selling_price=int(input("enter the selling price"))
quantity=int(input("enter the quantity"))
total_revinue=selling_price*quantity
purchase_price=int(input("enter the purchase price"))
total_purchase_cost=purchase_price*quantity
dif=total_revinue-total_purchase_cost
if dif<0:
    print("total loss over the product_name is ",dif)
elif dif>0:
    print ("total profit over product_name is",dif)
else:
    print("no profit ,no loss")