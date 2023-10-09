def main():
    number=int(input("Enter number to check if Prime number:"))
    if(is_prime(number) or number==1):
        print(f'{number} is not Prime Number')
    else:
        print(f'{number} is Prime Number')
def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return True
                break
main()