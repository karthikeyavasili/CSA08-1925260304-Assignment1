# Task 12 — Day-4 Design Challenge: Re-evaluate and Adapt

## Decision: MODIFY
Keep the modular design and Decimal arithmetic, but make the rate card selectable by season and add a separate volume-bonus function.

## Changed requirements
- April–June base rate: Rs 32.00.
- April–June fat step: Rs 0.45 per 0.1 percentage point.
- SNF step value remains Rs 0.30 unless the union announces otherwise.
- Fat and SNF readings can have two decimal places, so calculate the number of 0.1-point steps using the documented nearest-step rule.
- A farmer supplying more than 500 litres in ten days receives Rs 0.50 per litre bonus. Exactly 500 litres does not qualify.

Run `seasonal_calculator.py` to see sample tests for the original and seasonal rates and the bonus. Add screenshots and your measured outputs to `evidence/`.
