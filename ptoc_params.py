#parameters for ptoc project

curr_dir = '/user_data/csimmon2/git_repos/ptoc'

import os
import shutil
import sys
import numpy as np
import pandas as pd
sys.path.insert(0,curr_dir)
import subprocess
from glob import glob as glob
import pdb

runs = [1,2,3]
raw_dir = '/lab_data/behrmannlab/vlad/hemispace'
data_dir = '/lab_data/behrmannlab/vlad/ptoc'

sub_info = pd.read_csv(f'{curr_dir}/sub_info.csv')
