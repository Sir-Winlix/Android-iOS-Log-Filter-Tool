#!/bin/python3

#####################################
#                                   #
#  @author      : pedro Javier      #
#    GitHub    : @Sir-winlix       #
#    Developer : PedroJSp92        #
#  﫥  Copyright : PedroJSp92        #
#                                   #
#####################################
#####################################
import re

def filter_battery_events(input_file, output_file):
    pattern = r"battery|power|charge|low power|Energy"
    
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line, re.IGNORECASE):
                out.write(line)
    
    print(f"Battery events guardados en {output_file}")

# Uso
filter_battery_events("iphone_logs.txt", "battery_events_filtered.txt")
