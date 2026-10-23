# Task 11 — Recommend and Defend the Final Design

## Recommendation
Use a reusable module, named constants, validated input, functions, and `Decimal` for financial calculations. Create Decimal values from input strings, not from floats. Round each farmer's payable amount to two decimal places before adding it to the ten-day payable total, then retain the individual entries for auditing.

## Rate revision
Update the rate card in one place or load a versioned rate card from a configuration file. Record the effective date so older transactions can be reproduced.

## Limitations
The starter design is a single-process calculator, not a production database system. Production use would need official SNF limits, authenticated users, persistent storage, duplicate-entry protection, audit logs, backups, and reconciliation procedures.

## Scale
O(n) calculation is appropriate for 150,000 entries. Benchmark on the target machine and use a database or batch-processing workflow for durable records. Include the actual timings from Task 10 as evidence.
