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

def filter_audio_routing(input_file, output_file):
    pattern = r"AudioSession.*Route Changed|Bluetooth|Headset"
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line):
                out.write(line)
    print(f"Eventos relacionados con redirección de audio guardados en {output_file}")

# Uso
filter_audio_routing("iphone_logs.txt", "filtered_audio.txt")
