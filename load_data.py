
import os
import pandas as pd


# Exact dataset path
DATA_PATH = (
    r"D:\2 nd year\ML\Skill Math\Project"
    r"\WA_Fn-UseC_-HR-Employee-Attrition.csv"
)


def load_data(path=DATA_PATH):
    """Load the employee attrition dataset."""

    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    return pd.read_csv(path)


def get_dataset_info():
    """Return dataset information for the web application."""

    df = load_data()

    return {
        "dataset_name": os.path.basename(DATA_PATH),
        "rows": df.shape[0],
        "columns": df.shape[1],
        "n_rows": df.shape[0],
        "n_cols": df.shape[1],
        "column_names": list(df.columns),

        "column_info": [
            {
                "name": col,
                "dtype": str(df[col].dtype),
                "missing": int(df[col].isnull().sum())
            }
            for col in df.columns
        ],

        "dtypes": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },

        "missing_counts": {
            col: int(df[col].isnull().sum())
            for col in df.columns
        },

        "preview": df.head(10).to_html(
            classes="table preview-table",
            index=False
        )
    }


def get_data_summary(df: pd.DataFrame) -> dict:
    """Return a summary of a DataFrame."""

    return {
        "n_rows": df.shape[0],
        "n_cols": df.shape[1],
        "columns": list(df.columns),

        "dtypes": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },

        "missing_counts": {
            col: int(df[col].isnull().sum())
            for col in df.columns
        },

        "preview": df.head(10).to_dict(
            orient="records"
        )
    }


if __name__ == "__main__":
    try:
        df = load_data()
        print("Dataset loaded successfully!")
        print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(get_data_summary(df))

    except Exception as e:
        print(f"Error loading dataset: {e}")
