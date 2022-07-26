import logging

import numpy as np
from numpy import ndarray
from pandas import Series
from sklearn.datasets import load_svmlight_file

from src.static_conf import StaticConf as sconf


class DataSplit:
    def __init__(
        self, data: ndarray, labels: ndarray, qids: ndarray, qids_count: ndarray
    ):
        self.data = data
        self.labels = labels
        self.qids = qids
        self.qids_count = qids_count


def read_data(path_filename) -> DataSplit:
    logging.info(f"read_data: {path_filename}")

    data, labels, qids = load_svmlight_file(
        path_filename, query_id=True, n_features=sconf.n_feats
    )
    return DataSplit(
        data=np.array(data.todense()),
        labels=labels.reshape(-1, 1),
        qids=qids,
        qids_count=get_count(qids=qids),
    )


def get_count(qids: ndarray) -> ndarray:
    return Series(qids).value_counts(sort=False).to_numpy()
