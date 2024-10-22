# SmartCity_TrafficLights
Date: 22/10/2024
Name : Tymoteusz Gladki
Version 1
HARDWARE REQUIREMENTS
CPU: Dual-core processor (2.0 GHz or higher)
RAM: 4 GB.
Storage: 50 GB HDD or SSD.
Operating System: Either Windows, macOS or Linux.
More Tools: Lightweight text editor; e.g., Visual Studio Code, Sublime Text, or PyCharm Community Edition.
-------Introduction ------
This project will include me creating a simple traffic light system that will have the states of the lights as well as ability to change them.
------ Algorithm ------
I have decided to go with a simple but effective algorithm of the time based cyclic algorith which will switch the states of the lights by the amount of time, for example every 30 sec.
The full cycle will be taking 120 sec which will be divide into four for north,east,south,west. The yellow light will have a phase of 5 sec in order to ensure the security of the traffic from each direction.
The pro's of this is that this is a simple and easy to implement, it allows for the drivers to predict when the light is going to change reducing uncertainty, it is relatively low maintenance 
The cons of this is that it is not efficient at managing trafic at adoptable traffic conditions like off peak and peak hours. This will lead to people waiting more even when there is no traffic.


------------ Program Description ------
The program works simply by taking the timings and making them play out on the timed basis, it starts with one side NE and SW have green lights as they do not cause any distrubtions to each others lane, then after 25 sec they start
to switch to amber for 5 sec which then stops the traffic from those directions then it switched to green for the SE NW for 25 sec and 5 sec for amber, after that all the lights turn red for 20 sec and the pedestrian crossing comes on.
This process is the basics of what the project might 
-----------Code Snippet------
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
        time.sleep(25)  # Turns the green light on for 25 seconds
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
-------------------------------------------------
This code shows how I have created then different states and the cycle for changing lights in the program. It is simplistic but it does what is supposed to do.

## Installation
1. Clone the repository
git clone https://github.com/yourusername/projectname.git
2. Navigate to the project directory:
cd SmartCity_TrafficLights
3. Install the required dependencies:
npm install


## Usage
Here’s how to use the project:
```python

import project

project.run()

#Disclaimer - This program has no usage yet but is to be built on for future projects.
#Contributing
If you want to contribute, please follow these steps:

Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
#Contact 
For any questions, feel free to reach out to me at warfarelik@gmail.com.
