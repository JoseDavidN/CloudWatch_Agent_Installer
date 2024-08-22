import os
import sys

# Agregar la subcarpeta al path para que sea posible importar desde ella
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CloudWatch_Agent_Installer'))

# Importar el archivo principal desde la subcarpeta
from main import main

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
