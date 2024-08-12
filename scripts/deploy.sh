#!/bin/bash

# Configuración
EC2_USER="ec2-user"                 # Usuario de la instancia EC2
EC2_HOST="ec2-xx-xxx-xxx-xxx.compute-1.amazonaws.com"  # Dirección de la instancia EC2
LOCAL_INSTALLER_PATH="./cloudwatch_agent_installer"     # Ruta local del instalador
REMOTE_INSTALLER_PATH="/home/ec2-user/cloudwatch_agent_installer"  # Ruta remota en la instancia EC2

# Copiar el instalador a la instancia EC2
echo "Copiando archivos al servidor EC2..."
scp -r $LOCAL_INSTALLER_PATH $EC2_USER@$EC2_HOST:$REMOTE_INSTALLER_PATH

# Ejecutar el instalador en la instancia EC2
echo "Ejecutando el instalador en el servidor EC2..."
ssh $EC2_USER@$EC2_HOST << 'ENDSSH'
    cd /home/ec2-user/cloudwatch_agent_installer
    # Ejecutar el instalador (puedes ajustar los comandos según sea necesario)
    python3 cloudwatch_agent_installer/main.py
ENDSSH

echo "Despliegue completado."
