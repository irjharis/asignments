# 1. Indexing
# Example 1
employee_data = ['Ali', 125000, 'Google', 5]
print(employee_data[0],"is working in",employee_data[2],"for",employee_data[3],"years and his salary is",employee_data[1])

# Example 2
studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,'28 Januray 2020', '05 February 2020']
print("Hello",studentData[0],studentData[1]+",","\n""Your application is accepted for admission in"
      ,'"'+studentData[4],studentData[3]+'"',"in",studentData[2]+".""\n""You have to submit fee",studentData[5]
      ,"before",studentData[6]+".","\n""Your classes will start from",studentData[7]+".","\n""Thanks")

# 2. Slicing
cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]
# For positive slicing
print(cities[0:4])
print(cities[2:6])
print(cities[5:8])

# For negative slicing
print(cities[-4:-1])
print(cities[-5:])

# 3. Update Lists
#Add values to this list using `append`
studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]
studentData.append("20 February 2019")
studentData.append(8)
print(studentData)

"""
Use `insert` method to insert at specific index
1. 25000 at index 4
2. 'M. Iqbal' at index 1
"""
studentData.insert(4,25000)
studentData.insert(1,"M. Iqbal")
print(studentData)

"""
Update list using list update method:
1. Change Name from 'Ali Raza' to 'Zohaib Ali'
2. Change No of subjects from 5 to 7
"""
studentData[0] = "Zohaib Ali"
studentData[6] = 7
print(studentData)

"""
Remove values from list using `remove` method
1. 'Computer Science'
2. 91.24
"""
studentData.remove("Computer Science")
studentData.remove(91.24)
print(studentData)

"""
Remove using `pop` method
1. Last value from list
2. value at 3rd index
"""
studentData.pop()
studentData.pop(3)
print(studentData)

"""
# 4. Multidimensional list tasks
# For Loop
1. Print name of employees with salary greater than 50000.
2. Calculate total salary of all employees.
"""
employeeData = [["Ali", 35000, "Software Engineer"],["Talha", 55000, "Product Manager"],["Nasir", 79000, "Computer Engineer"],["Khalid", 44000, "DBA"]]
ts = 0
print("Employees name whose salary is greater than 50000:")
for i in employeeData:
      sal = i[1]
      name = i[0]
      ts += sal
      if sal > 50000:
            print(name)
print("Total salary of all employees:",ts)

"""
# List update tasks
1. Change salary of nasir from 79000 to 90000 and designation to "Product Manager"
2. Change salary of Khalid to 50000
"""
employeeData[2][1] = 90000
employeeData[2][2] = "Product Manager"
employeeData[3][1] = 50000
print(employeeData)


"""
# 5. Login User
You have given some users data. You have to write a script to check if username and password are correct.
If `username` and `password` are correct. Then you have to check if email is verified or not.
If it is verified then print `Login Succeed` else print `Email not verified`. 
If username or password are incorrect you have to print `Incorrect Login details`
"""
# Data 1
username = str(input("Enter username:"))
password = str(input("Enter password:"))
emailVerified = False

if username == "haris" and password == "h123":
      if emailVerified == True:
            print("Login Succeed")
      else:
            print("Email not verified")
else:
      print("Incorrect Login details")

# Data 2
emailVerified = True

if username == "haris" and password == "h123":
      if emailVerified == True:
            print("Login Succeed")
      else:
            print("Email not verified")
else:
      print("Incorrect Login details")
