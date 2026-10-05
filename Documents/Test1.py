print("What is your first name?")
first_name = input()
print("What is your last name?")
last_name = input()
answer = "y"
while answer == "y":
   print("Give me two integers and I will add, subtract, multiply, divide, and find the remainder between them")
   Num1=int(input())
   Num2=int(input())
   print(first_name," ",last_name," , your numbers added together is ",Num1+Num2," , subtracted is ",Num1-Num2,", multiplied is ",Num1*Num2," , divided is ",Num1//Num2," , and the remainder is ",Num1%Num2)
   print("Do you want me to continue, (y/n)")
   answer = input()
exit()