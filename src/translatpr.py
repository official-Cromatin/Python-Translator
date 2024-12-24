import logging
from typing import overload, Literal
from pathlib import Path
from dataclasses import dataclass

@dataclass
class MISSING:
    pass

class Translator:
    """
    Class to create language dynamic applications based on json files.

    Author: official-Cromatin
    Source: https://github.com/official-Cromatin/Python-Translator
    Version: V3.0
    """
