This account will be used to keep track of my programming progression where the first language will be python.py

this my first project(calculator) I worked with the if,elif,else statements and was able to understand loops better


list = ("+","-","x","/")
operator = None
opnieuw = True 
nieuw_som = ("y","n")

while opnieuw:

    operator = None

    while operator not in list:
        operator = input("wat wordt het vandaag (+ - x / ):")
     
    num1 = float(input("eerste nummer:"))
    num2 = float(input("tweede nummer:"))

    if operator == "+":
        print("result:"+ str(num1 + num2))
    elif operator == "-":
        print("result:"+ str(num1 - num2))
    elif operator == "x":
        print("result:"+ str(num1 * num2))
    else:
        print("result:"+ str(num1 / num2))
    
    nieuw_som = input("wil je nog iets bereken ? (y/n)").lower()
    if not nieuw_som == "y":
        opnieuw = False
        print("tot de volgende keer !")
