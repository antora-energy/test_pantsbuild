from loguru import logger as log


def hello(name: str) -> str:
    log.debug(name)
    return f"Hello from {name}!"
