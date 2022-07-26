x = 0
y = 0
d = 0


print("Welcome to Operator Calculator")
c = int(input("""PLease select the number of the operator you wish to work with:
1->Addition
2->Substraction
3->Multiplication
4->Division:
Enter the number with the Keyboard:"""))

if c==1:
        print("You are adding values")
        x= int(input('Enter First value:'))
        y= int(input('Enter Second Value:'))
        d=x+y
        print("Result is: ",d)
 
elif c==2:
        print("You are substracting values")
        x=int(input('Enter First value:'))
        y=int(input('Enter Second Value:'))
        d=x-y
        print("Result is: ",d)
elif c==3:
        print("You are Multiplying values")
        x=int(input('Enter First value:'))
        y=int(input('Enter Second Value:'))
        d=x*y
        print("Result is: ",d)

elif c==4:
        print("You are Dividing values")
        x=int(input('Enter First value:'))
        y=int(input('Enter Second Value:'))
        d=x/y
        print("Result is: ",d)
else:
        print("Please try again and select options with the keyboard: ",d)




        

    



    
