print("------------------------")
print("STOCK PORTFOLIO TRACKER ")
print("------------------------")
#STOCK PORTFOLIO TRACKER

stocks={'APPL':180,'TSLA':250,'TATA':300,'BENZ':400}
l={}
n=int(input("enter how many types of stocks you had purchased "))
i=0
while(i<n):
    s=input("enter the stocks(apple:APPL,tesla:TSLA,tata:TATA,benz:BENZ) ")
    if(s=='apple'):
        s='APPL'
    elif(s=='tesla'):
        s='tsla'
    if(s.upper() in stocks):
        l[s.upper()]=int(input("enter the quantity of it "))
        i=i+1
    else:
        print("enterd invalid stock object! enter again ")
        i=i-1

def calculate_investment(l,stocks):
    price=0
    for i in l:
        price=price+(l[i]*stocks[i])
    return price
total=calculate_investment(l,stocks)
print("total investment is ",total,"/-")
with open("stock.txt",'w') as file:
    file.write("your stock investment is ")
    file.write(str(total))
file.close()