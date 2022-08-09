
import sys
import os
from inspect import stack

sys.path.append(os.path.join(os.path.dirname(stack()[0][1]), "chem"))

from ptable import *
from еlement import Element
from сompound import Compound
