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
def filter_incallservice(input_file, output_file):
    pattern = r"InCallService.*"
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line):
                out.write(line)
    print(f"Eventos relacionados con InCallService guardados en {output_file}")

# Uso
filter_incallservice("iphone_logs.txt", "filtered_incallservice.txt")
