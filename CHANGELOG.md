# Changelog

Todas las notas de la versión importantes para este proyecto se documentan en este archivo. Las versiones se enumeran en orden descendente (las versiones más recientes están al principio).

## [0.2.3] - 2020-08-20
## Agregado
- Agregado ultilidad, funciones para la carga de configuracion json en sistemas linux y windows

## Corregido
- Actualizacion de dependiencias
- Se corrigio la funcion de instalacion para windows
- Modificacion en el archivo `config.py`
- Modificacion en la configuracion json del agente para windows

## [0.2.2] - 2020-08-15
## Agregado
- Agregado archivo de configuracion JSON para agente en windows
- Comandos para descargar e instalar el agente cloudwatch en windows
- Archivo de test para conexion remota a windows

## Corregido
- Se cambio el nombre de `agent_config.json` por `agent_config_linux.json`
- Se modifico la funcion de install en linux (minimizar codigo)
- Se corrigieron unos parametros en el `setup.py`
- Corregida la funcion que se conecta he instala el agente cloudwacth

## [0.2.1] - 2020-08-13
## Correccion
- Se corrigio el archivo `setup.py`

## [0.2.0] - 2020-08-13
## Agregado
- se agrego comando de descarga y instalacion del agente.
- Se agrego comando para otorgar permisos de escritura en la carpeta etc de amazon-cloudwatch-agent.
- se agrego comando para iniciar el agente.
- se agrego test de conexion ssh.
- se agrego plantilla `agent_config.JSON` con configuracion para metricas.
  
## Corregido
- se corrigio la conexion a instancias linux.
- se corrigio sintaxis en la documentacion.
- se corrigio test de instalacion.
- se corrigio el archivo `.gitignore` para excluir una carpeta mas
- se corrigio la funcion de instalacion en linux del archivo `installer.py`
  
## Quitado
- se quito el archivo `utils.py`.

## [0.1.1] - 2024-08-12
## Agregado
- se anexo archivo '.env.example' con las plantillas de las variables de entorno.

## Corregido
- Se corrigio el archivo 'README.md' junto a los archivos `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` actualizando la informacion.

## [0.1.0] - 2024-08-12
### Agregado
- Estructura básica del proyecto y archivos iniciales.
- Configuración de entorno y dependencias iniciales.

## [0.0.1] - 2024-08-12
### Inicial
- Creación del repositorio y configuración inicial del proyecto.