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
## Installation

To install the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/projectname.git
2. **Navigate to the project directory:**
    ```bash
   cd SmartCity_TrafficLights
3. **Install the required dependencies:**
  ```bash
   npm install
   ```

---
If you want to contribute, please follow these steps:

1.Fork the repository.   
2.Create a new branch.   
3.Make your changes.   
4.Submit a pull request.    

Contact
For any questions, feel free to reach out to me at warfarelik@gmail.com.

