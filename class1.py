class showroom:
    name=""
    mobile=""
    cost=0
    dis=0
    amt=0
c1=showroom()
c2=showroom()
c1.name="Madav"
c1.mobile="iphone"
print("name:",c1.name)
print("mobile:",c1.mobile)
c1.cost=int(input("enter cost:"))
if c1.cost<=10000:
    c1.dis=c1.cost*5/100
    print("discount:",c1.dis)
if c1.cost>10000 and c1.cost<=20000:
    c1.dis=c1.cost*10/100
    print("discount:",c1.dis)
if c1.cost>20000 and c1.cost<=35000:
    c1.dis=c1.cost*15/100
    print("discount:",c1.dis)
if c1.cost>35000:
    c1.dis=c1.cost*20/100
    print("discount:",c1.dis)
c1.amt=c1.cost-c1.dis
print("Total amount:",c1.amt)
c2.name="Madav"
c2.mobile="iphone"
print("name",c2.name)
print("mobile",c2.mobile)
c2.cost=int(input("enter cost:"))
if c2.cost<=10000:
    c2.dis=c2.cost*5/100
    print("discount:",c2.dis)
if c2.cost>10000 and c2.cost<=20000:
    c2.dis=c2.cost*10/100
    print("discount:",c2.dis)
if c2.cost>20000 and c2.cost<=35000:
    c2.dis=c1.cost*15/100
    print("discount:",c2.dis)
if c2.cost>35000:
    c2.dis=c1.cost*20/100
    print("discount:",c2.dis)
c2.amt=c2.cost-c2.dis
print("Total amount:",c2.amt)   
