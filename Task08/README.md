# Task 08 — Plan the Algorithm Before Coding

## Pseudocode
1. Set total to zero.
2. Repeat for each farmer entry.
3. Read farmer ID, litres, fat, SNF, and shift.
4. Convert numeric text to Decimal; if conversion fails, report invalid input.
5. Validate litres, fat, SNF, and shift.
6. Calculate fat and SNF steps relative to 3.5% and 8.5%.
7. Calculate rate and payment; round money to two decimal places.
8. Add payment to total.
9. Display each payment and the ten-day total.

## Flowchart
See `validation_flowchart.mmd`. You can render it in a Mermaid-compatible editor and add a screenshot to `evidence/`.

## Hand trace
Use `hand_trace.csv` as a starter table. Verify the values by running the code; do not submit unverified sample values as measured results.

## Complexity
Both storing entries and using a running total take O(n) time. Storing every entry requires O(n) space; a running total requires O(1) additional space. Retain records when audit trails, corrections, or farmer-level reports are needed.
