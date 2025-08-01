from setuptools import setup, find_packages

setup(
    name='ml_orchestrator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'joblib'
    ],
    author='Ruslan Mamedov',
    description='Pipeline orchestrator module for modular ML system',
)
