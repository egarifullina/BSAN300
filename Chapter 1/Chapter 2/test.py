wage = float(input("Enter the wage: "))
regHours = float(input("Enter the regular hours: "))
overHours = float(input("Enter the overtime hours: "))

regularPay = wage * regHours
overtimePay = overHours * (1.5 * wage)

totalWeeklyPay = regularPay + overtimePay

print("The total weekly pay is:", "$" + str(round(totalWeeklyPay, 2)))