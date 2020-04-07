import sys

sys.stdin = open('input.txt', 'r')

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    def calculate(self):
        avg_mark=sum(scores)/scores_count
        if 90<=avg_mark<=100:
            return 'O'
        elif 80<=avg_mark<90:
            return "E"
        elif 70<=avg_mark<80:
            return 'A'
        elif 55<=avg_mark<70:
            return 'P'
        elif 40<=avg_mark<55:
            return 'D'
        else:
            return 'T'
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()

if __name__ == '__main__':
    Student.printPerson()
