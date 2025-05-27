class Car:
    def drive(self):
        print("Driving on the road")

class Airplane:
    def fly(self):
        print("Flying on the sky")

class AmphibiousVehicle(Car, Airplane):
    pass

amphibious = AmphibiousVehicle()
amphibious.drive()
amphibious.fly() 