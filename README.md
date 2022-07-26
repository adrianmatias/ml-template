ml-template
==============================

Starter code for Machine Learning projects

## Data


### Passage ranking dataset
This passage dataset is based on the public MS MARCO dataset, although our evaluation will be quite different. We will use a different set of test queries and we will use relevance judges to evaluate the quality of passage rankings in much more detail.


https://microsoft.github.io/msmarco/Datasets.html#passage-ranking-dataset

### Wider context
### msmarco: Datasets for Document and Passage Ranking Leadboards
MS MARCO (MicroSoft MAchine Reading COmprehension) is a large-scale dataset focused on machine reading comprehension. Since its initial release, benchmarking efforts for several NLP and IR tasks have made use of this dataset—incl. question-answering, passage ranking, document ranking, keyphrase extraction, and conversational search.


## Reproducibility

Is recommended to use `conda` for managing dependencies:

- Install `conda` if needed: https://docs.conda.io/en/latest/miniconda.html
```
conda env create -f environment.yaml
```

## Code formatting and test 

```
pre-commit install
pre-commit run --all-files
```

## Test

```
pytest -vv
```

## Run experiment
```
cd scripts
python run_experiment.py
```

