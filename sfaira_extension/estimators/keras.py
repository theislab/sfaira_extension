from sfaira.estimators import EstimatorKeras, EstimatorKerasEmbedding, EstimatorKerasCelltype
from typing import Union
import anndata
import numpy as np


class EstimatorKerasEmbeddingExtended(EstimatorKerasEmbedding):
    def __init__(
            self,
            data: Union[anndata.AnnData, np.ndarray],
            model_dir: Union[str, None],
            model_id: Union[str, None],
            species: Union[str, None],
            organ: Union[str, None],
            model_type: Union[str, None],
            model_topology: Union[str, None],
            weights_md5: Union[str, None] = None,
            cache_path: str = 'cache/'
    ):
        super(EstimatorKerasEmbeddingExtended, self).__init__(
            data=data,
            model_dir=model_dir,
            model_id=model_id,
            species=species,
            organ=organ,
            model_type=model_type,
            model_topology=model_topology,
            weights_md5=weights_md5,
            cache_path=cache_path
        )


class EstimatorKerasCelltypeExtended(EstimatorKerasCelltype):
    def __init__(
            self,
            data: Union[anndata.AnnData, np.ndarray],
            model_dir: Union[str, None],
            model_id: Union[str, None],
            species: Union[str, None],
            organ: Union[str, None],
            model_type: Union[str, None],
            model_topology: Union[str, None],
            weights_md5: Union[str, None] = None,
            cache_path: str = 'cache/',
            max_class_weight: float = 1e3
    ):
        super(EstimatorKerasCelltypeExtended, self).__init__(
            data=data,
            model_dir=model_dir,
            model_id=model_id,
            species=species,
            organ=organ,
            model_type=model_type,
            model_topology=model_topology,
            weights_md5=weights_md5,
            cache_path=cache_path,
            max_class_weight=max_class_weight
        )
