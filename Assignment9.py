'''Q1'''
'''Defining Circle class'''
class Circle():
    def __init__(self, r):
        self.radius = r
    '''Initializing class with a Radius r'''

    def getArea(self):
        return self.radius ** 2 * 3.14
    '''getArea() method to calculate Area'''

    def getCircumference(self):
        return 2 * self.radius * 3.14
    '''getCircumferece() method to calculate Circumference'''

NewCircle = Circle(int(input("Enter the Radius: ")))
'''Creating object of Circle class and taking radius from user as input'''
print(NewCircle.getArea())
'''Calculating and printing the area of circle'''
print(NewCircle.getCircumference())
'''Calculating and printing the Circumference of circle'''

'''Q2'''
'''Defining Student Class0'''
class Student():
    def __init__(self):
        self.name = input("Enter the Name of Student: ")
        '''Taking Name of Student as Input from user'''
        self.roll = int(input("Enter the Roll number of the Student: "))
        '''Taking Roll Number of Student as Input from user'''

    def display(self):
        '''Display method to display Details of Student'''
        print("Name: ", self.name)
        print("Roll Number: ", self.roll)

NewStudent = Student()
'''Creating Object of Student Class'''
NewStudent.display()
'''Calling display() megthd to print details'''

'''Q3'''
class Temprature():
    '''Defining Temprature Class'''
    def convertFahrenheit(self):
        c = int(input("Enter the Temprature in Celcius: "))
        f = (c * 1.8) + 32
        print("Temprature in Fahrenheit: ", f)
        '''Defining convertFahrenheit() method to convert Celcius to Fahrenheit'''
    def convertCelsius(self):
        f = int(input("Enter the Temprature in Fahrenheit: "))
        c = (f - 32) / 1.8
        print("Temprature in Celcius: ", c)
        '''Defining convertCelcius() method to convert Fahrenheit to Celcius'''

NewTemprature = Temprature()
NewTemprature.convertCelsius()
NewTemprature.convertFahrenheit()

'''Q4'''
class MovieDetails():
    '''Defining MovieDetails Class'''
    def __init__(self):
        self.name = input("Enter the Name of the Movie: ")
        self.artistname = input("Enter the Name of the Artist: ")
        self.release = input("Enter the Year of Release: ")
        self.ratings = int(input("Enter the Ratings out of 10: "))
        '''Initializing class with Name,Artist name,release & ratings with input from user'''

    def display(self):
        print("Name: ", self.name)
        print("Artist Name: ", self.artistname)
        print("Year of Release: ", self.release)
        print("Ratings(out of 10): ", self.ratings)

    def update(self):
        self.name = input("Enter the Updated Name: ")
        self.artistname = input("Enter the Updated Name of the Artist: ")
        self.release = input("Enter the Updated Year of Release:")
        self.ratings = input("Enter the Updated Ratings:")
        self.display()

NewMovie = MovieDetails()
NewMovie.display()
NewMovie.update()

'''Q5'''
class Expenditure():
    def __init__(self):
        self.expenditure = int(input("Enter the Expenditure: "))
        self.savings = int(input("Enter the Savings: "))

    def display(self):
        print("Expenditure: ", self.expenditure)
        print("Savings: ", self.savings)

    def calTotalSalary(self):
        self.totalSal = self.expenditure + self.savings

    def displayTotalSalay(self):
        print("Totak Salary: ", self.totalSal)

NewExpenditure = Expenditure()
NewExpenditure.display()
NewExpenditure.calTotalSalary()
NewExpenditure.displayTotalSalay()