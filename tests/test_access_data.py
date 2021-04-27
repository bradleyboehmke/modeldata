"""Test data acess functionality."""
from modeldata import available_datasets
from modeldata import load_dataset
import os
import glob
from pandas import DataFrame
import pytest


def test_available_datasets():
    """All available datasets are listed."""
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'modeldata', 'data')
    os.chdir(path)
    available_csv_files = glob.glob('*.csv')
    actual_datasets = [os.path.splitext(file)[0] for file in available_csv_files]
    assert available_datasets() == actual_datasets


@pytest.mark.parametrize("dataset", available_datasets())
def test_load_data(dataset):
    df = load_dataset(dataset)
    assert type(df) == DataFrame
