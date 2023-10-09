def main():
    ammount_purchase=float(input("Enter the amount of a purchase:"))
    st_tax,ct_tax,to_tax=tax(ammount_purchase)
    total_sale=ammount_purchase+to_tax
    print(f'The amount of the purchase={ammount_purchase:,.2f}\n'+
      f'The state sales tax={st_tax:,.2f}\n'
      +f'The county sales tax={ct_tax:,.2f}\n'
      +f'The total sales tax={to_tax:,.2f}\n'
      +f'The total of the sales={total_sale:,.2f}')
def tax(purchase):
    statetax=purchase*0.05
    countystate=purchase*0.025
    tottax=statetax+countystate
    return statetax,countystate,tottax
main()

