def main():
    for z in range(2,101):
        if(is_prime(z)):
            print(f'{z} is a Prime Number')
def is_prime(y):
    for x in range(2,y):
        if(y%x)==0:
            break
    else:
        return True
main()
