def main():
    cost_replace=float(input("Enter the replacement cost of a building:"))
    amount_insua=insuarence(cost_replace)
    print(f'The minimum amount of insurance you should buy for the property={amount_insua:,.2f} sh')
def insuarence(amount):
    total_insua=amount*0.8
    return total_insua
main()

