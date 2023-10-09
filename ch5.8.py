def main():
    square_feet=float(input("Enter the square feet of wall space to be painted:"))
    price_gallon=float(input("Enter the price of the paint per gallon:"))
    ########################
    n_gallon=number_gallon(square_feet)
    labo_hour=labor_hour(square_feet)
    cos_piant=cost_paints(square_feet,price_gallon)
    labo_charge=labor_charge(square_feet)
    ##########################################
    total_cost=cos_piant+labo_charge
    #######################################
    print(f'The number of gallons of paint required={n_gallon:,} gallons')
    print(f'The hours of labor required={labo_hour:,} hours')
    print(f'The cost of the paint={cos_piant:,.2f} sh')
    print(f'The labor charges={labo_charge:,.2f} sh')
    print(f'The total cost of the paints={total_cost:,.2f} sh')
def number_gallon(sq_feet):
    num_gallon=sq_feet//112
    return num_gallon
def labor_hour(sqr_feet):
    n_gallon=number_gallon(sqr_feet)
    lab_hour=n_gallon*8
    return lab_hour
    ############
    #xh=(sqr_feet*8)/112
    #return xh
def cost_paints(sqrf,pr_gal):
    n_gal=number_gallon(sqrf)
    cost_paint=n_gal*pr_gal
    return cost_paint 
def labor_charge(sqrr_feet):
    lb_hour=labor_hour(sqrr_feet)
    lab_charge=lb_hour*35
    return lab_charge
 
main()
    
