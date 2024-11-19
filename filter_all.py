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
def filter_all(input_file):
    filters = [
        ("InCallService", r"InCallService.*", "filtered_incallservice.txt"),
        ("Audio Routing", r"AudioSession.*Route Changed|Bluetooth|Headset", "filtered_audio.txt"),
        ("XPC Connections", r"xpc_connection.*unknown service|peer connection", "filtered_xpc.txt"),
        ("System Errors", r"<Error>:.*", "filtered_errors.txt"),
    ]
    
    for name, pattern, output_file in filters:
        with open(input_file, "r") as logs, open(output_file, "w") as out:
            for line in logs:
                if re.search(pattern, line):
                    out.write(line)
        print(f"{name} filtrados y guardados en {output_file}")

# Uso
filter_all("iphone_logs.txt")
