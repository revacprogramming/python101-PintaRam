class Menu(dict):
  """fill in class definition here"""
  def __init__(self):
    pass
  def dict(self,item,rate):
    self[item]=rate

class Order():
  """fill in class definition here"""
  def __init__(self,menu):
   self.menu=menu
   self.orders=dict()
  def __setitem__(self,item,qty):
    self.orders[item]=qty
    

class Bill:
  """fill in class definition here"""
  def __init__(self,item,order):
    self.bill=sum(v*self.item[k] for k,v in order.orders.items())
  def __str__(self):
    return f"{self.bill} rupees"

m = Menu()
m['pongal']=30
m["idly"] = 10
m["vada"] = 20
m['dosa']=25
m['lemon Rice']=30
m['Tea']=8
print('Hi welcome to Hotel')
choice=input("Do u like to see the Menu y/n:")
if choice =='y':
  print("We have the following Items")
  print('Menu'.center(20,'-'))
  i=0
  for k,v in m.items():
   i+=1
   print(str(i)+'.'+k,'->',v)
else:
   exit()
print("Accepting your Order".center(50,'>'))

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2
except KeyError as e:
    print(e)
for k,v in o.item():
 print(f"U selected {v}->{k} ")



