import logging
import os
from typing import Dict

import lightgbm

from conf import Conf
from src.data import DataSplit, read_data


class Experiment:
    def __init__(self, conf: Conf):
        self.split_dict: Dict[str, DataSplit] = {}
        self.model = lightgbm.LGBMRanker(objective="lambdarank", metric="ndcg")
        self.path_data_raw = conf.path_data_raw
        logging.info(f"init with attributes: {self.__dict__}")

    def run(self):
        self.load_data()
        self.train()

    def load_data(self):
        for name, filename in [
            ("train", "train.txt"),
            ("valid", "vali.txt"),
            ("test", "test.txt"),
        ]:
            self.split_dict[name] = read_data(
                path_filename=os.path.join(self.path_data_raw, filename)
            )

    def train(self):

        train = self.split_dict["train"]
        valid = self.split_dict["valid"]

        self.model.fit(
            X=train.data,
            y=train.labels,
            group=train.qids_count,
            eval_set=[(valid.data, valid.labels)],
            eval_group=[valid.qids_count],
            eval_at=10,
            verbose=10,
        )

    def evaluate(self) -> float:
        return self.model.best_score_
