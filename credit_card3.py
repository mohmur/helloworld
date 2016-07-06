balance = int(input("Enter the outstanding balance:"))
act_balance = balance
ann_int = float(0.18)
mon_int = float(0.18/12)
min_mon_pay_rate = float(0.02)
mon_lb = balance/12
mon_ub = (balance*pow((1+mon_int),12))/12.0
print("lb:")
print(mon_lb)
print("ub:")
print(mon_ub)
min_pay = mon_lb
while balance > 0 and min_pay < mon_ub :    
    for i in range( 1 , 13 ):
        mon_unpaid = balance - min_pay
        balance = mon_unpaid + (mon_int * mon_unpaid )
        if balance <= 0:
            break        
    if balance>0:    
        min_pay = min_pay+0.01
        balance = act_balance


print("The Lowest Monthly Payment That Will Pay Off All Debt in under 1 year is :")
print(float(int(min_pay*100)/100))



    

