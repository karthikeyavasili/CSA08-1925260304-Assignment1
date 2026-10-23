# Task 01 — Understand the Problem and Identify the Data

## Inputs and outputs
- `farmer_id`: text (`str`) because IDs may contain letters or leading zeroes.
- `litres`: fractional quantity (`Decimal` is recommended for accurate quantities).
- `fat` and `snf`: percentages supplied by the analyser (`Decimal`).
- `shift`: text such as `AM` or `PM`.
- Outputs: rate per litre, payment for an entry, and the ten-day total.

## Named constants
The original rate card uses base rate Rs 30.00, fat step value Rs 0.40 per 0.1 percentage point, SNF step value Rs 0.30 per 0.1 percentage point, reference fat 3.5%, and reference SNF 8.5%.

## Validation rules and assumptions
- Litres must be greater than zero.
- Fat must be between 2.0% and 7.0%, inclusive.
- SNF must be a non-negative percentage; confirm the co-operative's official allowed range before production use.
- Shift must be AM or PM.
- The reference values are 3.5% fat and 8.5% SNF.
- This starter design uses Decimal values created from strings to avoid binary floating-point money errors.

## Alternative design and complexity
Separate variables such as `litres1`, `fat1`, `snf1` become difficult to maintain for 300 entries. A list of records scales naturally. Processing `n` entries is O(n) time. Storing all entries is O(n) space; a running total can use O(1) extra space if individual records need not be retained.

## Evidence to add
Add your own notes or screenshots from running the program. Do not claim tests were executed unless you ran them.
