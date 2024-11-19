#!/bin/python3

#####################################
#                                   #
#  @author      : pedro Javier      #
#    GitHub    : @Sir-winlix       #
#    Developer : PedroJSp92        #
#  﫥  Copyright : PedroJSp92        #
#                                   #
#####################################
#####################################4
import os
import datetime

# Función para obtener la fecha actual en formato YYYY-MM-DD_HH-MM-SS
def get_date_str():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Función para crear la carpeta de Logs y subcarpetas de eventos
def create_log_directories():
    # Creamos la carpeta Logs si no existe
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    # Diccionario con los filtros y sus nombres de subcarpetas
    filters = {
        "network_events": "NetworkEvents",
        "location_events": "LocationEvents",
        "camera_events": "CameraEvents",
        "app_crashes": "AppCrashes",
        "battery_events": "BatteryEvents",
        "system_events": "SystemEvents",
        "app_specific_events": "AppSpecificEvents",
        "touch_events": "TouchEvents"
    }

    # Creamos las subcarpetas correspondientes
    for folder_name in filters.values():
        folder_path = os.path.join('Logs', folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def run_all_filters(input_file):
    # Obtenemos la fecha actual para agregarla al nombre de los archivos
    date_str = get_date_str()

    # Creamos la carpeta Logs y las subcarpetas de eventos
    create_log_directories()

    filters = [
        ("filter_network_events", f"Logs/NetworkEvents/network_events_filtered_{date_str}.txt"),
        ("filter_location_events", f"Logs/LocationEvents/location_events_filtered_{date_str}.txt"),
        ("filter_camera_events", f"Logs/CameraEvents/camera_events_filtered_{date_str}.txt"),
        ("filter_app_crashes", f"Logs/AppCrashes/app_crashes_filtered_{date_str}.txt"),
        ("filter_battery_events", f"Logs/BatteryEvents/battery_events_filtered_{date_str}.txt"),
        ("filter_system_events", f"Logs/SystemEvents/system_events_filtered_{date_str}.txt"),
        ("filter_app_specific_events", f"Logs/AppSpecificEvents/app_specific_events_filtered_{date_str}.txt", "Safari"),
        ("filter_touch_events", f"Logs/TouchEvents/touch_events_filtered_{date_str}.txt")
    ]
    
    # Ejecutamos cada filtro
    for filter_name, output_file, *args in filters:
        module = __import__(filter_name)
        if args:
            module.__dict__[filter_name](input_file, output_file, *args)
        else:
            module.__dict__[filter_name](input_file, output_file)

# Uso
run_all_filters("iphone_logs.txt")

