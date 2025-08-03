# 🧩 ml_orchestrator

The `ml_orchestrator` module serves as the central coordinator that connects all other modular components of a machine learning pipeline. It orchestrates the end-to-end workflow including data loading, preprocessing, training, evaluation, prediction, and explanation.

---

## 🚀 Features

- Integrates modular components:
  - `ml_data_loader`
  - `ml_preprocessor`
  - `ml_trainer`
  - `ml_evaluator`
  - `ml_predictor`
  - `ml_explainer`
- Manages pipeline execution with a simple `run_pipeline()` function
- Easily extensible for batch or streaming jobs
- Built for professional-grade ML system reuse

---

## 📦 Installation

From source:

```bash
pip install -e .
