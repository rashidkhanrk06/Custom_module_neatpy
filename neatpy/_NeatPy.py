import re
import pandas as pd
import string

"""
NeatPy: A Python module for data cleaning operations.

This module provides functions for cleaning and transforming data in pandas Series.

Functions:
- to_integer(series: pd.Series, dtype=float) -> pd.Series:
  Convert a pandas Series of strings to integers with a specified data type.

- to_text(series: pd.Series, punct=True, keep=None, keep_num=None) -> pd.Series:
  Remove digits and/or punctuation from a pandas Series of strings with optional preservation of specified characters.

- to_specialChr(series: pd.Series) -> pd.Series:
  Remove alphanumeric characters from a pandas Series of strings.

Usage:
>>> import neatpy 
>>> data = pd.Series(['123.45', '456.78', '789.0'])
>>> result = NeatPy.to_integer(data, dtype=int)
>>> print(result)
0    123
1    456
2    789
dtype: int32

>>> data = pd.Series(['Hello, 123!', 'World456', 'Python'])
>>> result = NeatPy.to_text(data, punct=True, keep=['o', '5'], keep_num=2)
>>> print(result)
0    Holle
1    Wrd
2    Python
dtype: object

>>> data = pd.Series(['Hello123', 'World456', 'Python'])
>>> result = NeatPy.to_specialChr(data)
>>> print(result)
0     #
1     #
2    Python
dtype: object
"""

__all__ = ['to_integer', 'to_text', 'to_specialChr']

def to_integer(series:pd.Series, dtype=float)-> pd.Series:
    """
    Convert a pandas Series of strings to integers with a specified data type.

    Parameters:
    - series (pd.Series): A pandas Series containing strings.
    - dtype (type, optional): The data type to which the converted values will be cast. Default is float.

    Returns:
    - pd.Series: A new pandas Series with non-digit characters removed and values converted to the specified data type.

    Example:
    >>> data = pd.Series(['123.45', '456.78', '789.0'])
    >>> result = to_integer(data, dtype=int)
    >>> print(result)
    0    123
    1    456
    2    789
    dtype: int32
    """
    
    return series.str.replace('\D','', regex=True).astype(dtype)

def to_text(series:pd.Series,punct=True,keep=None,keep_num = None) -> pd.Series:
    """
    Remove digits and/or punctuation from a pandas Series of strings with optional preservation of specified characters.

    Parameters:
    - series (pd.Series): A pandas Series containing strings.
    - punct (bool, optional): If True, remove punctuation along with digits. Default is True.
    - keep (str or list, optional): Characters to preserve during the removal process. Can be a string or a list of strings.
    - keep_num (int or list, optional): Numbers to preserve during the removal process. Can be an integer or a list of integers.

    Returns:
    - pd.Series: A new pandas Series with digits and/or punctuation removed, while preserving specified characters.

    Example:
    >>> data = pd.Series(['Hello, 123!', 'World456', 'Python'])
    >>> result = to_text(data, punct=True, keep=['o', '5'], keep_num=2)
    >>> print(result)
    0    Holle
    1    Wrd
    2    Python
    dtype: object
    """
    numbers = '0123456789'
    punctuation = string.punctuation
    if keep:
        if isinstance(keep, str):
            punctuation = punctuation.replace(keep, '')
        elif isinstance(keep, list):
            for keep_str in keep:
                punctuation = punctuation.replace(keep_str, '')

    if keep_num:
        if isinstance(keep_num, int):
                numbers = numbers.replace(str(keep_num), '')
        elif isinstance(keep_num, list):
            for num in keep_num:
                numbers = numbers.replace(str(num), '')
   
    punct_numbers = punctuation + numbers if punct else numbers
    return series.apply(lambda x:x.translate(str.maketrans('','',punct_numbers)))


def to_specialChr(series:pd.Series)-> pd.Series:
    """
    Remove alphanumeric characters from a pandas Series of strings.

    Parameters:
    - series (pd.Series): A pandas Series containing strings.

    Returns:
    - pd.Series: A new pandas Series with alphanumeric characters removed.

    Example:
    >>> data = pd.Series(['Hello123', 'World456', 'Python'])
    >>> result = to_specialChar(data)
    >>> print(result)
    0     #
    1     #
    2    Python
    dtype: object
    """
    pattern = re.compile('[a-z0-9]',flags=re.IGNORECASE)
    return series.apply(lambda x: re.sub(pattern, '', x)) 