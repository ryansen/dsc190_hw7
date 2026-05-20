"""
Stage 3 – features
Reads data/transformed/events.csv and adds:
  - duration_minutes: duration_seconds / 60
  - weekday: full day-of-week name (Monday … Sunday)
Writes result to data/features/events.csv.
Row count is unchanged.
"""

import pathlib
import pandas as pd

TRANSFORMED_PATH = pathlib.Path("data/transformed/events.csv")
FEATURES_PATH = pathlib.Path("data/features/events.csv")


def main() -> None:
    df = pd.read_csv(TRANSFORMED_PATH)

    df["duration_minutes"] = df["duration_seconds"] / 60

    df["weekday"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.day_name()

    FEATURES_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(FEATURES_PATH, index=False)
    print(f"Wrote {len(df)} rows to {FEATURES_PATH}")


if __name__ == "__main__":
    main()
