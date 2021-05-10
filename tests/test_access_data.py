"""Test data acess functionality."""
import glob
import os

import pytest
from modeldata import available_datasets
from modeldata import load_dataset
from pandas import DataFrame


def test_available_datasets():
    """All available datasets are listed."""
    path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "src", "modeldata", "data"
    )
    os.chdir(path)
    available_csv_files = glob.glob("*.csv")
    actual_datasets = sorted(
        [os.path.splitext(file)[0] for file in available_csv_files]
    )
    assert available_datasets() == actual_datasets


@pytest.mark.parametrize("dataset", available_datasets())
def test_load_data(dataset):
    """Loading datasets returns a DataFrame"""
    df = load_dataset(dataset)
    assert type(df) == DataFrame
