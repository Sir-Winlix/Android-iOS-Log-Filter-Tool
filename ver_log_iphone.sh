#!/bin/bash

# Script para ver el log en tiempo real de un iPhone conectado a Arch Linux

# Aseguramos que libimobiledevice esté instalado
echo "Verificando si libimobiledevice está instalado..."
if ! pacman -Qi libimobiledevice &>/dev/null; then
    echo "libimobiledevice no está instalado. Instalando..."
    sudo pacman -S --noconfirm libimobiledevice
else
    echo "libimobiledevice ya está instalado."
fi

# Verificamos si el iPhone está conectado
echo "Comprobando si el iPhone está conectado..."
if ! idevice_id -l &>/dev/null; then
    echo "No se detecta ningún iPhone conectado. Asegúrate de que tu dispositivo esté desbloqueado y correctamente conectado."
    exit 1
fi

# Preguntamos si el usuario quiere guardar el log
echo "¿Quieres guardar los logs en un archivo? (S/N)"
read -r respuesta

# Si la respuesta es 'S' o 's', preguntamos por el nombre del archivo
if [[ "$respuesta" =~ ^[Ss]$ ]]; then
    # Obtenemos la fecha y hora actual
    fecha=$(date +"%Y-%m-%d_%H-%M-%S")
    archivo="log_iphone_$fecha.txt"  # Nombre del archivo con la fecha y hora
    echo "Guardando los logs en el archivo: $archivo"

    # Usamos idevicesyslog para obtener los logs en tiempo real y guardarlos en el archivo
    idevicesyslog > "$archivo" &
    echo "Los logs están siendo guardados en $archivo"
else
    # Si no se quiere guardar el log, solo mostramos los logs en tiempo real
    echo "Mostrando los logs en tiempo real..."
    idevicesyslog
fi
