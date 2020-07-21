import logging

logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(levelname)s:%(lineno)s] %(message)s',
                   datefmt='%I%M%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])

logging.warning('Mensaje a nivel warning')
logging.info('Mensaje a nivel info')
logging.debug('Mensaje a nivel debug')
logging.error('Ocurrió un error en la base de datos')
logging.debug('Se realizó la conexión con éxito')