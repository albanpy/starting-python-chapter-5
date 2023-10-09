def main():
    P=float(input("Enter the account’s present value:"))
    i=float(input("Enter monthly interest rate in %:"))
    t=float(input("Enter the number of months that\n the money will be left in the account:"))
    F_value=future_value(P,i,t)
    print(f"The account’s future value={F_value:,.2f} SH")
def future_value(P,i,t):
    F=P*(1+i/100)**t
    return F
main()