import yaml
import logging
from pathlib import Path

from ml_data_loader.loader import load_data
from ml_preprocessor import Preprocessor
from ml_trainer import Trainer
from ml_evaluator import Evaluator
from ml_predictor import Predictor

class PipelineOrchestrator:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.logger = self._init_logger()

        self.preprocessor = Preprocessor()
        self.trainer = Trainer()
        self.evaluator = Evaluator()
        self.predictor = Predictor()

        self.logger.info("PipelineOrchestrator initialized.")

    def _load_config(self, path: str) -> dict:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        return config

    def _init_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("PipelineOrchestrator")

    def run(self):
        try:
            self.logger.info("🔹 Loading data...")
            df = load_data(**self.config["load"])

            self.logger.info("🔹 Preprocessing data...")
            X_train, X_test, y_train, y_test = self.preprocessor.process(df, **self.config["preprocess"])

            self.logger.info("🔹 Training model...")
            model = self.trainer.train(X_train, y_train, **self.config["train"])

            self.logger.info("🔹 Evaluating model...")
            metrics = self.evaluator.evaluate(model, X_test, y_test, **self.config.get("evaluate", {}))
            self.logger.info(f"✅ Evaluation results: {metrics}")

            self.logger.info("🔹 Making predictions...")
            preds = self.predictor.predict(model, X_test)

            # Optional: call to explainer
            if hasattr(self, "explainer") and self.explainer:
                self.logger.info("🔹 Explaining predictions...")
                self.explainer.explain(model, X_test)

            self.logger.info("✅ Pipeline execution completed successfully.")

        except Exception as e:
            self.logger.exception(f"❌ Pipeline failed: {e}")
            raise
