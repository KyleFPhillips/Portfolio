# Portfolio
## About
Recent Maths graduate // Aspiring Data Analyst/Programmer

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

This portfolio contains elements of these modules plus some extra areas I have looked into, which include:

Final Year Project Code 1 & 2 are basic neural network systems used in my dissertation:

Code 1 is a basic feed forward network specifically avoiding using any additional machine learning libraries.

Code 2 is a form of NLP for sentiment analysis which trains itself to measure sentiment in a written form (the example used is in amazon reviews).

Nonlinear Systems Code is from a final year module "Nonlinear Systems". The code is designed to replicate findings made in "Bifrucations in a simple hydraulic oscillator; The 'Tantalus' Cup" by Chialvo et al. (Eur. J. Phys. 12(1991) 297-302). The investigation is about a Tantalus cup (a cup that would empty itself if filled above a certain level) that is continuously filled and drained while, at certain intervals, will recieve an extra squirt of water. The program will look at the same circumstance in 3 different situations:
 - The first section simply replicates figure 5 in the paper which is how the water in the cup oscillates when no external stimulus is applied to the process (so not additional squirts of water) for consistent oscillations while the second section adds the stimulus.
 - The third section introduces the stimulus to replicate figure 6B from the paper by reproducing the bifrucation structure given. The function works by using a pair of ’for’ loops, one for stimulus amplitude and one for stimulus period. For each amplitude, from 0.001 to 1 in intervals of 0.001, a ’Devil’s Staircase’ graph of rotation numbers for each stimulus period from 1 to 100 is created, but not displayed. From this, the specific stimulus period at which each increase in rotation number occurred is recorded. When each amplitude has been tested, the results are plotted as a scatter graph, with each point representing a stimulus period at which the amplitude it corresponds to had an increase in rotation number.

