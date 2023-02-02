#A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
#Write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.
salary = int(input())
experience = int(input())

if experience > 5:
    bonus = salary *0.05
    print(bonus)
else:
    print("No Bonus")