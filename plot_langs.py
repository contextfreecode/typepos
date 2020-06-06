from matplotlib.pyplot import Axes, show, style
from matplotlib import rcParams
from pandas import DataFrame

# Talking points:
# - I'm one of those folks that cares about syntax.
# - These are the popular languages of now, not 40 years ago.
# - Decimal abstracted in C++.
# - C++ here is C++17 (mostly), not C++20.
# - Function call prefix vs piped operations.
# - If YouTube is right, I'm older than most of my viewers.
# - Go only trailing on this list without extra operators.
# - `name: type = ...` similar to `name = type ...`


columns = ["name", "share", "year", "typepos"]
data = [
    ["Python 3", 14.28, 2008, "trailing"],
    ["Java", 10.34, 1995, "leading"],
    ["Go", 7.68, 2012, "trailing"],
    ["C++", 7.18, 1985, "leading"],
    ["C++11", 7.18, 2011, "both"],
    ["TypeScript", 5.45, 2014, "trailing"],
    ["PHP 5", 5.33, 2004, "both"],
    ["C#", 4.21, 2002, "leading"],
    ["C", 3.85, 1978, "leading"],
    ["Swift", 1.13, 2014, "trailing"],
    ["Scala", 1.06, 2004, "trailing"],
    ["Dart", 0.92, 2013, "leading"],
    ["Rust", 0.91, 2015, "trailing"],
    ["Kotlin", 0.82, 2016, "trailing"],
    ["Objective-C", 0.70, 1984, "leading"],
]


def main():
    languages = DataFrame(columns=columns, data=data)
    print(languages)
    print(languages.groupby("typepos").mean())
    rcParams.update({"font.size": 14})
    style.use("dark_background")
    ax: Axes = None
    colors = dict(leading=[0.4, 0.6, 1], trailing=[1, 0.7, 0])
    colors.update(both=colors["trailing"])
    edges = {**colors, **dict(both=colors["leading"])}
    for typepos, group in languages.groupby("typepos"):
        ax = group.plot(
            x="year",
            y="share",
            ax=ax,
            color=colors[typepos],
            label=typepos,
            markeredgecolor=edges[typepos],
            markeredgewidth=3,
            markersize=10,
            style="o",
        )
        for _, row, *_ in group.iterrows():
            ax.annotate(
                s=row["name"],
                xy=[row["year"], row["share"]],
                xytext=[0, 12],
                textcoords="offset pixels",
                horizontalalignment="center",
                # verticalalignment="center",
            )
    ax.set_ylim([0, ax.get_ylim()[1]])
    ax.set_ylabel("2020Q1 GitHub Activity Share")
    # ax.figure.tight_layout()
    show()


if __name__ == "__main__":
    main()
