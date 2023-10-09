def main():
    actual_value=float(input("Enter actual value of a piece of property:"))
    assess,tax_value=tax(actual_value)
    print(f'The assessment value=${assess:,.2f}')
    print(f'The property tax=${tax_value:,.2f}')
def assess(ac_value):
    assess_value=ac_value*0.6
    return assess_value
def tax(tx_value):
    ases_value=assess(tx_value)
    total_tax=0.72*ases_value/100
    return ases_value,total_tax
main()