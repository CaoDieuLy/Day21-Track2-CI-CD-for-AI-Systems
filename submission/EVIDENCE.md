# Submission Evidence

## Repository

```text
https://github.com/CaoDieuLy/Day21-Track2-CI-CD-for-AI-Systems
```

## VM API

Public VM IP:

```text
34.134.253.171
```

Health:

```json
{"status":"ok"}
```

Predict:

```json
{
  "prediction": 0,
  "label": "thap"
}
```

## MLflow Runs

Top local MLflow runs:

```text
accuracy,f1_score,params
0.746,0.7449481408322124,model_type=random_forest n_estimators=300 max_depth=None min_samples_split=2
0.746,0.7449481408322124,model_type=random_forest n_estimators=300 max_depth=None min_samples_split=2
0.682,0.6810790629331478,model_type=random_forest n_estimators=300 max_depth=None min_samples_split=2
0.682,0.6810790629331478,n_estimators=300 max_depth=None min_samples_split=2
0.682,0.6806135013922618,n_estimators=800 max_depth=20 min_samples_split=2 max_features=log2
0.676,0.6748089375284998,n_estimators=500 max_depth=None min_samples_split=2
0.644,0.6416822593730938,n_estimators=200 max_depth=10 min_samples_split=5
0.564,0.5533560988979983,n_estimators=100 max_depth=5 min_samples_split=2
```

## Cloud Storage

Bucket:

```text
gs://vin-mlops-lab-757312350-bucket
```

Objects:

```text
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/58/53e7711c78f02286e65fca6cb6e124
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/64/53f2f5cac61359410969b8708a1b22
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/6b/364476204c84eed29c25061ede898b
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/b1/1de6b7adaa93a44278fd7e168b2288
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/e7/d8293d8d3f387490a0103bab0104ab
gs://vin-mlops-lab-757312350-bucket/dvc/files/md5/fd/073d6651b2ff224c0da1eb1c049a32
gs://vin-mlops-lab-757312350-bucket/models/latest/model.pkl
gs://vin-mlops-lab-757312350-bucket/outputs/latest/metrics.json
gs://vin-mlops-lab-757312350-bucket/outputs/latest/report.txt
```

## Latest Metrics

```json
{
  "accuracy": 0.748,
  "f1_score": 0.7472470244898887,
  "label_distribution": {
    "0": 0.36630929174788823,
    "1": 0.43810916179337234,
    "2": 0.19558154645873943
  }
}
```

## GitHub Actions

Latest successful full pipeline:

```text
Run: https://github.com/CaoDieuLy/Day21-Track2-CI-CD-for-AI-Systems/actions/runs/25510435090
Commit: 2922a82651b603032f9022f5f2ce3a04bda1d9c0
Jobs: Unit Test, Train, Eval, Deploy all success
Artifact: model-outputs
```

Continuous-training data commits:

```text
e7ed636 data: trigger continuous training update
83931c1 data: add step 3 continuous training sample
2922a82 data: final step 3 trigger sample
ad48f0b data: mark step 3 continuous trigger metadata
```

## Bonus Status

```text
Bonus 1: Remote MLflow tracking configured through DagsHub secrets.
Bonus 2: Multiple algorithms supported through model_type.
Bonus 3: Automated report written to outputs/report.txt and uploaded as artifact.
Bonus 4: Rollback guard compares new accuracy against deployed metrics in GCS.
Bonus 5: Label distribution is logged and saved in metrics.json.
```

Note: the workflow supports DagsHub MLflow tracking through
`MLFLOW_TRACKING_URI`, `MLFLOW_TRACKING_USERNAME`, and
`MLFLOW_TRACKING_PASSWORD` secrets. Those secrets must point to a real DagsHub
repo/token for remote DagsHub evidence.

## CI/CD Cloud Auth

GitHub Actions is configured to authenticate to GCP through Workload Identity
Federation:

```text
projects/141571983280/locations/global/workloadIdentityPools/github-pool/providers/github-provider
mlops-lab-sa@vin-mlops-lab-757312350.iam.gserviceaccount.com
```
