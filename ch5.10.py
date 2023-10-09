def main():
    number_feet=float(input("Enter a number of feet:"))
    number_inches=feet_to_inches(number_feet)
    print(f"The {number_feet:,.2f} feet is equal to {number_inches:,.2f} inches")
def feet_to_inches(num_feet):
    num_inches=num_feet*12
    return num_inches
main()