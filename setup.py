from setuptools import setup, find_packages

# Configuration
setup(
    name = "cloudwatch_agent_installer",
    version = "0.1.0",
    author = "Jose David Gomez",
    author_email = "gomezjosedavid997@gmail.com",
    description = "Programa de instalacion de CloudWatch Agent para instancias de EC2 con linux y windows",
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = "",
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires = [
        'boto3',
        'paramiko',
        'pywinrm'
    ],
    entry_points = {
        'console_scripts': [
            'cwa-installer = cloudwatch_agent_installer.main:main',
        ],
    },
)