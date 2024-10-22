# SmartCity_TrafficLights

**Date:** 22/10/2024  
**Author:** Tymoteusz Gladki  
**Version:** 1.0  

## Hardware Requirements
- **CPU:** Dual-core processor (2.0 GHz or higher)
- **RAM:** 4 GB
- **Storage:** 50 GB HDD or SSD
- **Operating System:** Windows, macOS, or Linux
- **Tools:** Lightweight text editor (e.g., Visual Studio Code, Sublime Text, PyCharm Community Edition)

---

## Introduction
This project involves creating a simple traffic light system that can manage the states of the lights and change them as necessary.

## Algorithm
I have implemented a time-based cyclic algorithm that switches the states of the lights every 30 seconds. The full cycle lasts 120 seconds and is divided into phases for North, East, South, and West. The yellow light has a 5-second phase to ensure traffic safety.

### Pros:
- Simple and easy to implement
- Predictable light changes for drivers
- Relatively low maintenance

### Cons:
- Not efficient for varying traffic conditions (peak vs. off-peak)
- Potentially longer wait times during low traffic

---

## Program Description
The program operates on a timed basis, starting with the NE and SW directions showing green lights. After 25 seconds, these lights switch to amber for 5 seconds, then turn red. The SE and NW directions then switch to green for another 25 seconds, followed by their amber phase. Finally, all lights turn red for 20 seconds to activate the pedestrian crossing.

This cycle forms the foundation of the traffic light management system.

---

## Code Snippet
```python
def change_state(self):
    # This is the first cycle of the light system.
    time.sleep(25)  # The lights will be on for 25 seconds
    print("NE - AMBER")
    print("SW - AMBER")
    print("----------------------")
    time.sleep(5)  # The amber lights turn on for 5 sec
    
    # Change the opposite sides to red.
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
    time.sleep(5)  # Turns amber light on for 5 seconds
    
    # Change the state to opposite sides again.
    self.states["SE"] = "Red"
    self.states["NW"] = "Red"
    self.states["NE"] = "Green"
    self.states["SW"] = "Green"
    
    print("SE - RED")
    print("NW - RED")
    print("NE - GREEN")
    print("SW - GREEN")
    print("----------------------")
---
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/projectname.git
Navigate to the project directory:
bash
Copy code
cd SmartCity_TrafficLights
Install the required dependencies:
bash
Copy code
npm install
Usage
Here’s how to use the project:

python
Copy code
import project

project.run()

# Disclaimer: This program is still in development and is intended for future enhancements.
Contributing
If you want to contribute, please follow these steps:

Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
Contact
For any questions, feel free to reach out to me at warfarelik@gmail.com.

css
Copy code

Feel free to adjust any sections as needed! This format should provide a clear, structured, a
