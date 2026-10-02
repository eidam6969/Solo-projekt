import logging

# TODO: Vytvořte logger, handler, formatter a vypište zprávy →

logger = logging.getLogger("cviceni1")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logger.addHandler(handler)

logger.debug("Toto je DEBUG zpráva")
logger.info("Toto je INFO zpráva")
logger.warning("Toto je WARNING zpráva")
logger.error("Toto je ERROR zpráva")
logger.critical("Toto je CRITICAL zpráva")