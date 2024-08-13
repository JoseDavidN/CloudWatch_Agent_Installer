import os
from dotenv import load_dotenv

load_dotenv()

# Configuracion de AWS
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Configuracion de CloudWatch Agent
CLOUDWATCH_AGENT_VERSION = "latest"
LINUX_INSTALL_COMMAND = "curl https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb -o amazon-cloudwatch-agent.deb && sudo dpkg -i -E amazon-cloudwatch-agent.deb"
LINUX_PERMISSIONS_COMMAND = "sudo rm amazon-cloudwatch-agent.deb && sudo chmod o+w /opt/aws/amazon-cloudwatch-agent/etc/"
LINUX_INIT_AGENT_COMMAND = "sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json -s"
WINDOWS_INSTALL_COMMAND = ""

# Configuracion de SSH
SSH_USER = os.getenv("SSH_USER")
SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")

# Configuracion de WinRM
WINRM_USER = os.getenv("WINRM_USER", "Administrator")
WINRM_PASSWORD = os.getenv("WINRM_PASSWORD", "password")

# Configuracion de archivos
LOCALE_PATH = "assets/agent_config.json"
REMOTE_PATH = "/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json"

# Configuraciones adicionales
LOG_FILE_PATH = "/var/log/cloudwatch-agent-installer.log"