import io
import pandas as pd

from src.logger.logger import logger

def load_data(path):
    """
    Takes the location of the csv file and returns a dataframe of the csv file provided.

    Parameters:
        path: Location of your csv data file
    
    Returns:
        df: Dataframe of the loaded csv
    """
    try:
        df = pd.read_csv(path)

        logger.info(f"Successfully loaded data for file: {path}")
        return df
    except FileNotFoundError:
        logger.error(f"The file at {path} was not found")
    except Exception as err:
        logger.error(f"An unexcected error occured while loading {path} file: {err}")

def get_dataset_info(df):
    """
    Takes in a dataframe and returns its .info() in string.

    Parameters:
        df: A pandas DataFrame
    
    Returns:
        info_string: df.info() converted into string
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The parameter 'df' must be a pandas DataFrame")

        buffer = io.StringIO()
        df.info(buf=buffer)
        info_string = buffer.getvalue()

        logger.info(f"Successfully generated info_string")
        return info_string
    except Exception as err:
        logger.error(f"An unexpected error occured {err}")
    finally:
        if buffer is not None:
            buffer.close()