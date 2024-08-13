import os
import paramiko
import winrm
from config import LINUX_INSTALL_COMMAND, LINUX_INIT_AGENT_COMMAND, LINUX_PERMISSIONS_COMMAND, WINDOWS_INSTALL_COMMAND, SSH_USER, SSH_KEY_PATH, WINRM_USER, WINRM_PASSWORD, LOCALE_PATH, REMOTE_PATH

def install_linux(instance):
    """
    Instala el agente de CloudWatch en una instancia Linux.
    """
    ip_address = instance.public_ip_address
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username=SSH_USER, key_filename=SSH_KEY_PATH)
    sftp = ssh.open_sftp()

    stdin, stdout, stderr = ssh.exec_command(LINUX_INSTALL_COMMAND)
    print(stdout.read().decode())
    print(stderr.read().decode())

    stdin, stdout, stderr = ssh.exec_command(LINUX_PERMISSIONS_COMMAND)
    print(stdout.read().decode())
    print(stderr.read().decode())

    path = os.path.join(os.path.dirname(__file__), LOCALE_PATH)

    sftp.put(path, REMOTE_PATH)

    sftp.close()

    stdin, stdout, stderr = ssh.exec_command(LINUX_INIT_AGENT_COMMAND)
    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()

def install_windows(instance):
    """
    Instala el agente de CloudWatch en una instancia Windows.
    """
    # ip_address = instance.public_ip_address
    # session = winrm.Session(f'http://{ip_address}:5985/wsman', auth=(WINRM_USER, WINRM_PASSWORD))
    # result = session.run_cmd(WINDOWS_INSTALL_COMMAND)
    # print(result.std_out.decode())
    # print(result.std_err.decode())
    pass