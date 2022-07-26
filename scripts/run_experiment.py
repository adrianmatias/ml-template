from conf import Conf
from src.experiment import Experiment


def main():
    experiment = Experiment(conf=Conf(env="main"))
    experiment.run()


if __name__ == "__main__":
    main()
