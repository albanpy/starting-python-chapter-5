def main():
    lp=float(input("Enter cost of monthly loan payment:"))
    ins=float(input("Enter cost of monthly insurance:"))
    gs=float(input("Enter cost of monthly gas:"))
    ol=float(input("Enter cost of monthly oil:"))
    tr=float(input("Enter cost of monthly tires:"))
    mt=float(input("Enter cost of monthly maintenance:"))
    ###################################################
    monthly_cost,yearly_cost=calculate_cost(lp,ins,gs,ol,tr,mt)
    ################################################################
    print(f"Total monthly cost of these expenses are {monthly_cost:,.2f} sh")
    print(f"Total annual cost of these expenses are {yearly_cost:,.2f} sh")
    ############################################################
    ############################################################
def calculate_cost(loan,insuarence,gas,oil,tires,maintenance):
    month_cost=loan+insuarence+gas+oil+tires+maintenance
    year_cost=month_cost*12
    return month_cost,year_cost
main()