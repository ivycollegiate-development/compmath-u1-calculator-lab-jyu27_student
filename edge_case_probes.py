"""Your personalized edge cases for U1 L13 — GENERATED, DO NOT COMMIT.

Written by gen_probes.py. This file is in .gitignore on purpose.

Work through each group. For every case write down:
  the input | what actually happened | bug, or correct behavior?

"Correct behavior" is a real and valuable answer. Say so when you find one.
"""

PROBES = {
    "WRONG_TYPE": [
        '   ',
        'NaN',
        '',
    ],
    "HUGE": [
        '123456789012345678901234567890',
        '1e16',
        '1e308',
    ],
    "BOUNDARY": [
        '273.15',
        '5e-324',
        '273.16',
    ],
    "DIV_ZERO": [
        '-1e-320',
        '-0.0',
        '-0',
    ],
}

# Groups worth working through, in this order:
GROUPS = ['WRONG_TYPE', 'HUGE', 'BOUNDARY', 'DIV_ZERO']
