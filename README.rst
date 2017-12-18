###########
Amstelhaege
###########

This project is based on a case part of the course Heuristics given at the University of Amsterdam. The objective is to find the highest value for a specific area named: 'Amstelhaege'. The Amstelhaege is filled with houses and water. The score is the sum of these houses. Using multiple alghoritms the score is calculated.  


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
requirements.py
```

When all packages have been installed, in a terminal type:

```
RUNME.py
```

A pair of questions will be asked:

```
Enter number of houses (20, 40 or 60): 
```

Answer which map you would like to use. The maps can be found in Specifications/amstelhaege.py. If you would like to make your own map, you can do this as long as it contains the same information as these maps do. Be warned, MAP_40 and MAP_60 can take considerable time to complete for most of the algorithms.

```
Enter algorithm of your choice:
```

Answer which algorithm you would like to use. The algorithms can be found in Algorithms/ (except helpers.py).

```
Enter number of iterations: 
```

Answer how many iterations you would like the chosen algorithm to run. Be warned, some algorithms (greedy.py, hillclimber with heuristic) take a lot of time to process, so few iterations are advised for these.


    
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
            For each algorithm the results are saved in sub folders. These folders contain a GIF of the process and the total score (sum of all house values) is stored in data.txt. Furthermore a plot figure is showing the increase of the score.


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
            * plot_data.py
        
        description:
            This folder contains all scripts used to visualise and document the change in score during each iteration for every algorithm    
           
Authors
=======
* Toon van Holthe tot Echten
* Raoul Lieben
* Luc Stefelmanns





