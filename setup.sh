#!/bin/bash

# 1. Actualizar el gestor de paquetes
sudo yum update -y 

# 2. Asegurar que Python3 y Pip estén instalados
sudo yum install -y git vim docker python3 python3-pip
sudo service docker start

# 3. Instalar dependencias(boto3 y otras necesarias)
echo "Instalando dependencias..."
pip3 install boto3

# 4. Verificar instalaciones
echo "-----------------------------------"
python3 --version
pip3 show boto3 | grep Version
echo "Configuración completada con éxito."