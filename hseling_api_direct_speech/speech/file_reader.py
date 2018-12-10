# -*- coding: utf-8 -*-
from .step import PipelineStep
import re

class FileReader(PipelineStep):
    
    def __init__(self):
        pass
    
    def annotate(self, text):
        return self.__delete_newlines(text)

    
    def __delete_newlines(self, text):
        text1 = re.sub(' +', ' ', text)
        text2 = re.sub(r'\n(?P<cap> [а-яё])', r'\g<cap>', text1)
        text3 = re.sub(r'(?P<punc>[^!\?\.\:])\n', r'\g<punc>', text2)
        text4 = re.sub('[  ]+', ' ', text3)
        return text4
