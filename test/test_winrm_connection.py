import winrm
import unittest
import os
from dotenv import load_dotenv

load_dotenv()

class TestWinrmConnection(unittest.TestCase):

    def setUp(self):
        # Configura los detalles de la conexión SSH
        self.hostname = "18.222.31.225"
        self.username = os.getenv("WINDOWS_USER")
        self.user_password = os.getenv("WINDOWS_PASSWORD")

    def test_connection_windows(self):
        try:
            session = winrm.Session(f'http://{self.hostname}:5985/wsman', auth=(self.username, self.user_password), transport='ntlm')
            result = session.run_ps('ipconfig')
            print(result.status_code)
            print(result.std_out.decode())
            print(result.std_err.decode())
            self.assertTrue(True)
        except Exception as e:
            print(f"Error al establecer conexión WinRM: {e}")
            self.fail("La conexión WinRM falló " + self.user_password)

if __name__ == "__main__":
    unittest.main()
