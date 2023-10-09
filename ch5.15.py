def userinput():
     grade1=float(input("Enter score 1:"))
     grade2=float(input("Enter score 2:"))
     grade3=float(input("Enter score 3:")) 
     grade4=float(input("Enter score 4:")) 
     grade5=float(input("Enter score 5:")) 
     avg=calc_average(grade1,grade2,grade3,grade4,grade5)
     ##################score#################
     print(f'{grade1} score is {determine_grade(grade1)}')
     print(f'{grade2} score is {determine_grade(grade2)}')  
     print(f'{grade3} score is {determine_grade(grade3)}')
     print(f'{grade4} score is {determine_grade(grade4)}')
     print(f'{grade5} score is {determine_grade(grade5)}')
     #################average score########################
     print(f'average score:{avg:.2f}')
     ###################################     
def calc_average(gr1,gr2,gr3,gr4,gr5):
    average=(gr1+gr2+gr3+gr4+gr5)/5
    return average
def determine_grade(gl):
    if gl>=90 and gl<=100:
       return "A"
    elif gl>=80 and gl<=89:
        return 'B'
    elif gl>=70 and gl<=79:
        return 'C'
    elif gl>=60 and gl<=69:
        return 'D'
    elif gl>=0 and gl<60:
        return 'F'
userinput()