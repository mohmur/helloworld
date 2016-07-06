balance = int(input("Enter the outstanding balance:"))
ann_int = float(0.18)
mon_int = float(0.18/12)
min_mon_pay_rate = float(0.02)
min_pay=0.0
mon_unpaid=0.0
tot_paid=0.0
for i in range( 1 , 13 ):
    min_pay = balance * min_mon_pay_rate
    mon_unpaid = balance - min_pay
    balance = mon_unpaid + (mon_int * mon_unpaid )
    print("Month:")
    print(i)
    print("Minimum Monthly payment : ")
    print(float(int(min_pay*100)/100))
    print("Remaining Balance : " )
    print(float(int(balance*100)/100))
    tot_paid = tot_paid + min_pay


print("Total Amount Paid till the end of the year : ")
print( float(int(tot_paid*100)/100) )
print("Remaining Balance : ")
print(float(int(balance*100)/100))

    

