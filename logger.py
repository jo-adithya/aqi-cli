import logging


def setup_logger(verbose: bool):
    logging.basicConfig(
        level=logging.INFO if verbose else logging.WARN,
        format="{asctime} - [{levelname}] - {message}",
        style="{",
        datefmt="%H:%M",
    )
