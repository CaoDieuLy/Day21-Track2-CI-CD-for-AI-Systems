# Screenshot Checklist

Capture these screenshots in order for submission.

## 1. MLflow Or DagsHub Runs

Local MLflow option:

```powershell
$env:MLFLOW_TRACKING_URI="sqlite:///mlflow.db"
.\.venv\Scripts\mlflow.exe ui --backend-store-uri sqlite:///mlflow.db
```

Open:

```text
http://localhost:5000
```

Screenshot requirements:

- at least 3 runs visible
- `accuracy` visible
- `f1_score` visible
- different parameter values visible

DagsHub bonus option:

- open the DagsHub MLflow experiment page
- screenshot runs logged from GitHub Actions

## 2. GitHub Actions

Open:

```text
https://github.com/CaoDieuLy/Day21-Track2-CI-CD-for-AI-Systems/actions
```

Screenshot requirements:

- latest workflow run is green
- jobs visible: Unit Test, Train, Eval, Deploy
- for Step 3 evidence, the run should correspond to a commit that changed `data/train_phase1.csv.dvc`

## 3. API Output

Run:

```powershell
curl.exe http://34.133.240.174:8000/health
$body = @{ features = @(7.4, 0.70, 0.00, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4, 0) } | ConvertTo-Json
Invoke-RestMethod -Uri http://34.133.240.174:8000/predict -Method Post -ContentType 'application/json' -Body $body
```

Screenshot requirements:

- command and output visible
- `/health` returns `{"status":"ok"}`
- `/predict` returns a valid `prediction` and `label`

## 4. Cloud Storage

Open GCP Console Storage bucket:

```text
vin-mlops-lab-757312350-bucket
```

Screenshot requirements:

- `dvc/` folder visible
- `models/latest/model.pkl` visible
- `outputs/latest/metrics.json` visible
- `outputs/latest/report.txt` visible

## 5. Bonus Evidence

Screenshots that help show bonus completion:

- `BONUS.md`
- GitHub Actions Eval log showing previous/current accuracy comparison
- uploaded `outputs/report.txt` artifact
- DagsHub MLflow page if Bonus 1 secrets are configured
