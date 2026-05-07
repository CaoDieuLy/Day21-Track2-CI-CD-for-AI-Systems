# MLOps Lab Report

Repository: https://github.com/CaoDieuLy/Day21-Track2-CI-CD-for-AI-Systems

## Best Hyperparameters

Best local result after continuous training:

```yaml
model_type: random_forest
n_estimators: 300
max_depth:
min_samples_split: 2
```

Evaluation result:

```text
accuracy = 0.7480
f1_score = 0.7472
```

This configuration was selected because it produced the highest held-out
evaluation accuracy among the MLflow and CI runs. The first phase of training
reached about 0.682 accuracy, while continuous-training data updates increased
accuracy to 0.748 and passed the 0.70 deployment gate.

## Difficulties And Solutions

Python 3.13 caused dependency build issues for `scikit-learn==1.4.2`, so the
environment was recreated with Python 3.12.

The Windows shell had permission issues with some temporary folders and gcloud
configuration paths. The solution was to use the project-local `.gcloud`
configuration directory and run test/deployment commands with explicit paths.

The GCE VM initially rejected SSH for the `admin` user because of a Linux user
name conflict. A dedicated `mlops` user and SSH deploy key were configured
instead.

The first model trained only on `train_phase1.csv` did not pass the 0.70 gate.
After the DVC-tracked continuous-training updates, `train_phase1.csv` contained
6156 samples and the model passed the gate with 0.748 accuracy.
