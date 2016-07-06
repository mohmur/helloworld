balance = int(input("Enter the outstanding balance:"))
ann_int = float(0.18)
mon_int = float(0.18/12)
min_mon_pay_rate = float(0.02)
min_pay=10
mon_unpaid=0.0
tot_paid=0.0
while balance > 0 :    
    for i in range( 1 , 13 ):
        mon_unpaid = balance - min_pay
        balance = mon_unpaid + (mon_int * mon_unpaid )
        if balance <= 0:
            break
    if balance>0:    
        min_pay = min_pay*10


print("The Lowest Monthly Payment That Will Pay Off All Debt in under 1 year is :")
print(min_pay)


    

