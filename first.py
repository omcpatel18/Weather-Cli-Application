# Name = "OMpatel"
# print(Name[0])
# print(Name[1])
# print(Name[2])
# print(Name[3])
# print(Name[4])
# print(Name[5])
# print("\n")
# print("\n")
# print(Name[-1])
# print(Name[-2])
# print(Name[-3])
# print(Name[-4])
# print(Name[-5])
# print(Name[-6])

# # NAMES = "we are engineers."
# print(NAMES)
# print(NAMES[0:14])
# print(len(NAMES))
# print(NAMES[0:5])
# print(NAMES[:3])
# print(NAMES[0:-4])

# nm = "HARRY"
# print(nm[-4:-2])

# print("hello world\n"*102)

# for i in range(102):
#     print("count start at ", i)

# print(2+5)

# print(2 > 1 )

# print(5 < 3)

# print(33 > 12)

# print(15 != 15)

# print(15 == 15 )

# print( 15 != 12)

# string = "python"
# print(string[0])
# print(string[0:3])
# print(string[0:])
# print(string[-3:-1])
# print(string[:2])
# print(string[:])


# age = float(input("Enter a number:"))
# if age > 18:
#     message = "Eligible"
# elif age == 18:
#     message = "Also Eligible"
# else :
#     message = "Not Eligible"

# print(message)

# item = input("Enter Items names:")
# red = bool(input("Does it is red ? True or False"))
# value = bool(input("Does it valuable ? True or False"))

# if  red or value:
#     print( "item is important use it wisely.dont over use it;)") 
# else:
#     print("Use some good things. have some faith. :)") 

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" < "cat":
#     print("b")
# else:
#     print("c")  

# for i in range (15):
#     print(i)

# attemp = 0

# for attemp in range (15):
#     print(attemp)
#     if 5 <= attemp <= 10:
#         print("enough attempt is given.")

# Successful = False
# for number in range(3):
#     print("Attempt")
#     if Successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed.")
# rows = 5
# for x in range(1, rows+1):
#    print("*"*x)


# while True:
#     print("echo")

# count = 0
# for i in range (2,10,2):
#     if( i % 2 == 0):
#         count += 1 
#         print("i=",i)

# print(f"We have {count} even numbers.")

# num = 2

# def add(number):
#     global num
#     total =  num + number
#     print(total)

# add(5)

numbers = [0,1,2,3,4,5,6 ,7,8,9]
first, second, third,*other = numbers
print(first)
print(second)
print(third)
print(other) 


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    print(total)

multiply(numbers)