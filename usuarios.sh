#!/bin/bash

# 1. Crear el usuario devops_user (sin password para fines del lab)
echo "Creando usuario devops_user..."
sudo useradd devops_user

# 2. Crear un grupo para el proyecto y añadir al usuario
sudo groupadd devops_group
sudo usermod -aG devops_group devops_user

# 3. (Simulación de asignación) Dar permisos al nuevo usuario sobre el entorno
# Esto es lo que normalmente causaría el bloqueo
sudo chown -R devops_user:devops_group ~/environment/DevOps-Proyecto

echo "Permisos transferidos temporalmente a devops_user."

# 4. RESTAURAR PERMISOS (Punto crítico solicitado)
# Devolvemos la propiedad al usuario ec2-user para que el IDE siga funcionando
echo "Restaurando permisos para ec2-user..."
sudo chown -R ec2-user:ec2-user ~/environment/DevOps-Proyecto

echo "Gestión de usuarios y permisos completada con éxito."