import pandas as pd
from joblib import load

def run_pipeline(
    data_path: str,
    model_path: str,
    preprocessor_path: str = None,
):
    # Step 1: Load Data
    df = pd.read_csv(data_path)

    # Step 2: Preprocess (optional)
    if preprocessor_path:
        preprocessor = load(preprocessor_path)
        X = preprocessor.transform(df)
    else:
        X = df.values

    # Step 3: Predict
    model = load(model_path)
    predictions = model.predict(X)

    return predictions
