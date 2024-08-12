import os

# Configuracion de AWS
AWS_REGION = os.environ.get("AWS_REGION", "us-east-2")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Configuracion de CloudWatch Agent
CLOUDWATCH_AGENT_VERSION = "latest"
LINUX_INSTALL_COMMAND = ""
WINDOWS_INSTALL_COMMAND = ""

# Configuracion de SSH
SSH_USER = os.environ.get("SSH_USER", "ubuntu")
SSH_KEY_PATH = os.environ.get("SSH_KEY_PATH")

# Configuracion de WinRM
WINRM_USER = os.environ.get("WINRM_USER", "Administrator")
WINRM_PASSWORD = os.environ.get("WINRM_PASSWORD", "password")

# Configuraciones adicionales
LOG_FILE_PATH = "/var/log/cloudwatch-agent-installer.log"