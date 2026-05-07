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
accuracy = 0.7460
f1_score = 0.7449
```

This configuration was selected because it produced the highest held-out
evaluation accuracy among the MLflow runs. The first phase of training reached
about 0.682 accuracy, while adding the second training phase increased accuracy
to 0.746 and passed the 0.70 deployment gate.

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
After the DVC-tracked continuous-training update, `train_phase1.csv` contained
5996 samples and the model passed the gate with 0.746 accuracy.
