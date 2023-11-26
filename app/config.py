import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

BUILDS_FILE_PATH = os.environ.get("BUILDS_FILE_PATH", default=BASE_DIR.parent / "builds/builds.yaml")
TASKS_FILE_PATH = os.environ.get("TASKS_FILE_PATH", default=BASE_DIR.parent / "builds/tasks.yaml")
