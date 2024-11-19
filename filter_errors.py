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
def filter_errors(input_file, output_file):
    pattern = r"<Error>:.*"
    with open(input_file, "r") as logs, open(output_file, "w") as out:
        for line in logs:
            if re.search(pattern, line):
                out.write(line)
    print(f"Errores encontrados guardados en {output_file}")

# Uso
filter_errors("iphone_logs.txt", "filtered_errors.txt")
