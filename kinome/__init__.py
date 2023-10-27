from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = PROJECT_ROOT / "datasets"

if __name__ == "__main__":
    print(PROJECT_ROOT)