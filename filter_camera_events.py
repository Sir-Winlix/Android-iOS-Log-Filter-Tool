
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

def filter_camera_events(input_file, output_file):
    pattern = r"camera|photo|video|media|AVCapture"
    
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line, re.IGNORECASE):
                out.write(line)
    
    print(f"Camera events guardados en {output_file}")

# Uso
filter_camera_events("iphone_logs.txt", "camera_events_filtered.txt")
