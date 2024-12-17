# Class Schedule Optimization using Genetic Algorithms

## Problem Description

The task is to create an optimal class schedule that:
- Handles classes with different durations (1-2 hours) and priorities (scale 1-5)
- Considers student availability and preferences
- Minimizes scheduling conflicts
- Maximizes alignment with student preferences
- Efficiently balances schedule across time slots

## Features

- Real-time schedule visualization using Pygame
- Genetic Algorithm optimization
- Dynamic mutation rate adjustment
- Fitness history plotting
- Conflict detection and visualization
- Student preference consideration
- High-priority class scheduling

## Components

The project consists of three main Python files:

### 1. environment.py
- Defines the scheduling environment
- Handles visualization using Pygame
- Manages class and student data
- Implements schedule generation
- Displays:
  - Student preferences
  - Class assignments
  - Conflicts (in red)
  - High-priority classes (in blue)
  - Generation and fitness information

### 2. agent.py
- Implements the Student class for managing individual schedules
- Contains the Genetic Algorithm implementation:
  - Fitness calculation
  - Tournament selection
  - Crossover operations
  - Mutation operations
- Handles schedule optimization

### 3. run.py
- Main execution file
- Sets up optimization parameters
- Manages the genetic algorithm loop
- Handles visualization updates
- Generates fitness history plots

### Program Parameters
- Population Size: 50
- Mutation Rate: 0.1
- Number of Generations: 100
- Visualization Delay: 1000ms

### Visualization Guide
- Blue Cells: High-priority classes (P1, P2)
- Red Cells: Scheduling conflicts
- Gray Cells: Normal assignments
- Left Panel: Student preferences
- Right Panel: Generation and fitness information

## Output Interpretation

- Current Fitness: Score of the currently displayed schedule
- Best Fitness: Highest fitness score achieved
- Generation: Current generation number
- Preferences: Individual student preferences (0.5-1.5)
- Conflicts: Shown in red, indicating scheduling issues

## Implementation Details

### Genetic Algorithm
- Uses tournament selection for parent selection
- Implements single-point crossover
- Features dynamic mutation rate adjustment
- Includes elitism to preserve best solutions

### Fitness Function
1. Conflict Minimization:
   - Penalizes assignments to unavailable slots
   - Penalizes duplicate class assignments

2. Preference Alignment:
   - Rewards schedules matching student preferences
   - Considers class priorities in scoring

3. Schedule Balance:
   - Promotes even distribution of classes
   - Prioritizes high-priority classes in preferred slots

## Contributing

This project is part of the Artificial Intelligence (CSE 366) course. Contributions should follow the project requirements and maintain code quality standards.

## Criteria of code

1. Correctness 
   - Conflict minimization
   - Preference alignment
   - Clear visualization

2. Optimization
   - Fitness improvement
   - Priority scheduling
   - Efficient time slot usage

3. Code Quality
   - Modular design
   - Documentation
   - Clean code practices

## License

This project is an academic assignment for CSE 366 course section 6(TR) at East west university.

## Acknowledgments

Course Instructor: Dr. Mohammad Rifat Ahmmad Rashid