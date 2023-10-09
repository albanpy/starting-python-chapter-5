def main():
    month_sale=float(input("Enter the total sales for the month:"))
    st_tax=state(month_sale)
    co_tax=county(month_sale)
    total_tax=st_tax+co_tax
    ####################################
    print(f'The amount of county sales tax are {co_tax:,.2f}')
    print(f'The amount of state sales tax are {st_tax:,.2f}')
    print(f'The total sales tax are {total_tax:,.2f}')
def state(mo_sale):
    state_tax=mo_sale*0.05
    return state_tax
def county(m_sale):
    county_tax=m_sale*0.025
    return county_tax
main()