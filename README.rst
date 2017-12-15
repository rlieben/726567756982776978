###########
Amstelhaege
###########

This project is based on a case part of the course Heuristics given at the University of Amsterdam. The objective is to find the highest value for a specific area named: 'Amstelhaege'. The Amstelhaege is filled with houses and the score is the sum of these houses. Using multiple alghoritms the score is calculated.  


Prerequisites
=============

* Python (3.6.3)

* Numpy (1.14)
    
* Matplotlib (2.1.0)

* Imageio (2.2.0)


How to run
=================

In a terminal type: 
```
RUNME.py <integer>
```

The integer ranges between 1 and 5.
The integers stand for :
    1. best of random
    2. greedy
    3. hillclimber
    4. force move
    5. simmulated annealing
    
Folder navigation
=======
    
    Algorithms/
        content:
            * best_of_random.py
            * greedy.py
            * hill_climber.py
            * force_move.py
            * simulated_annealing_hillclimber.py
        
        description:
            This folder contains all algorithms used to solve the case.


    Classes/
        content:
            * house.py
            * map.py
            * water.py
            
        description:
            This folder contains all classes used in the algorithms. The classes contain functions that for example calculate the free space for a house


    Results/
        content:
            * best_of_random
            * greedy
            * hillclimber
            * force_move
        
        description:    
            For each algorithm the results are saved in sub folders. These folders contain a GIF of the process and the total score (sum of all house values) is stored in data.txt


    Specifications/
        content: 
            * amstelhaege.py
        
        description:
            This folder contains the spefications used for this project like the Amstelhaege's width and height


    Visualisations/
        content:
            * coloured_map.py
            * make_gif.py
            * txtwriter.py
        
        description:
            This folder contains all scripts used to visualise and document the change in score during each iteration for every algorithm    
           
Authors
=======
* Toon van Holthe tot Echten
* Raoul Lieben
* Luc Stefelmanns





