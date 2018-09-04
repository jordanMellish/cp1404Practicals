"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    # """Demo test code to show how to use car class."""
    # my_car = Car(180)
    # my_car.drive(30)
    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)
    # print(my_car)
    #
    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # Limo Task
    car1 = Car('Limo', 100)
    car1.add_fuel(20)
    print('The limo has {}kms of fuel left'.format(car1.fuel))
    car1.drive(115)
    print('The limo has {}kms clocked on the odometer'.format(car1.odometer))
    print(car1)

main()
