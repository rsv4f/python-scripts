import csv
import random as rand

print("Enter amount of people to survey: ")
people = int(input())
#age = rand.randint(18, 62)

'''
used traditional student instead of age.
tradidional_student is better indicator for current project
'''

computer = ["PC", "Mac", "Other"]
myBool = [True, False]
phone = ["iPhone", "Android", "Other"]

# create a function that writes to a file
def write_to_file():
    with open("survey.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow([ #  write the header
            "Age",
            "PC/Mac/Other",
            "Phone",
            "Employed",
            "PCCycle(yrs)",
            "PhoneCycle(yrs)",
            "DIYRepairs",
            "PurchaseWarranty",
            "OwnVehicle",
            "DIYMaintenance",
            ])
        for i in range(0, people):
            writer.writerow([
                rand.randrange(18,62),  # age
                computer[rand.randint(0,2)], # computer
                phone[rand.randrange(0,2)], # phone
                myBool[rand.randrange(0, 2)],  # employment status 
                rand.randrange(0, 5), # PC upgrade cycle
                rand.randrange(0, 5), # phone upgrade cycle
                myBool[rand.randrange(0, 2)], # DIY repairs
                myBool[rand.randrange(0, 2)], # purchase warranty
                myBool[rand.randrange(0, 2)], # own vehicle
                myBool[rand.randrange(0, 2)], # DIY maintenance
            ])

write_to_file() # write to csv file