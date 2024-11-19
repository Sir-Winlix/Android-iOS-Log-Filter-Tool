# **Android/iOS Log Filter Tool**

Este proyecto proporciona herramientas para obtener, filtrar y organizar los logs de dispositivos **iOS** y **Android** en carpetas específicas, permitiendo el análisis de eventos como llamadas, red, ubicación, batería, entre otros.

### **Estructura del Proyecto:**
LogFilterTool/
├── Filtros/
│   ├── filter_audio.py        # Filtro para eventos relacionados con audio
│   ├── filter_network.py      # Filtro para eventos relacionados con la red
│   ├── filter_location.py     # Filtro para eventos relacionados con la ubicación
│   ├── filter_camera.py       # Filtro para eventos relacionados con la cámara
│   ├── filter_app_crashes.py  # Filtro para eventos relacionados con los fallos de aplicaciones
│   ├── filter_battery.py      # Filtro para eventos relacionados con la batería
│   ├── filter_system.py       # Filtro para eventos del sistema
│   ├── filter_app_specific.py # Filtro para eventos específicos de aplicaciones (por ejemplo, Chrome)
│   └── filter_touch.py        # Filtro para eventos relacionados con las interacciones táctiles
├── run_all_filters_ios.py     # Script para ejecutar todos los filtros sobre logs de iOS
├── run_all_filters_android.py # Script para ejecutar todos los filtros sobre logs de Android
└── README.md                  # Documentación del proyecto


El **Android/iOS Log Filter Tool** está diseñado para facilitar el análisis de los logs generados por dispositivos móviles. Los logs pueden ser capturados mediante herramientas como `adb logcat` en Android y `idevicesyslog` en iOS. Este proyecto permite la aplicación de varios filtros para extraer eventos específicos, como:

- Eventos de **audio**
- Eventos de **red** (conexión, desconexión, etc.)
- **Ubicación** del dispositivo
- **Cámara**
- **Fallos de aplicaciones**
- **Batería** (uso y estadísticas)
- **Sistema** (cambios de estado del sistema)
- **Eventos específicos de aplicaciones** (por ejemplo, Chrome)
- **Táctiles** (interacciones táctiles)

### **Requisitos:**

- **Python 3.6+**
- **`adb`** para Android: [Instalar ADB](https://developer.android.com/studio/command-line/adb)
- **`libimobiledevice`** para iOS: [Instalar libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)
- **`idevicesyslog`** para iOS: [Instalar idevicesyslog](https://github.com/libimobiledevice/libimobiledevice/wiki)

### **Cómo Usar:**

#### 1. **Para Android:**
   
   1. Habilita la depuración USB en tu dispositivo Android.
   2. Conecta tu dispositivo Android a tu PC y asegúrate de que `adb` esté funcionando correctamente.
   3. Ejecuta el siguiente script para capturar y filtrar los logs:
      ```bash
      python3 run_all_filters_android.py
      ```

   Esto creará una carpeta `Logs/` con subcarpetas para cada tipo de evento, y los logs filtrados serán guardados allí.

#### 2. **Para iOS:**

   1. Instala y configura `libimobiledevice` y `idevicesyslog` para acceder a los logs del dispositivo.
   2. Conecta tu dispositivo iOS y asegúrate de que los logs se estén generando correctamente.
   3. Ejecuta el siguiente script para capturar y filtrar los logs:
      ```bash
      python3 run_all_filters_ios.py
      ```

   Al igual que en Android, se creará una carpeta `Logs/` con subcarpetas para cada tipo de evento y los logs filtrados se guardarán en las respectivas carpetas.

### **Archivos Principales:**

- **Filtros:**
  - `filter_audio.py`: Filtra los eventos relacionados con audio.
  - `filter_network.py`: Filtra los eventos relacionados con la red.
  - `filter_location.py`: Filtra los eventos relacionados con la ubicación.
  - `filter_camera.py`: Filtra los eventos relacionados con la cámara.
  - `filter_app_crashes.py`: Filtra los eventos relacionados con fallos de aplicaciones.
  - `filter_battery.py`: Filtra los eventos relacionados con el uso de la batería.
  - `filter_system.py`: Filtra los eventos del sistema.
  - `filter_app_specific.py`: Filtra eventos específicos de aplicaciones.
  - `filter_touch.py`: Filtra los eventos táctiles.

- **Scripts para ejecutar los filtros:**
  - `run_all_filters_ios.py`: Ejecuta todos los filtros en los logs de iOS.
  - `run_all_filters_android.py`: Ejecuta todos los filtros en los logs de Android.

### **Ejemplo de Salida:**

Después de ejecutar los filtros, se generarán archivos de log organizados en carpetas bajo `Logs/`. Ejemplo:



