# Bonus Implementation Notes

This repo implements all five bonus tasks.

## Bonus 1: Remote MLflow Tracking With DagsHub

The GitHub Actions training job supports remote MLflow tracking. Add these
repository secrets after connecting the GitHub repo to DagsHub:

```text
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo>.mlflow
MLFLOW_TRACKING_USERNAME=<dagshub-username>
MLFLOW_TRACKING_PASSWORD=<dagshub-token>
```

If `MLFLOW_TRACKING_URI` is not set, the workflow falls back to
`sqlite:///mlflow.db` so local development still works.

## Bonus 2: Multiple Algorithms

`params.yaml` contains `model_type`. `src/train.py` supports:

- `random_forest`
- `gradient_boosting`
- `logistic_regression`

## Bonus 3: Automated Performance Report

`src/train.py` writes `outputs/report.txt` with:

- confusion matrix
- precision, recall, and f1 per class
- training label distribution

GitHub Actions uploads the report together with `metrics.json` and
`model.pkl`.

## Bonus 4: Rollback Guard

The Eval job reads `outputs/latest/metrics.json` from Cloud Storage. If the new
accuracy is lower than the currently deployed accuracy, the pipeline stops
before deployment.

## Bonus 5: Label Distribution Warning

`src/train.py` computes training label distribution, stores it in
`outputs/metrics.json`, logs it to MLflow, and prints a warning if any class is
below 10 percent of the training set.
