class Vehicle():
    vehicle_number = 0

    def __init__(self,vehicle_name,top_speed):
        self.vehicle_name = vehicle_name
        self.top_speed = top_speed
        self.speed = 0
        Vehicle.vehicle_number += 1

    def accelerate_change(self,change_of_speed):
        # We take both accelerations and decelerations here.
        self.speed += change_of_speed
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    

    def drive(self,drive_cycles):
        print("\n",self.vehicle_name,"\n")

        for i in range(0,drive_cycles,1):
            self.accelerate_change(10)
            self.information()

        while(self.speed > 0):
            self.accelerate_change(-10)
    

    def information(self):
        print(self.vehicle_name, " is driving at ", self.speed, " kph")
    

    def total_vehicles():
        print(f"\nCurrently there are {Vehicle.vehicle_number} vehicles.\n")


class Bus(Vehicle):
    bus_number = 0

    def __init__(self,vehicle_name,top_speed,passenger_capacity):
        super().__init__(vehicle_name,top_speed)
        self.passenger_capacity = passenger_capacity
        self.current_passenger = 0
        Bus.bus_number += 1
    def load_unload_passengers(self,target_passenger):
        self.current_passenger = max(min(self.passenger_capacity,target_passenger),0)
        print(f"Currently the count of passengers is: {self.current_passenger}.")
    def total_busses():
        print(f"\nCurrently there are {Bus.bus_number} busses.\n")
    def information(self):
        print(self.vehicle_name, " is driving at", self.speed, " kph. It is currently carrying ", self.current_passenger, "/", self.passenger_capacity)



if __name__ == "__main__":
    DRIVE_CYCLES = 15
    vehicle_list = [Vehicle("Subaru",200),Vehicle("Porsche",120),Vehicle("Jeep",90),Bus("Volvo Bus",70,60)]
    for vehicle in vehicle_list:
        if isinstance(vehicle,Bus):
            vehicle.load_unload_passengers(30)
            vehicle.drive(15)
            vehicle.information()
            vehicle.load_unload_passengers(0)
        else:
            vehicle.drive(15)
            vehicle.information()
    
    Vehicle.total_vehicles()
    Bus.total_busses()

