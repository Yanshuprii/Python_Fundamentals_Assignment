cp=int(input("enter your cost price"))
sp=int(input("enter your selling price"))
d=int(input("enter disocunt percentage"))
def profit_loss(*args,**kwargs):
  selling_price=args[1]
  cost_price=args[0]
  discount=kwargs["dis"]
  if(selling_price>cost_price):
    print("profit")
  elif(selling_price<cost_price):
    print("loss")
  else:
    print("no profit no loss")

profit_loss(cp,sp,dis=d)
