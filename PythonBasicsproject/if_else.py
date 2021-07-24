
while True:
    print('Enter The Your Age: ')
    age = int(input())

    if age > 7 and age<100:

        if age>18 and age<60:
            print('you can drive')

        elif age==18:
            print('we will think about')
            
        else:
            print('you can not drive')

    else:
        print('you are the out of age')
        
# faulty calculator 
def faulty():
    while True:
        operators = ['+', '-', '*', '/']
        print(operators)
        print('Enter your operators')
        operators_input = input()
        if operators_input in operators:
                print('Enter your number:')
                n1 = int(input())
                n2 = int(input())
                if operators_input=='+':
                    if (n1==56 and n2==9) or (n1==9 and n2==56):
                        print(77)
                    else:
                        print(n1+n2)

                elif operators_input=='-':
                    print(n1-n2)

                elif operators_input=='*':
                    if n1==45 and n2==3 or n1==3 and n2==45:
                        print(555)
                    else:
                        print(n1*n2)

                elif operators_input=='/':
                    if n1==56 and n2==6 or n1==6 and n2==56:
                        print(4)
                    else:
                        print(n1/n2)
        elif operators_input=='exit':
            break
        
        else:
            print('try again')

if __name__=='__main__':
    faulty()
