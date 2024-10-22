# SmartCity_TrafficLights
I have decided to go with a simple but effective algorithm of the time based cyclic algorith which will switch the states of the lights by the amount of time, for example every 30 sec.
The full cycle will be taking 120 sec which will be divide into four for north,east,south,west. The yellow light will have a phase of 5 sec in order to ensure the security of the traffic from each direction.
The pro's of this is that this is a simple and easy to implement, it allows for the drivers to predict when the light is going to change reducing uncertainty, it is relatively low maintenance 
The cons of this is that it is not efficient at managing trafic at adoptable traffic conditions like off peak and peak hours. This will lead to people waiting more even when there is no traffic.

------------
The program works simply by taking the timings and making them play out on the timed basis, it starts with one side NE and SW have green lights as they do not cause any distrubtions to each others lane, then after 25 sec they start
to switch to amber for 5 sec which then stops the traffic from those directions then it switched to green for the SE NW for 25 sec and 5 sec for amber, after that all the lights turn red for 20 sec and the pedestrian crossing comes on.
