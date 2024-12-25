import os
from pathlib import Path

project_name = "ccc_0.0.1"

path_list = [
    ".github/workflows/main.yaml",
    "config/config.yaml",
    "notebook/stage_01_data_ingestion.py",
    "notebook/stage_02_data_transformation.py",
    "notebook/stage_03_model_training.py",
    "notebook/stage_04_model_evaluation.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data/__init__.py",
    f"src/{project_name}/components/data/ingestion.py",
    f"src/{project_name}/components/data/transformation.py",
    f"src/{project_name}/components/model/__init__.py",
    f"src/{project_name}/components/model/training.py",
    f"src/{project_name}/components/model/evaluation.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    "templates/index.html",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore"
]

for filepath in path_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)):
        with open(filepath, "w") as f:
            pass
    
print("""
Task completed !!!!!! 👌
""")
