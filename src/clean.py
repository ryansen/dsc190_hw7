"""
Stage 1 – clean
Reads data/raw/events.csv, drops invalid rows, normalizes timestamps to ISO 8601.
Writes result to data/clean/events.csv.

Invalid rows are those with:
  - any missing field
  - a non-positive duration_seconds
  - an event_type not in the allowed set {click, page_view, purchase}
"""

import pathlib
import pandas as pd

VALID_EVENT_TYPES = {"click", "page_view", "purchase"}

RAW_PATH = pathlib.Path("data/raw/events.csv")
CLEAN_PATH = pathlib.Path("data/clean/events.csv")

TIMESTAMP_FORMATS = [
    "%Y-%m-%dT%H:%M:%S",   # 2024-01-15T08:23:11
    "%Y-%m-%d %H:%M:%S",   # 2024-01-15 09:14:32
    "%d/%m/%Y %H:%M:%S",   # 15/01/2024 12:30:00
]


def parse_timestamp(ts: str) -> pd.Timestamp | None:
    """Try each known format; return None if none matches."""
    for fmt in TIMESTAMP_FORMATS:
        try:
            return pd.to_datetime(ts, format=fmt)
        except (ValueError, TypeError):
            continue
    return None


def main() -> None:
    df = pd.read_csv(RAW_PATH, dtype=str)

    # Drop rows with any missing field
    before = len(df)
    df = df.dropna()
    print(f"Dropped {before - len(df)} rows with missing fields ({len(df)} remain)")

    # Strip whitespace from all string columns
    df = df.apply(lambda col: col.str.strip())

    # Drop rows with invalid event_type
    before = len(df)
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]
    print(f"Dropped {before - len(df)} rows with invalid event_type ({len(df)} remain)")

    # Convert duration_seconds to numeric and drop non-positive values
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    before = len(df)
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]
    print(f"Dropped {before - len(df)} rows with non-positive duration_seconds ({len(df)} remain)")

    # Normalize timestamps to ISO 8601
    df["timestamp"] = df["timestamp"].apply(parse_timestamp)
    before = len(df)
    df = df.dropna(subset=["timestamp"])
    print(f"Dropped {before - len(df)} rows with unparseable timestamps ({len(df)} remain)")

    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    # Write output
    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Wrote {len(df)} clean rows to {CLEAN_PATH}")


if __name__ == "__main__":
    main()
