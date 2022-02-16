#OOPS
class Employee:
    company="Microsoft"
    def __init__(self, name , product):
        self.name=name
        self.product=product
    def getInfo(self):
            print(f"The name of the pragrammer is {self.name} and the product is {self.product} ")
Bharat=Employee("Bharat", "WhatsApp")
Sarita=Employee("Sarita", "Microsoft website")
Santy=Employee("Santy", "Microsoft Edge")
Ash=Employee("Ash", "Alexa")
Bharat.getInfo()
Sarita.getInfo()
Santy.getInfo()
Ash.getInfo()
