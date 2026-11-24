#!/usr/bin/env python3
"""Write one time-machine warning label to /output/entry.txt. Stdlib only."""
import os

LINE = "WARNING: Do not meet yourself. If you do, the warranty is void, the timeline is confused, and you will both be charged for the same repair."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
