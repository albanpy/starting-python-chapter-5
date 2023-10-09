from random import *
seed(0)
def main():
    count_even=0
    count_odd=0
    for i in range(100):
        number=randrange(1,101)
        if(even(number)):
            count_even+=1
        if (odd(number)):
            count_odd+=1
    print(f'number of even number in range number of 1-100 are {count_even}')
    print(f'number of odd number in range number of 1-100 are {count_odd}')
def even(ev_n):
    if ev_n%2==0:
        return True
def odd(od_n):
    if od_n%2==1:
        return True
main()