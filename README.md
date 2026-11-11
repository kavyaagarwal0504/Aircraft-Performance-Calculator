# Aircraft-Performance-Calculator

## Project Overview

The **Aircraft Performance Calculator** is a Python-based project that
performs basic aircraft performance calculations and presents the
results using graphs. The program accepts aircraft and atmospheric
parameters from the user, calculates important aerodynamic and
performance values, and runs simplified simulations of takeoff and
flight-path behaviour.

## Objectives

-   Calculate basic aircraft performance parameters using user-provided
    inputs.
-   Determine aircraft weight, lift, drag, stall speed, wing loading,
    thrust-to-weight ratio, and lift-to-drag ratio.
-   Estimate takeoff speed from the calculated stall speed.
-   Simulate changes in aircraft velocity, acceleration, lift, and drag
    over time.
-   Study how aircraft mass, engine thrust, wing area, and air density
    affect performance.
-   Model simplified changes in lift and drag with angle of attack.
-   Simulate a basic takeoff sequence and a simplified flight path.
-   Display calculated results through graphs for easier interpretation.

## Features

-   Interactive command-line input for aircraft parameters.
-   Basic aerodynamic calculations.
-   Lift and drag variation with velocity.
-   Estimated stall and takeoff speeds.
-   Simplified takeoff acceleration simulation.
-   Parameter sensitivity plots for mass, thrust, wing area, and air
    density.
-   Simplified angle-of-attack model and lift-to-drag analysis.
-   Basic takeoff and flight-path simulations.
-   Final aircraft performance summary printed in the terminal.

## Requirements

### Python libraries

-   `numpy` --- used for numerical calculations and generating
    simulation ranges.
-   `matplotlib` --- used to create the performance graphs.

### Create a virtual environment

**Windows:**

``` bash
py -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install the required libraries

Run:

``` bash
python -m pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, you can install the
libraries directly:

``` bash
python -m pip install numpy matplotlib
```

## How to Execute the Program

1.  Open the project folder in Visual Studio Code or another Python IDE.
2.  Open `aircraft_performance_calculator_complete.py`.
3.  Open the integrated terminal in the same folder.
4.  Run the program:

``` bash
python aircraft_performance_calculator_complete.py
```

On some Windows installations, use:

``` bash
py aircraft_performance_calculator_complete.py
```

5.  Enter the requested values when prompted. The program asks for:
    -   Aircraft mass (kg)
    -   Wing area (m²)
    -   Lift coefficient (CL)
    -   Drag coefficient (CD)
    -   Maximum lift coefficient (CLmax)
    -   Engine thrust (N)
    -   Aircraft velocity (m/s)
    -   Air density (kg/m³)
6.  After entering the values, read the calculated performance results
    in the terminal.
7.  Matplotlib graph windows will appear during execution. Close each
    graph window to allow the program to continue to the next graph.
8.  Review the final aircraft performance report printed in the
    terminal.

