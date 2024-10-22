import time
#Added the import as it is needed for delays
class TrafficLight:
    def __init__(self): #These states are called for each name.
        self.states = {
            "NE": "Green",
            "SW": "Green",
            "SE": "Red",
            "NW": "Red"
        }
        self.pedestrian_signal = "Don't Walk"

    def change_state(self):
        # This is the first cycle of the light system.
        time.sleep(25)  # The lights will be on for 25 seconds
        print("NE - AMBER")
        print("SW - AMBER")
        print("----------------------")
        time.sleep(5)  # The amber lights turn on for 5 sec
        
        # This changes the opposite sides to red.
        self.states["NE"] = "Red"
        self.states["SW"] = "Red"
        self.states["SE"] = "Green"
        self.states["NW"] = "Green"
        
        print("NE - RED")
        print("SW - RED")
        print("SE - GREEN")
        print("NW - GREEN")
        print("----------------------")

        # The second cycle.
        time.sleepp(25)  # Turns the green light on for 25 seconds
        print("SE - AMBER")
        print("NW - AMBER")
        print("----------------------")
        time.sleep(5)  # Turns amber ligt on for 5 seconds
        
        # This changes the state to opposite sides again.
        self.states["SE"] = "Red"
        self.states["NW"] = "Red"
        self.states["NE"] = "Green"
        self.states["SW"] = "Green"
        
        print("SE - RED")
        print("NW - RED")
        print("NE - GREEN")
        print("SW - GREEN")
        print("----------------------")

    def pedestrian_crossing(self):
        # This defines the pedestrians for crossing.
        self.pedestrian_signal = "Walk"
        print("All lights are RED. Pedestriant Crossing Walk")
        print("----------------------")
        time.sleep(20)
        """This makes the pedestrian able to cross for 20 seconds"""
        self.pedestrian_signal = "Don't Walk"
        print("Pedestrian crossing: Don't Walk")
        print("----------------------")

    def display_states(self):
        #This shows current status and state.
        for direction in self.states:
            print(f"{direction} - {self.states[direction]}")
        print(f"Pedestrian crossing: {self.pedestrian_signal}")
        print("----------------------") #Included the separators for spacing.

    def run(self):
        while True:
            self.display_states()  # Shows the state again.
            self.change_state()  #This changes the state for traffic.
            self.pedestrian_crossing()  # Turns on the crossing.

if __name__ == "__main__":
    traffic_light = TrafficLight()  #It creates trafficlight object
    traffic_light.run()  #  Initialises the main and starts the program
