import logging

LOG_FORMAT = "%(asctime)s----%(levelname)s-----%(message)s"
DATE_FORMAT = "%m-%d-%Y %p %H:%M:%S"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
#logging.basicConfig(level=logging.DEBUG, filename="my.log", format="%(asctime)s-%(levelname)s-%(message)s")

name = "Lily"
age = 18

logging.debug("This is a debug logs. name is {0} age is {1}".format(name, age))
logging.log(logging.INFO,"This is a info logs.", exc_info =True ,stack_info =False)
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")