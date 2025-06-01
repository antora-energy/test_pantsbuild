from loguru import logger as log


def hello(name: str):
    print(name)
    return f"Hello from {name}!"
