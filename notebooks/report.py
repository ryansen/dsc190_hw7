import marimo

__generated_with = "0.7.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    return mo, pd, plt, ticker


@app.cell
def __(mo):
    mo.md(
        r"""
        # Event Duration Report

        This notebook loads the final pipeline output (`data/features/events.csv`)
        and visualises the distribution of event durations.
        """
    )
    return


@app.cell
def __(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)


@app.cell
def __(mo, df):
    mo.md(
        f"""
        **Dataset summary:** {len(df):,} events across
        {df['date'].nunique()} days,
        {df['event_type'].nunique()} event types.
        """
    )
    return


@app.cell
def __(df, plt, ticker):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(
        df["duration_minutes"],
        bins=30,
        color="#4f86c6",
        edgecolor="white",
        linewidth=0.6,
    )

    ax.set_xlabel("Duration (minutes)", fontsize=12)
    ax.set_ylabel("Number of events", fontsize=12)
    ax.set_title("Distribution of Event Durations", fontsize=14, fontweight="bold")
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    fig
    return ax, fig


@app.cell
def __(df, mo):
    stats = df["duration_minutes"].describe().round(2)
    mo.md(
        f"""
        ### Duration statistics (minutes)

        | Metric | Value |
        |--------|------:|
        | Count  | {stats['count']:.0f} |
        | Mean   | {stats['mean']} |
        | Std    | {stats['std']} |
        | Min    | {stats['min']} |
        | Median | {stats['50%']} |
        | Max    | {stats['max']} |
        """
    )
    return (stats,)


@app.cell
def __(df, plt):
    fig2, ax2 = plt.subplots(figsize=(9, 4))

    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counts = df["weekday"].value_counts().reindex(order, fill_value=0)

    ax2.bar(counts.index, counts.values, color="#6abf69", edgecolor="white", linewidth=0.6)
    ax2.set_xlabel("Day of week", fontsize=12)
    ax2.set_ylabel("Number of events", fontsize=12)
    ax2.set_title("Events by Day of Week", fontsize=14, fontweight="bold")
    ax2.grid(axis="y", linestyle="--", alpha=0.4)
    ax2.spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    fig2
    return ax2, counts, fig2, order


if __name__ == "__main__":
    app.run()
