from loguru import logger as log


def hello(name: str) -> str:
    '''This is a wonderful hello function!'''
    log.debug(name)
    return f"Hello from {name}!"
