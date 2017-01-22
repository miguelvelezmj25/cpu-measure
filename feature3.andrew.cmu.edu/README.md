# Feature 3

The data collected and analyzed in this folder is from the **Feature3** server at Carnegie Mellon University.

    hostname: feature3.andrew.cmu.edu
    hardware: Intel(R) Core(TM) i5-4250U CPU @ 1.30GHz with SSD drive

## Measurement Protocol

For idle, and 1 or more executions of the Java program, we started measuring the data immediately for about 2 minutes. 
For the experiments where the Java program slept for an interval, we waited about 10 minutes for the CPU utilization to 
stabilize and then started recording data for about 2 minutes. Multiple executions of the Java program in this repo were 
executed to have multiple threads running the program. 

## Data

The power data for this machine is located in this 
[repository](https://github.com/cmuvariability/brass/tree/master/turtlebot/power_scripts/wemo_monitor_EB3/feature3.andrew.cmu.edu).
This same repo contains the script used to analyze and get the model in this folder.