# ALEPHON

ALEPHON is an open-source, command-line text encoder and decoder written in Python. It converts characters into numerical sequences using a table of prime numbers, square roots, and each character's position in the message. The output also includes randomized decimal precision and numerical separators.

ALEPHON uses a custom encoding method, **not secure encryption**. Do not use it to protect sensitive information.

## How it works

ALEPHON supports 31 characters: the letters `A–Z`, the punctuation marks `. , ? !`, and spaces. Lowercase input is converted to uppercase before encoding. Other characters have no mapping and are skipped.

Each supported character corresponds to one prime number in `numberIndex`, matched by its position in `letterIndex`.

### Encoding

For each input character, ALEPHON:

1. Looks up its corresponding prime number.
2. Takes the square root of that number.
3. Multiplies the result by the character's **1-based position** in the original input.
4. Formats the result with a randomly selected **2–5 decimal places**.
5. Appends one randomly selected four-digit separator from `breakCharacterIndex`.

The separator-selection function avoids choosing a separator whose first digit matches the last digit of the preceding encoded value. It does **not** guarantee that separators cannot occur inside encoded values.

### Decoding

The decoder:

1. Replaces all known separator sequences with spaces and splits the result into numerical segments.
2. Divides each segment by its **1-based position** in the decoded sequence, squares the result, and rounds it to the nearest integer.
3. Looks for an **exact match** in `numberIndex` and appends the corresponding character from `letterIndex`.

The decoder does not currently choose the *closest* prime number. If a calculated value does not exactly match an entry in the table, that character is not recovered.

## Running ALEPHON

You need Python 3. The program uses only Python standard-library modules (`os`, `math`, and `random`); no third-party packages are required.

Run the Python script from a terminal:

```bash
python <script-name>.py
```

Replace `<script-name>` with the filename in your copy of the repository.

At the prompt, enter `1` to encode a message or `2` to decode one. The program prints intermediate diagnostic information as well as the result. It remains in its menu loop until you stop it.

## Creating your own version

The character mappings are defined in two lists near the top of the source file:

- `letterIndex` contains the supported characters.
- `numberIndex` contains their corresponding numerical values **in the same order**.

You can fork the project and change the values in `numberIndex` to create a different mapping. Keep both lists the same length, and keep the numerical values distinct if you want each character to map back unambiguously. Because the algorithm takes square roots, values must also be nonnegative; the existing implementation is designed around positive prime numbers.

Both the encoder and decoder must use the **same mapping and separator sequences** to exchange messages correctly. Changing the mapping does not make the system cryptographically secure.

## Limitations and security warning

**ALEPHON is not intended for confidential communication.** Its algorithm and default character mappings are public. Anyone with access to your version of the source code can inspect its mappings and decoding process. Even without source access, changing the numerical values alone is not a reliable substitute for established cryptography.

Other limitations of the current implementation include:

- **Separator collisions:** a four-digit separator may also appear within an encoded number, causing the decoder to split the message incorrectly.
- **Rounding and precision:** the encoder discards decimal digits, while the decoder requires exact integer matches after reversing the calculation. Some values may therefore fail to decode.
- **Unsupported characters:** characters outside the 31-character table are omitted during encoding. Their positions still affect the encoder's position multiplier, which can prevent subsequent characters from decoding correctly.
- **Uppercase output:** lowercase letters are converted to uppercase during encoding, so the original capitalization cannot be recovered.
- **No input validation:** malformed encoded input may cause a conversion error rather than a readable error message.

ALEPHON is a readable, customizable text-encoding program, **not a replacement for tested encryption software**.
