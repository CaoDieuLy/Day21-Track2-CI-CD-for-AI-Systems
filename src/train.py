import mlflow
import mlflow.sklearn
import pandas as pd
import yaml
import json
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

EVAL_THRESHOLD = 0.70


def _build_model(params: dict):
    model_type = params.get("model_type", "random_forest")
    model_params = {k: v for k, v in params.items() if k != "model_type"}

    if model_type == "random_forest":
        return RandomForestClassifier(**model_params, random_state=42)
    if model_type == "gradient_boosting":
        return GradientBoostingClassifier(**model_params, random_state=42)
    if model_type == "logistic_regression":
        return make_pipeline(
            StandardScaler(),
            LogisticRegression(**model_params, random_state=42),
        )

    raise ValueError(f"Unsupported model_type: {model_type}")


def _write_report(y_true, preds, label_distribution: dict, acc: float, f1: float):
    labels = [0, 1, 2]
    matrix = confusion_matrix(y_true, preds, labels=labels)
    precision, recall, class_f1, support = precision_recall_fscore_support(
        y_true,
        preds,
        labels=labels,
        zero_division=0,
    )

    lines = [
        "Model performance report",
        f"accuracy: {acc:.4f}",
        f"f1_score_weighted: {f1:.4f}",
        "",
        "Training label distribution:",
    ]
    for label in labels:
        ratio = label_distribution.get(str(label), 0.0)
        warning = " WARNING: below 10%" if ratio < 0.10 else ""
        lines.append(f"class {label}: {ratio:.4f}{warning}")

    lines.extend(["", "Confusion matrix:", str(matrix), "", "Per-class metrics:"])
    for idx, label in enumerate(labels):
        lines.append(
            "class "
            f"{label}: precision={precision[idx]:.4f}, "
            f"recall={recall[idx]:.4f}, "
            f"f1={class_f1[idx]:.4f}, "
            f"support={int(support[idx])}"
        )

    with open("outputs/report.txt", "w") as f:
        f.write("\n".join(lines) + "\n")


def train(
    params: dict,
    data_path: str = "data/train_phase1.csv",
    eval_path: str = "data/eval.csv",
) -> float:
    """
    Huan luyen mo hinh va ghi nhan ket qua vao MLflow.

    Tham so:
        params     : dict chua cac sieu tham so cho RandomForestClassifier.
        data_path  : duong dan den file du lieu huan luyen.
        eval_path  : duong dan den file du lieu danh gia.

    Tra ve:
        accuracy (float): do chinh xac tren tap danh gia.
    """

    df_train = pd.read_csv(data_path)
    df_eval = pd.read_csv(eval_path)

    X_train = df_train.drop(columns=["target"])
    y_train = df_train["target"]
    X_eval = df_eval.drop(columns=["target"])
    y_eval = df_eval["target"]

    with mlflow.start_run():
        mlflow.log_params(params)

        model = _build_model(params)
        model.fit(X_train, y_train)

        preds = model.predict(X_eval)
        acc = accuracy_score(y_eval, preds)
        f1 = f1_score(y_eval, preds, average="weighted")
        label_distribution = {
            str(label): float(ratio)
            for label, ratio in y_train.value_counts(normalize=True).sort_index().items()
        }

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)
        for label, ratio in label_distribution.items():
            mlflow.log_metric(f"train_label_ratio_{label}", ratio)
        mlflow.sklearn.log_model(model, "model")

        print(f"Accuracy: {acc:.4f} | F1: {f1:.4f}")
        for label in ["0", "1", "2"]:
            ratio = label_distribution.get(label, 0.0)
            if ratio < 0.10:
                print(f"WARNING: class {label} only has {ratio:.2%} of training data")

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/metrics.json", "w") as f:
            json.dump(
                {
                    "accuracy": acc,
                    "f1_score": f1,
                    "label_distribution": label_distribution,
                },
                f,
                indent=2,
            )
        _write_report(y_eval, preds, label_distribution, acc, f1)

        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/model.pkl")

    return float(acc)


if __name__ == "__main__":
    with open("params.yaml") as f:
        params = yaml.safe_load(f)
    train(params)
