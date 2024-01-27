class eightA:
    Amount = 24
    Girls = 11
    Boys = 13

    def __init__(self, name, avggrades, teacher):
        self.name = name
        self.avggrades = avggrades
        self.teacher = teacher


class Teachers:
    Amount = 20
    Girls = 16
    Boys = 4

    def __init__(self, name, Mainclass, Salary):
        self.name = name
        self.Mainclass = Mainclass
        self.Salary = Salary


St1 = eightA(name="Sonya", avggrades="9", teacher="Dvachevskiy D.")
St2 = eightA(name="Max", avggrades="6", teacher="Dvachevskiy D.")
St3 = eightA(name="Robert", avggrades="12", teacher="Samiy C. Umniy")

Tc1 = Teachers(name="Dvachevskiy D.", Mainclass="8A", Salary="250$ for week")
Tc2 = Teachers(name="Satoru G.", Mainclass="10B", Salary="400$ for week")
Tc3 = Teachers(name="Samiy C. Umniy", Mainclass="8A", Salary="600$ for week")

print(St1.name, St1.avggrades, St1.teacher)
print(St2.name, St2.avggrades, St2.teacher)
print(St3.name, St3.avggrades, St3.teacher)

print(Tc1.name, Tc1.Mainclass, Tc1.Salary)
print(Tc2.name, Tc2.Mainclass, Tc2.Salary)
print(Tc3.name, Tc3.Mainclass, Tc3.Salary)

