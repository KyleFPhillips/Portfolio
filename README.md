# Portfolio
## About
Maths Graduate

## Modules
Tech modules studied in my degree include:
- Basic Statistics
- Programming
- Computational Modelling
- Statistical Modelling
- Space Dynamics
- Nonlinear Optimisation
- Nonlinear Systems
- Final year dissertation (Focusing on Neural Networks/Machine Learning)

## Projects Included:

### Dissertation code
Final Year Project Code 1 & 2 are basic neural network systems used in my dissertation:

- Code 1 is a basic feed forward network specifically avoiding using any additional machine learning libraries. Based on solving the XOR gate problem. The network is constructed and fed each of the 4 outcomes you can get out of a XOR gate which the program will then learn through training and will give you the correct XOR response when you ask it one of the options as test data. As the program is repeatedly training itself on the XOR responses it will record each EPOCH and plot the trendline of "Loss values" against "EPOCHs" showcasing the accuracy of the program increasing over time.

- Code 2 is a form of NLP for sentiment analysis which trains itself to measure sentiment in a written form. Using an excel sheet of ~5000 Amazon reviews of various products that tracks the sentiment (whether it was a positive, neutral or negative review), the program will train itself on a majority of the reviews (80%) feeding the information in through multiple EPOCHs and at the end it will test itself on the remaining 20% set and give you the accuracy. 

### Nonlinear Systems - Tantalus Cup Bifrucation Testing
Nonlinear Systems Code is from a final year module "Nonlinear Systems". The code is designed to replicate findings made in "Bifrucations in a simple hydraulic oscillator; The 'Tantalus' Cup" by Chialvo et al. (Eur. J. Phys. 12(1991) 297-302). The investigation is about a Tantalus cup (a cup that would empty itself if filled above a certain level) that is continuously filled and drained while, at certain intervals, will recieve an extra squirt of water. The program will look at the same circumstance in 3 different situations:
 - The first section simply replicates figure 5 in the paper which is how the water in the cup oscillates when no external stimulus is applied to the process (so not additional squirts of water) for consistent oscillations.
 - The second section works identical to the first but it will add the stimulus in at predetermined intervals.
 - The third section introduces the stimulus to replicate figure 6B from the paper by reproducing the bifrucation structure given. The function works by using a pair of ’for’ loops, one for stimulus amplitude and one for stimulus period. For each amplitude, from 0.001 to 1 in intervals of 0.001, a ’Devil’s Staircase’ graph of rotation numbers for each stimulus period from 1 to 100 is created, but not displayed. From this, the specific stimulus period at which each increase in rotation number occurred is recorded. When each amplitude has been tested, the results are plotted as a scatter graph, with each point representing a stimulus period at which the amplitude it corresponds to had an increase in rotation number.

### Space Dynamics
Space Dynamics was a module during my final year, focusing on respresenting the travel of celestial bodies or rockets/probes attempting to travel between them through Python or MATLAB attempting to use as many true physical qualities of the objects as possible to let python simulate the real events. Below are some codes I have used during the module and ones I have created on my own as thought exercises.

## Probe Moon
This code is a simpler one from the module. Based on a flare launcher sat on the moon that would shoot a flare directly upwards however the code will show what happens for the flare launcher that doesnt only shoot directly upwards and instead shoots at different angles of differing pi/12 radians. Showing trajectory and landing area.

## WE7
WE7 is about showing a probe travelling into a planet which eventually comes to land on the planet by aerobraking, a process of orbiting the planet until the gravity slowly pulls the probe in enough that the probe can make its own safe landing. It plots a graph that shows the specific trajectory of the probe as it aerobrakes.

## WE8

This project is a part of work in progress, working as an extension of part of the module I have persued in my own time and will endeavour to show a successful transfer orbit (where a rocket will travel from one planet in its orbit to another, specifically using the orbit trajectory and the planets gravity to successfully pull the rocket in) between Earth and Mars. This project is not finished but is updated as I move forward.
