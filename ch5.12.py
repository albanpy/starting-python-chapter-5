def main():
    n1=int(input("Enter first integer number:"))
    n2=int(input("Enter second integer number:"))
    if n1==n2:
        print('same number')
    else:
        result=max(n1,n2)
        print(f'{result:,} is greater')   
def max(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
main()

