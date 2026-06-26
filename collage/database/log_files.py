import logging

logging.basicConfig(
    filename="app_log.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("user logged in")
logging.warning("someone is trying brout fource!")
logging.debug("issue is risen by user")
logging.error("server crashed")
logging.critical("data is compramised")

print("!done")