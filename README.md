# ALEPHON

ALEPHON is an open-source text encoder and decoder written in Python. It converts text into numerical sequences using a customizable character mapping.

The project is intended for encoding and decoding text, **not for secure communication**.

## Features

- Encodes and decodes text through a terminal interface.
- Supports the English alphabet (`A–Z`), spaces, and `. , ? !`.
- Does not preserve capitalization.
- Uses customizable numerical values for individual characters.
- Requires no third-party Python packages.

## Usage

Install Python 3, download the source code, and run the main Python script in your terminal:

```bash
python alephon.py
```

Select `1` to encode or `2` to decode, but generally just follow the prompts.

## Make your own version

ALEPHON is open source, so you can fork the repository and customize the character mappings. The values are stored in `numberIndex`, with each entry corresponding to the character at the same position in `letterIndex`.

Keep the lists aligned and use distinct, positive numbers. Anyone exchanging encoded messages with your version must use compatible mappings and separators.

## Security disclaimer

ALEPHON uses a custom encoding method, **not established cryptography**. Its default mappings are public, and the encoding can be reverse-engineered. Access to your modified source code would also reveal your mappings.

**Changing the values yourself does not guarantee security. Do not use ALEPHON to protect sensitive information.**

## Known limitations

- Certain encoded values may not decode correctly because of separator collisions or rounding.
- Unsupported characters are skipped.
- Original capitalization is not preserved.

