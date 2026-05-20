"""
Stage 2 – transform
Reads data/clean/events.csv and adds a `date` column (YYYY-MM-DD).
Writes result to data/transformed/events.csv.
"""

import pathlib
import pandas as pd

CLEAN_PATH = pathlib.Path("data/clean/events.csv")
TRANSFORMED_PATH = pathlib.Path("data/transformed/events.csv")


def main() -> None:
    df = pd.read_csv(CLEAN_PATH)

    df["date"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%dT%H:%M:%S").dt.strftime(
        "%Y-%m-%d"
    )

    TRANSFORMED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(TRANSFORMED_PATH, index=False)
    print(f"Wrote {len(df)} rows to {TRANSFORMED_PATH}")


if __name__ == "__main__":
    main()
