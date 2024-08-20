import json
from config import REMOTE_PATH_LINUX, REMOTE_PATH_WINDOWS

def send_json_linux(ssh, json_path):
    """
    Envia un archivo JSON a una instancia EC2.
    """
    sftp = ssh.open_sftp()

    sftp.put(json_path, REMOTE_PATH_LINUX)

    sftp.close()

    if sftp:
        return True
    else:
        return False

def send_json_windows(session, json_path):
    """
    Envia un archivo JSON a una instancia EC2.
    """

    with open(json_path, "r") as file:
        data = json.load(file)
    
    json_string = json.dumps(data)

    command = f"Set-Content -Path '{REMOTE_PATH_WINDOWS}' -Value '{json_string}' -Force"
    result = session.run_ps(command)

    if result.status_code == 0:
        print("Archivo JSON enviado con éxito")
        print("Output: ", result.std_out.decode())
    else:
        print("Error al enviar archivo JSON")
        print("Output: ", result.std_err.decode())