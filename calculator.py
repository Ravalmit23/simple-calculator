class calculator:
    
    def menu(self):
        print('''
THIS IS A SIMPLE CALCULATOR!
              PRESS 1:SUM
              PRESS 2:MULTIPLY
              PRESS 3:SUBTRACTION
              PRESS 4:DIVISON
              PRESS 5:PERCENTAGE
              PRESS 6:EXIT

        ''')
        num1=int(input("ENTER FIRST NUMBER:-"))
        num2=int(input("ENTER SECOND NUMBER:-"))
        
        choice=input("ENTER YOUR CHOICE:-")
        
        if choice =='1':
             num3=num1+num2
             print("YOUR SUM=",num3)
        elif choice =='2':
            num3=num1*num2
            print("YOUR MULTIPLY=",num3)
        elif choice =='3':
            num3=num1-num2
            print("YOUR MINUS=",num3)
        elif choice =='4':
            num3=num1/num2
            print("YOUR DIVISION=",num3)
        elif choice =='5':
            num3=(num1/num2)*100
            print("YOUR PERCENTAGE=",num3)
        elif choice=='6':
            exit()
        

C1=calculator()
C1.menu()
