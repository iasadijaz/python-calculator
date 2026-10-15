condition="Yes"
while condition.strip().lower()=="yes":
      try:
            num1=float(input("Enter the first number"+" "))
            num2=float(input("Enter the second number")+" ")
            operator=input("Enter the operation you want to perform"+" ")
            if operator=="+":
                  print(num1+num2)
            elif operator=="-":
                  print(num1-num2)
            elif operator=="*":
                  print(num1*num2)
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
            
