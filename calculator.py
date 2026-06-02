class calculator:
    
    def menu(self):
        print('''
              PRESS 1:SUM
              PRESS 2:MULTIPLY
              PRESS 3:MINUS
              PRESS 4:DIVISON
              PRESS 5:PERCENTAGE
              PRESS 6:EXIT

        ''')
        choice=input("ENTER YOUR CHOICE:-")
        num1=int(input("ENTER FIRST NUMBER:-"))
        num2=int(input("ENTER SECOND NUMBER:-"))
        
        if choice =='1':
             num3=num1+num2
             print("YOUR SUM=",num3)

C1=calculator()
C1.menu()
