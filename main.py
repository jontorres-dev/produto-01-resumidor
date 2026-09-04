import argparse
import sys

from resumidor import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Resume um texto em no máximo 3 frases.")
    parser.add_argument("texto", nargs="*", help="Texto a resumir. Se omitido, lê do stdin.")
    args = parser.parse_args()

    text = " ".join(args.texto) if args.texto else sys.stdin.read()
    print(summarize(text))


if __name__ == "__main__":
    main()
