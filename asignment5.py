# 1. Calculate area of circle.
def calcArea(r,pi=3.14):
    A = r ** 2 * pi
    print(A)
calcArea(8.7)
calcArea(9.2)
calcArea(16.03)

# 2. Write function to check if a value exists in a list
def checkVal():
    data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
    print(data)
    for a in data:
         if a=="python":
            print("python found in data list")
         elif a=="html":
             print("html found in data list")
         elif a=="c":
            print("c found in data list")
checkVal()

# 3. Write a function to shift list item to right n times
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
def shiftItems(ListName,n):
    return ListName[-n:] + ListName[:-n]
print(data)
print(shiftItems(data,1))
print(shiftItems(data,3))

# # 4. Use while loop to get data
# You have to write a while loop to get input from user for `radius of circle`.
# If user enters `quit`, break the loop, otherwise call `calcArea` function to
# get area of cricle from radius and print `area of circle`.

p="yes"
def calcArea():
    r = float(input("Enter radius of circle: "))
    A = r ** 2 * 3.14
    print(f"area of circle is {A} ")
while True:
    calcArea()
    p = input("If you want to exit enter 'quit': ")
    if p=="quit":
        break

"""
name ="Ali"
clas = "AI"
marks = {"math" : 50, "physics" : 80, "biology" : 90, "computer" : 67}
date = "1 Feb 2020"
nextClass = True
total_marks = 0
avg= 1
sm=0
# def showDetails(**kwargs):
def tm():
    global total_marks,avg
    total_marks = marks["math"]+marks["physics"]+marks["biology"]+marks["computer"]
    # print(total_marks)s
    avg = total_marks/len(marks)
    # print(avg)
    if marks['biology']>marks["math"] or marks['biology']>marks["physics"]:
        print("Maximum marks are in "Biology")

tm()
print(f"Hello {name}\nHere is your result for class of {clas}.\nYour score card is as follows.\nClassMarks:\n\t:{marks['math']}\n\t:{marks['physics']}\n\t:{marks['biology']}\n\t:{marks['computer']}"
      f"\nTotal marks are: {total_marks}\nPercentage is as follows: {avg}%\nMaximum marks are in \nMinimum marks are in \nYou are promoted to next class.")
"""