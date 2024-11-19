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

def filter_app_specific_events(input_file, output_file, app_name_pattern):
    pattern = rf"{app_name_pattern}"
    
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line, re.IGNORECASE):
                out.write(line)
    
    print(f"App specific events guardados en {output_file}")

# Uso para una app como Safari
filter_app_specific_events("iphone_logs.txt", "app_specific_events_filtered.txt", "Safari")
