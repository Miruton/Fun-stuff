"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old. Note: for this exercise, the expectation is that
you explicitly write out the year (and therefore be out of date the next year)."""


x = input('What is your name?: ')

y = int(input('Can you enter your current age?: '))


if y>0:
    m=y+100
    print("Hello",x ,"Nice to meet you")
    print("In the year 2122 you are turning",m,'Years Old')

        

