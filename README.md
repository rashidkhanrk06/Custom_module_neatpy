# neatpy

neatpy is a Python module designed for data cleaning operations. It provides functions for cleaning and transforming data in pandas Series. The module includes functions to convert strings to integers, remove digits and/or punctuation from strings, and remove alphanumeric characters from strings.

## Installation

To install NeatPy, you can use pip:

```bash
pip install git+https://github.com/rashidkhanrk06/neatpy.git

```
## Usage

```bash
import pandas as pd
import neatpy 

# Example 1: Convert strings to integers
data = pd.Series(['123.45', '456.78', '789.0'])
result = neatpy.to_integer(data, dtype=int)
print(result)

# Example 2: Remove digits and/or punctuation
data = pd.Series(['Hello, 123!', 'World456', 'Python'])
result = neatpy.to_text(data, punct=True, keep=['o', '5'], keep_num=2)
print(result)

# Example 3: Remove alphanumeric characters
data = pd.Series(['Hello123', 'World456', 'Python'])
result = neatpy.to_specialChr(data)
print(result)

```

## License
This project is licensed under the MIT License - see the LICENSE file for details.