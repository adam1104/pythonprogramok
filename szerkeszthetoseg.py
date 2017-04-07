a=int(input("1. oldal: "))
b=int(input("2. oldal: "))
c=int(input("3. oldal: "))
if a+b>c and b+c>a and a+c>b:
	print("Megszerkeszthető")
else:
	print("Nem megszerkeszthető")
