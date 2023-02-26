class  Rover:
    def __init__(self, weigh,velocity):
        self.weight=weigh
        self.velocity=velocity

    def rover_weight(self):
        print(f"waga {self.weight} kg")

    def rover_velocity(self):
        print(f"prędkość {self.velocity} km/h")

class Sampler:
    def __init__(self, sample_range):
        self.sampler_range=sample_range
    def sampler_description(self):
        print(f"ten łazik posiada próbnik o zasięgu {self.sampler_range} cm")

class LunarRover(Rover):
    def __init__(self, weight, velocity):
        super(LunarRover, self).__init__(weight,velocity)
        self.sampler =Sampler(20)




rover1 = Rover(200,10)
rover1.rover_weight()
rover1.rover_velocity()

lunar_rover=LunarRover(400,13)
lunar_rover.rover_weight()
lunar_rover.rover_velocity()
lunar_rover.sampler.sampler_description()