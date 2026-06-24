actual_cost=float(input("Enter the actual cost"))
selling_cost=float(input("Enter the selling cost"))
if selling_cost>actual_cost:
    profit= selling_cost-actual_cost
    print ("The profit gained is", profit)
else:
    loss= actual_cost-selling_cost
    print ("The loss is", loss)