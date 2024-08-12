#!/bin/bash

# Actualizar la lista de paquetes
echo "Actualizando la lista de paquetes..."
sudo apt-get update

# Instalar dependencias básicas
echo "Instalando dependencias básicas..."
sudo apt-get install -y python3 python3-pip

# Instalar dependencias del proyecto
echo "Instalando dependencias del proyecto..."
pip3 install -r /home/ec2-user/cloudwatch_agent_installer/requirements.txt

echo "Instalación completada."
