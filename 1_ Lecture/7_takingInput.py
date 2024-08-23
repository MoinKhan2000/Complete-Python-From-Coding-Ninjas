a = float(
    input(("Enter your first number\n"))
)  # byDefault input takes each input as string
 
b = float(
    input(("Enter your second numnbe\n"))
)  # to convert this we use int (type conversion)
try:
  print(a+b)
except:
  print("Enter valid numbers")