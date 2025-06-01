from loguru import logger as log


def hello(name: str):
    log.debug(name)
    return f"Hello from {name}!"
