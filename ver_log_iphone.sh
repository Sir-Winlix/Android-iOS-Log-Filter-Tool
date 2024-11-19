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

# Si el dispositivo está conectado, mostramos los logs en tiempo real
echo "iPhone detectado. Mostrando logs en tiempo real..."

# Usamos ideviceconsole para obtener los logs en tiempo real
ideviceconsole --watch
