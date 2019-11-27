import pandas as pd
from logging import getLogger

logger = getLogger(__name__)

def load_data(path):
    logger.debug("Loading")
    df = pd.read_csv(path)
    logger.debug("Loading Done")
    return df

def write_data(path):
    logger.debug("Loading")
    df.write_csv(path)
    logger.debug("Loading Done")
    return