#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:28:06 2026

@author: brice-nelson
"""

# =============================================================================
# File Handling Example - Groundwater Research Log
# =============================================================================

filename = "output/groundwater_results.txt"


# Provide space for printing purposes
print("")

# Write initial simulation results.
with open(filename, "w", encoding="utf-8") as file:
    file.write("Groundwater Drawdown Analysis\n")
    file.write("=" * 40 + "\n")
    file.write("Pumping Rate: 500 gpm\n")
    file.write("Elapsed Time: 24 hours\n")
    file.write("Drawdown: 12.45 ft\n")

# Append additional simulation results.
with open(filename, "a", encoding="utf-8") as file:
    file.write("\nAdditional Simulation\n")
    file.write("Pumping Rate: 750 gpm\n")
    file.write("Elapsed Time: 24 hours\n")
    file.write("Drawdown: 18.68 ft\n")

# Read and display the complete file.
with open(filename, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)