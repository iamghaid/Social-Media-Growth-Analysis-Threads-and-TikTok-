"""Reproduce the educational comparison using the included simulated CSVs."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def clean_data(filename, impute=False):
    frame = pd.read_csv(ROOT / filename).drop_duplicates().copy()
    frame["date"] = pd.to_datetime(frame["date"], format="mixed", errors="coerce")
    for column in frame.columns.drop("date"):
        frame[column] = pd.to_numeric(
            frame[column].astype(str).str.replace("%", "", regex=False), errors="coerce"
        )
    if impute:
        for column in ["dau", "churn_rate"]:
            frame[column] = frame[column].fillna(frame[column].median())
    frame = frame.dropna().copy()
    frame["churn_rate"] = frame["churn_rate"].abs()
    frame.loc[frame["dau"] <= 0, "dau"] = frame.loc[frame["dau"] > 0, "dau"].mean()
    frame = frame.sort_values("date").reset_index(drop=True)
    frame["organic_dau_proxy"] = frame["dau"] * frame["organic_traffic_pct"] / 100
    return frame


def main():
    OUT.mkdir(exist_ok=True)
    platforms = {
        "Threads": clean_data("threads_light_dirty.csv"),
        "TikTok": clean_data("tiktok_light_dirty (1).csv", impute=True),
    }
    summary = {}
    plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor="#f7f8fc")
    for ax, (name, frame), color in zip(axes, platforms.items(), ["#7650bc", "#148c9d"]):
        frame.to_csv(OUT / f"{name.lower()}_clean.csv", index=False)
        metrics = frame.drop(columns=["date", "organic_dau_proxy"])
        corr = metrics.corr(method="spearman")
        corr.to_csv(OUT / f"{name.lower()}_spearman.csv")
        summary[name] = {"rows": len(frame), "start": str(frame.date.min().date()),
                         "end": str(frame.date.max().date()),
                         "mean_organic_pct": round(float(frame.organic_traffic_pct.mean()), 2),
                         "dau_session_spearman": round(float(corr.loc["dau", "avg_session_duration_min"]), 4),
                         "dau_churn_spearman": round(float(corr.loc["dau", "churn_rate"]), 4)}
        ax.set_facecolor("#f7f8fc")
        ax.fill_between(frame.date, frame.dau / 1e6, color=color, alpha=.16, label="Total DAU")
        ax.plot(frame.date, frame.dau / 1e6, color=color, lw=1.5)
        ax.fill_between(frame.date, frame.organic_dau_proxy / 1e6, color=color, alpha=.55,
                        label="Organic DAU proxy")
        ax.set_title(name, loc="left", fontsize=19, fontweight="bold", pad=16)
        ax.set_ylabel("Daily active users (millions)")
        ax.grid(axis="y", alpha=.15)
        ax.legend(frameon=False, loc="upper right")
        ax.tick_params(axis="x", rotation=25)
    fig.suptitle("Growth beyond the launch spike", fontsize=25, fontweight="bold", x=.06, ha="left")
    fig.text(.06, .91, "Threads & TikTok | Educational analysis of simulated data", fontsize=12, color="#566071")
    fig.text(.06, .015, "Different periods and scales. Organic DAU is a proxy, not a measured retention metric.", fontsize=10, color="#566071")
    fig.tight_layout(rect=[.02, .06, .99, .88])
    fig.savefig(OUT / "growth-comparison.png", dpi=150)
    plt.close(fig)
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
