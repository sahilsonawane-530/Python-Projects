class Person:
    name = str(input("Enter your name : "))
    trainName = str(input("Enter train name : "))
    startPoint = str(input("Enter start point : "))
    endPoint = str(input("Enter end point : "))
    classes = str(input("Enter class : "))

    def info(self):
        print("\nYour ticket has been booked")
        print(f"{self.name} has selected {self.trainName} from {self.startPoint} to {self.endPoint} in {self.classes}")

a = Person()
a.info()