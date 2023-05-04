import pandas as pd

collection = {
    "Employee ID": ["161E90", "161F91", "161F99", "171E20", "171G30"],
    "Name": ["Raman", "Himadri", "Jaya", "Tejas", "Ajay"],
    "Age": [41, 38, 51, 30, 45],
    "Salary(PM)": [56000, 67500, 82100, 55000, 44000]
}

df = pd.DataFrame(collection)


class Employee:
    def __init__(self, data):
        self.data = data

    def age(self):
        self.sdf = self.data.sort_values(by=["Age"], ascending=True)
        return self.sdf

    def name(self):
        self.sdf = self.data.sort_values(by=["Name"], ascending=True)
        return self.sdf

    def salary(self):
        self.sdf = self.data.sort_values(by=["Salary(PM)"], ascending=True)
        return self.sdf


ob = Employee(df)

choose = 1

while choose:
    print("0. Exit")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choose = int(input("Enter your choice:"))
    if choose == 1:
        print(ob.sort_age())
    elif choose == 2:
        print(ob.sort_name())
    elif choose == 3:
        print(ob.sort_salary())
    elif choose == 0:
        print("Exiting")
    else:
        print("Wrong ans")