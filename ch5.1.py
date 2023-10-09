def main():
    kilo=float(input("Enter a distance in kilometers:"))
    result(kilo)
def convert(kilometer):
    miles=kilometer*0.6214
    return miles
def result(kl):
    res=convert(kl)
    print(f"The distance {kl:,.2f} kilometers is equal to {res:,.2f} miles")
main()