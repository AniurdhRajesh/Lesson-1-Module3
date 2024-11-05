while True:
 print("/ for Division")
 print("* for Multiplication")
 print("+ for Addition")
 print("- for Subtraction")
 op=input("Enter the Operation : ")
 n1=int(input("Enter the first number : "))
 n2=int(input("Enter the second number : "))
 
 def add():
  print(n1+n2)
 def sub():
   print (n1-n2)
 def mul():
     print (n1*n2)
 def div():
    print (n1/n2)
 if op=="/":
     div()
 elif op=="*":
     mul()
 elif op=="+":
     add()
 elif op=="-":
    sub()
 else:
    print("Invalid")