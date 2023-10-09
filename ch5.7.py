def main():
    A=int(input("how many tickets of class A seats were sold?:"))
    B=int(input("how many tickets of class B seats were sold?:"))
    C=int(input("how many tickets of class C seats were sold?:"))
    tot_amount=class_ticket(A,B,C)
    ##########################################
    print(f'The amount of income generated from ticket sales are ${tot_amount:,.2f}')
def class_ticket(ticket_A,ticket_B,ticket_C):
    class_A=ticket_A*20
    class_B=ticket_B*15
    class_C=ticket_C*10
    total_amount=class_A+class_B+class_C
    return total_amount
main()