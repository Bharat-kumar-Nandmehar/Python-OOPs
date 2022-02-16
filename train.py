class Train:
    def __init__(self , name, fare, seats , name1):
        self.name=name
        self.fare=fare
        self.seats=seats
        self.name1=name1
    @staticmethod
    def great():
        print("Thank you sir for booking a Train ticket , Details of your tickets are mentioned below :")

    def getinfo(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats in this train is {self.seats}")
    def getFareInfo(self):
        print(f"The fare of the train is {self.fare}")
    def getBooking(self):
          if self.seats>0:
                  print(f"Your train ticket is booked , and the seat no. is {self.seats}")
                  self.seats= self.seats - 1

          else:
              print("No ticket are available as our train is fully booked , Please try in tatkal ")
    def getInfoPassengerr(self):
        print(f"The name of the passenger is {self.name1}")

a=input("Enter the name:")
Domestictrain=Train("Rajdhani Express",100,400,a)
Domestictrain.great()
Domestictrain.getInfoPassengerr()
Domestictrain.getinfo()
Domestictrain.getFareInfo()
Domestictrain.getBooking()

