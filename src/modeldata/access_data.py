"""Provides basic data loading functionality.

Available functions:
- available_datasets: Lists all available data sets provided by modeldata.
- load_dataset: Load a data set of interest.
"""

import os
import glob
from typing import List
from pandas import read_csv
from pandas import DataFrame
from pkg_resources import resource_filename


def available_datasets() -> List[str]:
    """
    List all available data sets

    Returns
    -------
    Names of all available data sets.
    """
    path = os.path.join(os.path.dirname(__file__), "data")
    os.chdir(path)
    available_csv_files = glob.glob('*.csv')
    available_datasets = [os.path.splitext(file)[0] for file in available_csv_files]
    return available_datasets


def load_dataset(name: str) -> DataFrame:
    """
    Load a data set of interest

    Parameters:
        name (str): Name of data set. See `available_datasets()` for options.

    Returns:
        DataFrame: Pandas DataFrame
    """
    return read_csv(resource_filename("modeldata", f"data/{name}.csv"))
