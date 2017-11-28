###########
Amstelhaege
###########

This project is based on a case part of the course heuristics given on the University of Amsterdam. The objective is to find the highest value for a specific area named: 'Amstelhaege'. The Amstelhaege is filled with houses and the score is the sum of these houses. Using multiple alghoritms the score is calculated.  

Getting Started
===============

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system

Prerequisites
=============

Python:
    https://www.python.org/downloads/

Numpy:
    Numpy can be installed using pip install numpy. Numpy is used for its mathematical features
    
Matplotlib:
    Matplotlib can be installed using pip install matplotlib. Matplotlib is used to visualize the map
    
```
Give examples
```

Running the tests
=================

Go to the map 'run me' chose one of the alghoritms listed in this map and type in a terminal for example:

```
python hill_climber.py
```

Results
=======

Explain what these tests test and why

```
Give an example
```

Deployment
==========

Add additional notes about how to deploy this on a live system

Authors
=======
* Luc Stefelmanns
* Raoul Lieben
* Toon van Holthe tot Echten



Study:        Minor Programming, University of Amsterdam
Course:       Heuristics
Assignment:   Amstelhaege
Group:        726567756982776978
Members:      Toon van Holthe, Raoul Lieben, Luc Stefelmanns

Archive/
    Contains all old scripts that may obtain valuable lines of code. Temporary backup location.

Scripts/
    algorithms.py
        All algorithms to places houses and water on the map.
    case.py
        Dictionaries containing the characteristics of this case.
    classes.py
        All classes (Map, House, Water).
    functions.py
        Functions for the algorithms and score function (place_house, calc_freespace).
    run_me.py
        Actual script that runs everthing.
    test_l.py, test_r.py, test_t.py
        Individual scripts to test.
    visuals.py
        Functions to show results.

Texts/
    constraints.txt
        The constraints of the current case.
    IDEA_todo.txt
        Progress list, with initials if working on particular area and asterix of todo is finished.
    links.txt
        Possible useful links for the project.
