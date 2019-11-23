startingLoan = float(input("Please type loan amount: "))
loan = startingLoan
interestRate = float(input("Please type interest rate: "))
lifeOfLoan = 0
totalInterest = 0
finalPayment = 0
print("\n")
print("Loan Amount :" + str(loan))
print("Interest rate :" + str(interestRate*100)+ "%")

monthly = (loan*0.05)
monthlyInterestRate = (interestRate/12)

while(loan > 0):
    payInterest = (loan * monthlyInterestRate)
    amountToPayOnBill = (monthly - payInterest)
    finalLoanAmount =  (loan - amountToPayOnBill)
    loan = finalLoanAmount
    totalInterest+=payInterest
    lifeOfLoan+=1
    if loan >0:
        finalPayment = loan
        

totalPaid = (startingLoan + totalInterest)
print("\n")

print("Loan amount                    : " + "$" + str(startingLoan))
print("Interest rate                  : " + str(interestRate*100) + "%")
print("Monthly payment                : " + "$" + str(monthly))
print("Final Payment                  : " + "$"+ str(round(finalPayment,2)))
print("Life of loan                   : " + str(lifeOfLoan)+" Months")
print("Total Interest paid            : " + "$"+ str(round(totalInterest,2)))
print("Total paid at the end of loan  : " + "$"+ str(round(totalPaid,2)))

