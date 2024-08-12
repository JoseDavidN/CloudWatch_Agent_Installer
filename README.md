# CloudWatch Agent Installer

Este proyecto proporciona una solución para instalar el Amazon CloudWatch Agent en instancias EC2 de Linux y Windows. El programa automatiza la configuración y la instalación del agente en instancias EC2 utilizando Python.

## Características

- **Automatización de Instalación**: Instala CloudWatch Agent en instancias EC2 de Linux y Windows.
- **Compatibilidad con SSH y WinRM**: Utiliza conexiones SSH para Linux y WinRM para Windows.
- **Configuración Flexible**: Configura parámetros de instalación y credenciales mediante el archivo `config.py`.

## Requisitos

- **Python 3.x**: Asegúrate de tener Python 3.x instalado en tu máquina.
- **AWS Credentials**: Necesitas tener configuradas tus credenciales de AWS (clave de acceso y secreto).
- **Permisos**: Debes tener permisos para gestionar instancias EC2 en tu cuenta de AWS.
- **Dependencias**: Las dependencias están listadas en `requirements.txt`.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/cloudwatch-agent-installer.git
   cd cloudwatch-agent-installer
