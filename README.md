# Numerical Methods in Engineering with Python 3

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Spyder](https://img.shields.io/badge/IDE-Spyder-FF0000?logo=spyderide&logoColor=white)
![NumPy](https://img.shields.io/badge/Scientific_Computing-NumPy-013243?logo=numpy)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)
![Discipline](https://img.shields.io/badge/Discipline-Computational_Engineering-blue)

## Overview

This repository documents an independent study of numerical methods,
engineering mathematics, and scientific computing through the textbook
*Numerical Methods in Engineering with Python 3* by Jaan Kiusalaas.

The objective is to develop a practical understanding of numerical
algorithms, their mathematical foundations, computational implementation,
and applicability to engineering problems.

The repository serves as a computational learning laboratory rather than
a production engineering software package. It emphasizes independent
programming, mathematical reasoning, numerical experimentation, and
verification of computational results.

Particular emphasis is placed on developing transferable knowledge
applicable to hydraulic modeling, infrastructure simulation, engineering
optimization, and scientific computing.

## Primary Reference

**Numerical Methods in Engineering with Python 3**

- Author: Jaan Kiusalaas
- Edition: Third Edition
- Publisher: Cambridge University Press
- Publication Year: 2013
- ISBN: 978-1-107-03385-6
- DOI: [10.1017/CBO9781139523899](https://doi.org/10.1017/CBO9781139523899)

## Learning Objectives

- Strengthen proficiency in Python for scientific computing.
- Develop an understanding of numerical approximation techniques.
- Translate mathematical formulations into computational algorithms.
- Implement fundamental numerical methods independently.
- Investigate numerical accuracy, stability, and convergence.
- Understand the limitations and assumptions of numerical algorithms.
- Compare independently implemented algorithms with established
  scientific computing libraries.
- Develop reproducible computational experiments.
- Establish a foundation for applied engineering modeling and simulation.
- Improve technical documentation and computational verification practices.

## Scope of Study

The study follows the general progression of the textbook while
incorporating independent exercises, computational experiments,
and practical engineering applications.

| Chapter | Subject | Status |
|:-------:|---------|--------|
| 01 | Python programming fundamentals | In Progress |
| 02 | Linear equation systems | Planned |
| 03 | Interpolation and data fitting | Planned |
| 04 | Nonlinear equation solvers | Planned |
| 05 | Numerical differentiation | Planned |
| 06 | Numerical integration | Planned |
| 07 | Initial-value differential equations | Planned |
| 08 | Boundary-value differential equations | Planned |
| 09 | Eigenvalue analysis | Planned |
| 10 | Numerical optimization | Planned |

## Technical Competencies

### Python and Scientific Programming

- Python fundamentals
- Functions and modules
- Data structures
- Array-based computation
- Vectorized operations
- Floating-point arithmetic
- Scientific visualization
- Modular algorithm development
- Debugging and computational troubleshooting

### Engineering Mathematics

- Linear algebra
- Matrix operations
- Polynomial approximations
- Nonlinear equations
- Differential equations
- Numerical approximation
- Eigenvalue analysis
- Mathematical optimization

### Numerical Analysis

- Absolute and relative error
- Truncation error
- Floating-point round-off error
- Numerical stability
- Convergence criteria
- Iterative solution methods
- Algorithm efficiency
- Sensitivity analysis
- Computational verification

## Engineering Applications

Although the primary purpose of this repository is educational,
the numerical methods investigated have direct applications across
multiple engineering disciplines.

| Numerical Method | Potential Engineering Application |
|------------------|-----------------------------------|
| Linear equations | Hydraulic network analysis and mass balance |
| Interpolation | Pump curves and performance characteristics |
| Curve fitting | Model calibration and parameter estimation |
| Root finding | Pump operating points and equilibrium conditions |
| Numerical differentiation | Sensitivity and rate-of-change analysis |
| Numerical integration | Storage volumes and cumulative flow |
| Initial-value problems | Tank drawdown and dynamic system simulation |
| Boundary-value problems | Groundwater flow and spatial systems |
| Eigenvalue analysis | System stability and modal analysis |
| Optimization | Pump scheduling and infrastructure design |

These applications provide a connection between fundamental numerical
methods and practical computational engineering.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Primary programming language |
| NumPy | Numerical and array-based computation |
| SciPy | Reference algorithms and numerical verification |
| Matplotlib | Scientific visualization |
| SymPy | Symbolic mathematics and analytical verification |
| pytest | Automated numerical and software verification |
| uv | Dependency and environment management |
| Spyder | Primary scientific development environment |
| Git | Version control |
| Markdown | Technical documentation |

Dependencies will be incorporated as required throughout the study.

## Development Philosophy

### Mathematics First

Before implementing a numerical algorithm, establish an understanding
of its mathematical formulation, assumptions, and intended application.

The objective is not simply to obtain a numerical answer, but to
understand how that answer is produced and whether it is reliable.

### Independent Implementation

Numerical algorithms should initially be implemented independently
where practical.

Established scientific computing libraries may subsequently be used
to compare results, evaluate accuracy, and investigate alternative
implementation approaches.

### Reproducibility

Computational experiments should be reproducible through documented
inputs, assumptions, dependencies, and numerical parameters.

### Verification

Numerical results should be evaluated against appropriate reference
solutions whenever possible.

Verification may include:

- Analytical solutions
- Hand calculations
- Independent implementations
- Established scientific computing libraries
- Published benchmark problems
- Convergence studies
- Boundary and limiting conditions

### Computational Experimentation

Algorithms should be investigated beyond their nominal implementation.

Where appropriate, experiments should examine:

- Initial conditions
- Boundary conditions
- Step-size selection
- Error tolerances
- Iteration limits
- Convergence behavior
- Computational efficiency
- Numerical failure conditions

### Independent Learning

The primary objective is to develop programming proficiency and
mathematical understanding through direct implementation and
problem-solving.

External references and development assistance may support conceptual
understanding, troubleshooting, and verification, but should not
replace independent implementation of the numerical methods under study.

## Study Methodology

Each major numerical method will generally follow the following
learning sequence:

1. Study the mathematical theory.
2. Identify assumptions and limitations.
3. Review the algorithm and computational procedure.
4. Develop an independent Python implementation.
5. Execute representative numerical examples.
6. Verify results against reference solutions.
7. Investigate accuracy and convergence.
8. Document observations and lessons learned.
9. Identify potential engineering applications.

Not every introductory exercise requires the complete verification
process. The level of documentation should be proportional to the
complexity and significance of the numerical method.

## Development Environment

The primary development environment is Spyder, selected for its
scientific computing capabilities and interactive numerical analysis
workflow.

Additional development environments may include:

- JetBrains PyCharm
- Visual Studio Code
- Command-line Python

### Environment Setup

For a repository configured with `pyproject.toml` and `uv.lock`,
synchronize the project environment using:

    uv sync

Verify the Python interpreter:

    uv run python --version

Run an individual Python script:

    uv run python path/to/script.py

Run automated tests, once configured:

    uv run pytest

When using Spyder, configure its Python interpreter to reference
the project-specific virtual environment and install a compatible
version of spyder-kernels when required.

On Linux:

    .venv/bin/python

On Windows:

    .venv\Scripts\python.exe

## Numerical Verification Standards

Numerical correctness should not be assumed simply because a program
executes successfully.

Where applicable, verification should consider:

- Correctness of mathematical formulation
- Consistency of input and output units
- Accuracy of numerical results
- Absolute and relative error
- Convergence behavior
- Sensitivity to numerical parameters
- Floating-point limitations
- Algorithm stability
- Appropriate stopping criteria
- Reproducibility of results

Acceptance tolerances should be established according to the numerical
method and intended application rather than applying a universal
tolerance to all computational problems.

## Coding Standards

Python implementations should progressively incorporate appropriate
software engineering practices, including:

- PEP 8 naming and formatting conventions
- Descriptive variable and function names
- Explicit mathematical notation where practical
- Clear comments explaining numerical procedures
- Function docstrings
- Type annotations where appropriate
- Modular and reusable functions
- Explicit unit definitions for engineering calculations
- Appropriate error handling
- Automated tests for reusable numerical algorithms

Introductory learning exercises may deliberately remain procedural
to emphasize fundamental programming and mathematical concepts.

## Documentation Standards

Documentation should focus on understanding and communicating
computational methods rather than merely describing source code.

Where appropriate, documentation should address:

- Mathematical formulation
- Algorithm purpose
- Input parameters
- Expected outputs
- Numerical assumptions
- Implementation decisions
- Verification procedures
- Observed limitations
- Potential engineering applications
- Lessons learned

## Relationship to Applied Engineering Projects

This repository provides a mathematical and computational foundation
for more advanced engineering software development.

Potential areas of application include:

- Hydraulic network modeling
- Water distribution system analysis
- Wastewater collection system modeling
- Pump station and force-main analysis
- Water storage and tank dynamics
- Groundwater flow simulation
- Infrastructure performance modeling
- Engineering optimization
- Uncertainty-aware simulation
- Infrastructure decision analytics
- Digital twins

The emphasis is on developing an understanding of the numerical
methods underlying engineering modeling software, rather than
exclusively relying on existing commercial modeling applications.

## Project Status

**Active Independent Study**

This repository is under continuous development as the textbook
and associated exercises are completed.

Implementations may be revised as mathematical understanding,
programming proficiency, and numerical analysis techniques improve.

The repository represents an evolving record of computational
engineering knowledge and professional development.

## Academic Integrity and Attribution

This repository is an independent educational project based on the
work of Jaan Kiusalaas.

All intellectual property associated with the referenced textbook
remains with its respective copyright holders.

The repository is intended to contain independently developed
implementations, original study notes, computational investigations,
and additional engineering examples.

Any third-party material must be appropriately attributed and used
in accordance with applicable copyright and licensing requirements.

This repository is not an official companion repository, publication,
or solution manual associated with the textbook or its publisher.

## Disclaimer

The numerical implementations contained in this repository are
developed for educational, research, and professional development
purposes.

They are not certified or validated production engineering tools
and should not be relied upon for engineering design, regulatory
compliance, or safety-critical decision-making without appropriate
independent verification and professional review.

---

**Focus Areas:** Numerical Methods | Engineering Mathematics |
Scientific Computing | Computational Engineering | Python |
Infrastructure Modeling
