from random import *
seed(1)
def main():
    result=int(input("Enter correct Answer from adding \n two random integers number between 1-100:"))
    answ,x,b=calculate()
    if result==answ:
        print('congratulations!!')
        print(f'{x}+{b}={answ}')
    else:
        print(f'{result} is a incorrect answer')
        print(f'correct answer is {x}+{b}={answ}')
def calculate():
    num1=randint(1,101)
    num2=randint(1,101)
    answer=num1+num2
    return answer,num1,num2
    
main()