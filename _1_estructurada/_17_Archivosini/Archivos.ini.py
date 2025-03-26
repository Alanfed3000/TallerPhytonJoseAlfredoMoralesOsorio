import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Verifica que las secciones y claves existan
    if ('Maximus' in config and
            'basedatos' in config['Maximus'] and
            'usuario' in config['Maximus'] and
            'contrasennia' in config['Maximus']):

        bd = config['Maximus']['basedatos']
        user = config['Maximus']['usuario']
        password = config['Maximus']['contrasennia']

        print(f"Base de datos: {bd}")
        print(f"Usuario: {user}")
        print(f"Contraseña: {password}")

    else:
        print("El archivo config.ini no contiene las secciones y claves necesarias.")