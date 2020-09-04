import os
from typing import Union

from sfaira.data import DatasetGroupBase


class DatasetGroupBrain(DatasetGroupBase):

    def __init__(
        self, 
        path: Union[str, None] = None,
        meta_path: Union[str, None] = None
    ):
        datasets = [
        ]
        keys = [x.id for x in datasets]
        self.datasets = dict(zip(keys, datasets))
