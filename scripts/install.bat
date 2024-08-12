@echo off
REM Actualizar el sistema
echo Actualizando el sistema...
powershell -Command "Start-Process cmd.exe -ArgumentList '/c echo Updating system...' -Verb RunAs"

REM Instalar Python y pip si no están instalados
echo Verificando Python y pip...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python no encontrado. Instalando Python...
    REM Descargar e instalar Python (ajustar URL según la versión)
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe' -OutFile 'python_installer.exe'"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
)

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip no encontrado. Instalando pip...
    powershell -Command "Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile 'get-pip.py'"
    python get-pip.py
)

REM Instalar dependencias del proyecto
echo Instalando dependencias del proyecto...
pip install -r C:\path\to\cloudwatch_agent_installer\requirements.txt

echo Instalación completada.
pause
