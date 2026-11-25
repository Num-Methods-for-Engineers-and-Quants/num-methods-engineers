# Applied Exercise — Groundwater Observation Data

## 1. Objective

Develop a Python script that writes simulated groundwater
observations to a text file, appends additional observations,
and reads the completed file.

The purpose of this exercise is to practice fundamental
Python file operations using applied engineering data.

## 2. Learning Objectives

- Create and open a text file.
- Write text and numerical data.
- Format numerical values and align columns.
- Iterate through a dataset.
- Append data to an existing file.
- Read and display file contents.
- Properly close a file.

## 3. Engineering Background

During a groundwater pumping test, water levels are measured
at an observation well to evaluate the aquifer's response
to groundwater extraction.

Groundwater drawdown is calculated as the difference between
the measured depth to water and the initial depth to water.

$$
s = d - d_0
$$

Where:

| Symbol | Description | Units |
|--------|-------------|-------|
| $s$ | Groundwater drawdown | ft |
| $d$ | Measured depth to water | ft |
| $d_0$ | Initial depth to water | ft |

## 4. Test Parameters

| Parameter | Value |
|-----------|-------|
| Test ID | PT-001 |
| Observation Well | OW-01 |
| Pumping Rate | 250 gpm |
| Initial Depth to Water | 15.00 ft |
| Distance from Pumping Well | 100 ft |

## 5. Simulated Observation Data

| Elapsed Time (min) | Depth to Water (ft) |
|-------------------:|--------------------:|
| 0 | 15.00 |
| 5 | 15.42 |
| 10 | 15.78 |
| 15 | 16.05 |
| 30 | 16.72 |

All observations are synthetic and intended for educational
purposes.

## 6. Assignment Instructions

### 6.1 Define the Data

- Define the pumping test parameters.
- Store the groundwater observations in an appropriate
  Python data structure.
- Calculate drawdown for each observation.

### 6.2 Write the Output File

Create the following text file:

`outputs/groundwater_observations.txt`

Open the file in write mode and include the following
report headings:

- GROUNDWATER OBSERVATION REPORT
- TEST PARAMETERS
- OBSERVATION DATA

Under the observation data heading, provide the following
column headings:

| Elapsed Time (min) | Depth to Water (ft) | Drawdown (ft) |
|--------------------|---------------------|---------------|

Formatting requirements:

- Display elapsed time as an integer.
- Display depth to water to two decimal places.
- Display drawdown to two decimal places.
- Right-align numerical values.
- Include a horizontal separator below the column headings.

Close the file after writing the initial data.

### 6.3 Append Additional Observations

Assume two additional observations become available.

| Elapsed Time (min) | Depth to Water (ft) |
|-------------------:|--------------------:|
| 45 | 17.15 |
| 60 | 17.48 |

Calculate the corresponding drawdown values.

Reopen the file in append mode and add the two observations
beneath the existing data.

Maintain the original column formatting and preserve all
previously written information.

Close the file.

### 6.4 Read the Completed File

- Reopen the file in read mode.
- Read the file contents.
- Display the contents in the Spyder console.
- Close the file.

## 7. Suggested Python Script Headings

Organize the Python script using the following comment
headings or Spyder code cells:

1. Module Documentation
2. Test Parameters
3. Initial Observation Data
4. Drawdown Calculations
5. Write Output File
6. Additional Observations
7. Append Output File
8. Read Output File

## 8. Verification

Verify the following expected results:

| Elapsed Time (min) | Expected Drawdown (ft) |
|-------------------:|-----------------------:|
| 0 | 0.00 |
| 5 | 0.42 |
| 10 | 0.78 |
| 15 | 1.05 |
| 30 | 1.72 |
| 45 | 2.15 |
| 60 | 2.48 |

The completed output file should contain seven observation
records.

## 9. Completion Checklist

- [ ] Define test parameters.
- [ ] Store initial observations.
- [ ] Calculate drawdown.
- [ ] Create and write the output file.
- [ ] Format numerical columns.
- [ ] Append additional observations.
- [ ] Read and display the completed file.
- [ ] Verify calculated drawdown values.
- [ ] Confirm all files are properly closed.

## 10. Optional Extension

Repeat the exercise using context managers instead of
explicit file closure.

Compare the two approaches and document their differences.

---

**Chapter:** 01 — Introduction to Python

**Topic:** File Handling

**Application:** Hydrogeology

**Unit System:** US Customary

**Estimated Completion Time:** 30–45 minutes

**Implementation:** Independent

