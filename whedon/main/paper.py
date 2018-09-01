# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/whedon-python

from whedon.logger import bot
from whedon.utils import read_yaml
from typing import List
from enum import Enum
import os
import re
import sys
  
class Journal(Enum):
    joss = 'joss'
    rse = 'rse'

class Author:
    '''an Author holds a name, orcid id, and affiliation'''
    def __init__(self, 
                 name: str, 
                 orcid: str, 
                 affiliation: str):

        self.name = name


class Paper:

    def __init__(self, filename):

        self._check_inputs(filename)
        self.metadata = read_yaml(filename)

    def __str__(self):
        return "<paper.md: %s>" % self.filename

    def __repr__(self):
        return self.__str__()

    def _check_inputs(self, filename):
        '''check to make sure that filename exists
           Parameters
           ==========
           filename: the markdown file to parse
        '''
        if not os.path.exists(filename):
            bot.exit('Cannot find %s' % filename)
        self.filename = os.path.abspath(os.path.realpath(filename))


    def get(self, key, quiet=True, sep=',', field=None):
        '''return a key from the yaml, default is silent (no print) if doesn't
           exist. If the yaml item is a list with different subfields, then
           field must also be defined.
        '''
        if key in self.metadata:
    
            value = self.metadata[key]

            if isinstance(value, (tuple, list)):

                # If the first entry is a dict
                if isinstance(value[0], dict):
                    values = []

                    for entry in value:
                        if field in entry:
                            if entry[field]:
                                values.append(entry[field])
                    value = values

                print(sep.join(value))
            else:
                print(self.metadata[key])
