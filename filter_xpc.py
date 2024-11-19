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
def filter_xpc_connections(input_file, output_file):
    pattern = r"xpc_connection.*unknown service|peer connection"
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line):
                out.write(line)
    print(f"Conexiones sospechosas guardadas en {output_file}")

# Uso
filter_xpc_connections("iphone_logs.txt", "filtered_xpc.txt")
