"""
Converts LOB data (prices, quotes) to images e.g. matrices indexed
by price and time with "pixel" values of quantities. The quantities
are normalized to be [0, 255] on the RGB spectrum.
"""

__author__ = "Justin Skillman"
__email__ = "jskillma@cmu.edu"

import numpy as np
import pandas as pd
import sys
import os
import tqdm

# Read  in Data
data_dir = './data/'
filename = 'test_lob.csv'

lob = pd.read_csv(data_dir + filename)
