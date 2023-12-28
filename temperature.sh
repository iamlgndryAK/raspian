#!/bin/bash

# Store the temperature in a variable
temperature=$(sudo vcgencmd measure_temp)

# Display the temperature
echo "$temperature"
