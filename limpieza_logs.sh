#!/bin/bash

# Definir la ruta del entorno
LOG_DIR="/home/ec2-user/environment/DevOps-Proyecto"

echo "Iniciando limpieza de logs en $LOG_DIR a las $(date)"

# Opción A: Eliminar archivos que terminen en .log
# find $LOG_DIR -name "*.log" -type f -delete

# Opción B: Vaciar el contenido de los logs sin borrar el archivo (más seguro)
find $LOG_DIR -name "*.log" -type f -exec truncate -s 0 {} +

echo "Limpieza completada."