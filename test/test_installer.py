import unittest
from CloudWatch_agent_Installer.installer import install_linux, install_windows

class TestInstaller(unittest.TestCase):
    def test_install_linux(self):
        # test para la instalacion en linux
        result = install_linux("i-1234567890abcdef0")
        self.assertEqual(result, "Instalando CloudWatch Agent en la instancia Linux i-1234567890abcdef0")
        self.assertTrue(result, "Fallo instalacion de CloudWatch Agent en la instancia Linux i-1234567890abcdef0")

    def test_install_windows(self):
        # Test para la instalacion en windows
        result = install_windows("i-1234567890abcdef0")
        self.assertEqual(result, "Instalando CloudWatch Agent en la instancia Windows i-1234567890abcdef0")
        self.assertTrue(result, "Fallo instalacion de CloudWatch Agent en la instancia Windows i-1234567890abcdef0")

if __name__ == "__main__":
    unittest.main()
