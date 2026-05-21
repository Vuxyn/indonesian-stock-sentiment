BASE_PATH = "/content/drive/MyDrive/indonesian-stock-sentiment"

GA_CONFIG = {
    "pop_size": 20,
    "generations": 10,
    "cx_prob": 0.7,
    "mut_prob": 0.2,
}

SPARK_CONFIG = {
    "executor_cores": "4",
    "executor_memory": "4g",
    "scheduler_mode": "FAIR",
}

MODEL_CONFIG = {
    "base_model": "indolem/indobert-base-uncased",
    "max_length": 128,
    "num_labels": 3,
}

LABEL_MAP = {
    "POSITIF": 0,
    "NEGATIF": 1,
    "NETRAL": 2,
}