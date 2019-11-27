import pandas as pd
from logging import getLogger

logger = getLogger(__name__)

# checking missing data
def missing_data(df):
    logger.debug('inspecting missing values')
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
    missing_data_df  = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    logger.debug('inspecting missing values complete')
    return missing_data_df
