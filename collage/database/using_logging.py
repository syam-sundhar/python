import logging
logging.basicConfig(filename='app.log',level=logging.INFO)


logging.info("Program started")
logging.warning("Low memory")
logging.error("Error occured")