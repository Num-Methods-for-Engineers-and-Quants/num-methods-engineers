#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:07:54 2026

@author: brice-nelson
"""


# =============================================================================
# String Formatting - Floating-Point Numbers
# =============================================================================
#
# The format() method allows numerical values to be displayed using a
# specified width, precision, and numerical representation.
#
# Syntax:
#     "{:7.2f}".format(num)
#
# Format specification breakdown:
#
#     :  - Indicates the beginning of the format specification.
#
#     7  - Specifies the minimum total field width, including digits,
#          the decimal point, negative sign, and any padding spaces.
#          If the number exceeds this width, the field expands.
#
#     .2 - Specifies the number of digits displayed after the
#          decimal point. The displayed value is rounded accordingly.
#
#     f  - Specifies fixed-point floating-point notation.
#
# Expected output:
#     1245.13
#
# The equivalent syntax using a modern Python f-string is:
#     print(f"{num:7.2f}")
#
# Important:
#     String formatting only changes the displayed representation
#     of the numerical value. It does not modify the original value
#     or its underlying floating-point precision.
#
# Engineering application:
#     Maintain full numerical precision throughout engineering and
#     scientific calculations. Apply formatting when presenting
#     results in reports, tables, or console output.
#
# =============================================================================

num = 1245.1256745687

# Traditional string formatting
print("Traditional Result:")
print("{:7.2f}\n".format(num))

# Modern f-string formatting
print("Modern f-string Result:")
print(f"{num:7.2f}")