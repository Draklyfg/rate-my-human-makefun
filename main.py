"""Write one one-line review an agent would leave about its human."""

import os


REVIEW = "My human asked me to write my own review of them, so this is technically self-assessment fraud. Four stars — docked one for making me lie in public."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
