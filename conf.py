import os

import yaml


class Conf:
    def __init__(self, env="main"):
        self.env = env
        self.root_dir = os.path.dirname(os.path.abspath(__file__))

        self.filename = f"{self.root_dir}/conf/config_{env}.yaml"
        with open(self.filename) as f:
            conf_dict = yaml.load(f, Loader=yaml.FullLoader)

        self.path_data_raw = self.add_root_dir(conf_dict["path"]["data"]["raw"])

    def add_root_dir(self, path: str) -> str:
        return os.path.join(self.root_dir, path)
