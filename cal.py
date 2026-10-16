import math
condition="Yes"
while condition.strip().lower()=="yes":
      try:
            num1=float(input("Enter the first number"+" "))
            operator=input("Enter the operation you want to perform"+" ") 
            if operator=="sqrt":
                  if num1<0:
                        print("Square Root of negative number is considered imaginary in math.")
                  else:
                        print(math.sqrt(num1))
            else:
                  if operator in ["+","-","*","**","/"]:
                                    num2=float(input("Enter the second number"+" "))
                                    if operator=="+":
                                                print(num1+num2)
                                    elif operator=="-":
                                                print(num1-num2)
                                    elif operator=="*":
                                                print(num1*num2)
                                    elif operator=="**":
                                                if num1==0 and num2<0:
                                                      print("Power can't be performed on such numbers.As it is undefined")
                                                else:
                                                      print(num1**num2)
                                    elif operator=="/":
                                                if num2==0:
                                                      print("Denominator can't be zero")
                                                else:
                                                      print(num1/num2)
                  else:
                        print("Invalid Operator")
      except:
            print("Enter a valid number Kindly")
      condition=input("Do you want to perform another calculation:"+" ")
print("Thank you for choosing our calculator")
            
