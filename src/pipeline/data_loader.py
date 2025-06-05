import io
import pandas as pd

def load_data(path):
    """
    Takes the location of the csv file and returns a dataframe of the csv file provided.

    Parameters:
        path: Location of your csv data file
    
    Returns:
        df: Dataframe of the loaded csv
    """
    df = pd.read_csv(path)
    return df

def get_dataset_info(df):
    """
    Takes in a dataframe and returns its .info() in string.
    """
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_string = buffer.getvalue()
    buffer.close()
    print("TYPE:", type(info_string))
    return info_string