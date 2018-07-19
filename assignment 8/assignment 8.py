

#1
print("Time tuple is used to represen time in a way it is easy to understand.And it is stored in tuple.And also that these tuples aree made of nine numbers..")
print("eg:index:0->year...index:1->Month...index:2->Day...index:3->hour...index:4->Minute..index:5->Sec..index:6->Day of Week..index:7->day f year..index:8->Dst")

#2

print("Formitted time:"+time.asctime(time.localtime()))

# 3
print(time.strftime("%b"))

#4

print(time.strftime("%A"))

#5

dateen=int(input("Enter  the date"))
yearen=int(input("Enter  the Year"))
monen=int(input("Enter  the month"))

dateentered=datetime.date(yearen,monen,dateen)
print(dateentered.strftime("%b"))

# 6:
print(strftime("%H:%M:%S", gmtime()))

#7:

x=int(input("Enter  any number"))
print("the factorial is"+" "+str(math.factorial(x)))

#8:
a= int(input("Enter 1 number"))
b= int(input("Enter 2 number"))
print("gcd is:"+str(math.gcd(a, b)))

# 9:

print("Current Working Directory"+str(os.getcwd()))
print("User environment"+str(os.environ))