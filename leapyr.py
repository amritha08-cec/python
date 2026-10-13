import datetime
year1=datetime.date.today().year
print("current year:",year1)

year2=int(input("Enter the last year"))
for i in range (year1,year2):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
