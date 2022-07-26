import os

from conf import Conf
from src.data import read_data
from src.static_conf import StaticConf as sconf

CONF = Conf(env="test")


def test_df_true():
    data_split = read_data(
        path_filename=os.path.join(CONF.path_data_raw, "train.txt")
    )

    data_length = 1000

    assert data_split.data.shape == (data_length, sconf.n_feats)
    assert data_split.labels.shape == (data_length, 1)
    assert len(data_split.qids) == data_length
    assert sum(data_split.qids_count) == data_length

    n_qid = len(set(data_split.qids))
    assert len(data_split.qids_count) == n_qid
