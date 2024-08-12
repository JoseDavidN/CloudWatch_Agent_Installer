import paramiko
import winrm
from config import LINUX_INSTALL_COMMAND, WINDOWS_INSTALL_COMMAND, SSH_USER, SSH_KEY_PATH, WINRM_USER, WINRM_PASSWORD

def install_linux(instance):
    """
    Instala el agente de CloudWatch en una instancia Linux.
    """
    ip_address = instance.public_ip_address
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username=SSH_USER, key_filename=SSH_KEY_PATH)

    stdin, stdout, stderr = ssh.exec_command(LINUX_INSTALL_COMMAND)
    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()

def install_windows(instance):
    """
    Instala el agente de CloudWatch en una instancia Windows.
    """
    ip_address = instance.public_ip_address
    session = winrm.Session(f'http://{ip_address}:5985/wsman', auth=(WINRM_USER, WINRM_PASSWORD))
    result = session.run_cmd(WINDOWS_INSTALL_COMMAND)
    print(result.std_out.decode())
    print(result.std_err.decode())