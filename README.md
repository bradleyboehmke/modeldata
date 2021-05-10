<!-- badges: start -->
![](https://img.shields.io/badge/version-0.1.0-blue.svg)
[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![tests](https://github.com/bradleyboehmke/modeldata/actions/workflows/package-ci.yaml/badge.svg)](https://github.com/bradleyboehmke/modeldata/actions)
<!-- badges: end -->

`modeldata` contains various data sets useful for teaching machine learning. The package serves as a sister package to the R [`modeldata`](https://github.com/tidymodels/modeldata) package and is designed to make comparisons across languages easily accessible.

## Installation

Get up and running with modeldata with:

```bash
pip install git+https://github.com/bradleyboehmke/modeldata.git
```

## Basic Usage

You can see all available data sets with:

```python
>>> from modeldata import available_datasets

>>> available_datasets()
['ad_data',
 'ames',
 'attrition',
 'biomass',
 'car_prices',
 'cells',
 'check_times',
 'chicago',
 'concrete',
 'covers',
 'credit_data',
 'crickets',
 'drinks',
 'hpc_cv',
 'hpc_data',
 'lending_club',
 'meats',
 'mlc_churn',
 'oils',
 'okc',
 'okc_text',
 'parabolic',
 'pathology',
 'pd_speech',
 'penguins',
 'sacramento',
 'scat',
 'smithsonian',
 'solubility_test',
 'stackoverflow',
 'two_class_dat',
 'two_class_example',
 'wa_churn']
```

And you can load any of these data sets as a Pandas DataFrame with:

```python
>>> from modeldata import load_dataset

>>> ames = load_dataset('ames')
>>> type(ames)
pandas.core.frame.DataFrame

>>> ames.shape
(2930, 74)
```

## Bugs & Enhancements

Your feedback allows us to make better tools. Please report any problems, bugs, or ideas for enhancement. You can report issues [here](https://github.com/bradleyboehmke/modeldata/issues).
