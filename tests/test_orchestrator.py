import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from joblib import dump
from ml_orchestrator.orchestrator import run_pipeline

def test_run_pipeline(tmp_path):
    # Prepare dummy data
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df_path = tmp_path / "data.csv"
    df.to_csv(df_path, index=False)

    # Train and save dummy model
    model = LogisticRegression()
    model.fit(iris.data, iris.target)
    model_path = tmp_path / "model.joblib"
    dump(model, model_path)

    # Run orchestrator
    preds = run_pipeline(str(df_path), str(model_path))

    assert len(preds) == len(df)
