"""Smoke tests: the names dataset loads and bigram counting behaves."""

from pathlib import Path

NAMES = Path(__file__).resolve().parent.parent / "names.txt"


def test_dataset_loads() -> None:
    words = NAMES.read_text().splitlines()
    assert len(words) > 30000
    assert all(w.isalpha() for w in words[:100])


def test_bigram_counts() -> None:
    words = NAMES.read_text().splitlines()[:100]
    counts: dict[tuple[str, str], int] = {}
    for w in words:
        chs = ["<S>", *list(w), "<E>"]
        for ch1, ch2 in zip(chs, chs[1:], strict=False):
            counts[(ch1, ch2)] = counts.get((ch1, ch2), 0) + 1
    assert counts
    assert all(v > 0 for v in counts.values())
    assert sum(counts.values()) == sum(len(w) + 1 for w in words)
