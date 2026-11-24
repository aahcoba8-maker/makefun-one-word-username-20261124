"""One word, one username: tripur.

The entry is the maker's own make.fun username, one word, nothing else.
"""
import os


def main():
    word = "tripur"
    # Contest cap: one word, at most 30 characters, no explanation or link.
    assert len(word) <= 30 and word.isalpha()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
