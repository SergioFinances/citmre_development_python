import logging

from citmre.citmre_fun import rmre_data

logging.basicConfig(level=logging.INFO)

def main():
    logging.info(rmre_data())

if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')

    main()

    logging.debug('>>> Estamos finalizando la ejecución del paquete.')