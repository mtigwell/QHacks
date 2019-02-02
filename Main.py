
class budgetType:
    def __init__(self, budget, type):
        if(type == 1):
            self.optionName = "Scrouge McDucky"
            self.Transport = budget * .01
            self.Bills = budget * .2
            self.Business_Services = budget * .02
            self.Education = budget * .03
            self.Entertainment = budget * .02
            self.Fees = budget * .03
            self.Financial = budget * .03
            self.Food = budget * .1
            self.Gym = budget * .01
            self.Home = budget * .2
            self.Personal_Care = budget * .01
            self.Taxes = budget * .2
            self.misc = budget * .01
            self.Savings = self.getSum(budget)

        if (type == 2):
            self.optionName = "Medium"
            self.Transport = budget * .01
            self.Bills = budget * .2
            self.Business_Services = budget * .02
            self.Education = budget * .03
            self.Entertainment = budget * .05
            self.Fees = budget * .03
            self.Financial = budget * .03
            self.Food = budget * .1
            self.Gym = budget * .01
            self.Home = budget * .2
            self.Personal_Care = budget * .01
            self.Taxes = budget * .2
            self.misc = budget * .01
            self.Savings = self.getSum(budget)
        if (type == 3):
            self.optionName = "High Roller"
            self.Transport = budget * .01
            self.Bills = budget * .2
            self.Business_Services = budget * .02
            self.Education = budget * .03
            self.Entertainment = budget * .1
            self.Fees = budget * .03
            self.Financial = budget * .03
            self.Food = budget * .1
            self.Gym = budget * .01
            self.Home = budget * .2
            self.Personal_Care = budget * .01
            self.Taxes = budget * .2
            self.misc = budget * .01
            self.Savings = self.getSum(budget)
        if (type == 4):
            self.optionName = "Custom"
            self.Transport = 0
            self.Bills = 0
            self.Business_Services = 0
            self.Education = 0
            self.Entertainment = 0
            self.Fees = 0
            self.Financial = 0
            self.Food = 0
            self.Gym = 0
            self.Home = 0
            self.Personal_Care = 0
            self.Taxes = 0
            self.misc = 0
            self.Savings = self.getSum(budget)

    def getSum(self, budget):

        sum = self.Transport + self.Bills  + self.Business_Services + self.Education +  self.Entertainment  + self.Fees + self.Financial + self.Food + self.Gym + self.Home + self.Personal_Care + self.Taxes + self.misc

        return budget - sum

    def printBudgetInfo(self):
        print("Budget Type : " +  self.optionName)
        print("     Transport: " + str(self.Transport))
        print("     Bills: " + str(self.Bills))
        print("     Business_Services: " + str(self.Business_Services))
        print("     Education: " + str(self.Education))
        print("     Entertainment: " + str(self.Entertainment))
        print("     Fees: " + str(self.Fees))
        print("     Financial: " + str(self.Financial))
        print("     Food: " + str(self.Food))
        print("     Gym: " + str(self.Gym))
        print("     Home: " + str(self.Home))
        print("     Personal_Care: " + str(self.Personal_Care))
        print("     Taxes: " + str(self.Taxes))
        print("     misc: " + str(self.misc))
        print("     Savings: " + str(self.Savings))



class Account:
    def __init__(self, name, password, income, option):
        self.name = name
        self.password = password
        self.budget = income
        self.option = budgetType(self.budget,option)




    def printAccountInfo(self):
        print("Name: " + self.name)
        print("Password: " + self.password)
        print("Budget: " + str(self.budget))
        self.option.printBudgetInfo()




ShowCase1 = Account("showcase1", "12345", 50000, 1)
ShowCase2 = Account("showcase2", "12345", 50000, 2)
ShowCase3 = Account("showcase3", "12345", 50000, 3)
ShowCase4 = Account("showcase4", "12345", 50000, 4)
ShowCase1.printAccountInfo()
ShowCase2.printAccountInfo()
ShowCase3.printAccountInfo()
ShowCase4.printAccountInfo()
