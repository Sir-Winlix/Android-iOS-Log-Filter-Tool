import os
import re
import csv
import json

# Función para generar el reporte en CSV
def generate_csv_report(logs_directory, output_file):
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Fecha', 'Evento', 'Detalles'])

        # Recorrer todas las subcarpetas dentro de Logs/
        for subdir, _, files in os.walk(logs_directory):
            for file in files:
                log_file_path = os.path.join(subdir, file)
                with open(log_file_path, 'r') as infile:
                    for line in infile:
                        match = re.match(r"^(\w+ \d+ \d{2}:\d{2}:\d{2}) (.*)", line)
                        if match:
                            date = match.group(1)
                            event_details = match.group(2)
                            writer.writerow([date, event_details, event_details])

    print(f"Reporte CSV generado exitosamente: {output_file}")

# Función para generar el reporte en JSON
def generate_json_report(logs_directory, output_file):
    logs = []

    # Recorrer todas las subcarpetas dentro de Logs/
    for subdir, _, files in os.walk(logs_directory):
        for file in files:
            log_file_path = os.path.join(subdir, file)
            with open(log_file_path, 'r') as infile:
                for line in infile:
                    match = re.match(r"^(\w+ \d+ \d{2}:\d{2}:\d{2}) (.*)", line)
                    if match:
                        date = match.group(1)
                        event_details = match.group(2)
                        event = {
                            'Fecha': date,
                            'Evento': event_details,
                            'Detalles': event_details
                        }
                        logs.append(event)

    # Guardar los logs en el archivo JSON
    with open(output_file, 'w') as outfile:
        json.dump(logs, outfile, indent=4)

    print(f"Reporte JSON generado exitosamente: {output_file}")

# Ejecutar la función con los parámetros adecuados
logs_directory = 'Logs/'  # Carpeta donde se encuentran los logs
output_csv = 'reporte_logs.csv'
output_json = 'reporte_logs.json'

# Elegir si generar CSV o JSON
#generate_csv_report(logs_directory, output_csv)  # Para CSV
generate_json_report(logs_directory, output_json)  # Para JSON
