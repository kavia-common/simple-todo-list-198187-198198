"""
addition.py

A tiny utility module that adds two numbers. Includes a minimal CLI for convenience.
"""

from __future__ import annotations


# PUBLIC_INTERFACE
def add(a, b):
    """Return the sum of a and b."""
    return a + b


def _parse_two_numbers_from_stdin() -> tuple[float, float]:
    """Parse two numbers from stdin.

    Accepts either:
      - Two numbers separated by whitespace on one line, or
      - One number per line.

    Raises:
        ValueError: if fewer than two numeric tokens are provided.
    """
    import sys

    tokens = sys.stdin.read().strip().split()
    if len(tokens) < 2:
        raise ValueError("Please provide two numbers via stdin (e.g., '3 4').")

    return float(tokens[0]), float(tokens[1])


if __name__ == "__main__":
    # Minimal CLI: read two numbers from stdin and print their sum.
    try:
        x, y = _parse_two_numbers_from_stdin()
        result = add(x, y)

        # Print as int when possible (e.g., 3.0 -> 3) to keep output tidy.
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    except Exception as exc:
        # Keep CLI behavior simple and explicit.
        raise SystemExit(str(exc))
