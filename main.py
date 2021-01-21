import time
import sys
def main():
  def add(x,y):
    return x+y

  def subtract(x,y):
    return x-y

  def multiply(x,y):
    return x*y

  def divide(x,y):
    return x/y

  def delay_print(s):
            for c in s:
              sys.stdout.write(c)
              sys.stdout.flush()
              time.sleep(0.05)


  delay_print("Hello.")
  time.sleep(0.5)
  delay_print(" My name is Colton the Calculator.\n")
  time.sleep(0.5)
  
  delay_print("1.Add\n")
  time.sleep(0.5)
  delay_print("2.Subtract\n")
  time.sleep(0.5)
  delay_print("3.Multiply\n")
  time.sleep(0.5)
  delay_print("4.Divide\n")
  time.sleep(0.5)

  i = 0
  while i < 100:
        try:
                choice = int(input("Enter a number(1,2,3,4): "))
                if choice >= 1 and choice <= 4:
                    break
                else:
                    print("Did you enter a number 1-4? No. So why did you type that! Please enter a number(1,2,3,4)  >:(")
        
        except ValueError:
            print("Did you enter a number 1-4? No. So why did you type that! Please enter a number(1,2,3,4)  >:(")
        except NameError:
            print("Did you enter a number 1-4? No. So why did you type that! Please enter a number(1,2,3,4)   >:(")
        i += 1    

  i = 0
  while i < 100:
        try:
            num1 = float(input("Enter First Number: "))
            break
        except ValueError:
            print("Did you even enter a number? No! So please enter a number this time!  >:(")
        except NameError:
            print("Did you even enter a number? No! So please enter a number this time!  >:(")
        i += 1

  i = 0
  while i < 100:
        try:
            num2 = float(input("Enter Second Number: "))
            break
        except ValueError:
            print("Did you even enter a number? No! So please enter a number this time! >:(")
        except NameError:
            print("Did you even enter a number? No! So please enter a number this time! >:(")
        i += 1

  if choice==1:
      print(num1,"+",num2,"=",add(num1,num2))
      
  elif choice==2:
      print(num1,"-",num2,"=",subtract(num1,num2))

  elif choice==3:
      print(num1,"*",num2,"=",multiply(num1,num2))

  elif choice==4:
      print(num1,"/",num2,"=",divide(num1,num2))

while True:
    main()
    if input("Are there anymore calculations you would like for me to do? (y/n): ") != "y":
        break