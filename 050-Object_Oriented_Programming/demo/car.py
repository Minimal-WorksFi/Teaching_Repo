class Car():
    car_number = 0
    def __init__(self,car_name,top_speed):
        self.car_name = car_name
        self.top_speed = top_speed
        self.speed = 0
        Car.car_number += 1
    
    def accelerate_change(self,change_of_speed):
        # We take both accelerations and decelerations here.
        self.speed += change_of_speed
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    
    def drive(self,drive_cycles):
        print("\n",self.car_name,"\n")
        for i in range(0,drive_cycles,1):
            self.accelerate_change(10)
            self.information()
        while(self.speed > 0):
            self.accelerate_change(-10)

    def information(self):
        print(self.car_name, " is driving at ", self.speed, " kph")
    
    def total_cars():
        print("\nCurrently there are ", Car.car_number, " cars\n")

if __name__ == "__main__":
    DRIVE_CYCLES = 15
    cars_list = [Car("Subaru",200),Car("Porsche",120),Car("Jeep",90)]
    for car in cars_list:
        car.drive(DRIVE_CYCLES)
        car.information()
    Car.total_cars()