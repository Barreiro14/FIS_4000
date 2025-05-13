# FIS_4000

**Polynomial Regression and Serial Data Acquisition for Experimental Analysis**

## Overview

This repository contains a suite of Python scripts designed to facilitate the acquisition, processing, and visualization of experimental data. The primary focus is on performing polynomial regression analysis on data obtained via serial communication, enabling users to model and interpret experimental results effectively.

## Features

- **Serial Data Acquisition**: Reads and stores experimental data from serial ports.
- **Polynomial Regression**: Fits data using polynomial models of varying degrees.
- **Data Visualization**: Generates plots showing raw data and fitted curves.
- **Modular Codebase**: Structured with reusable modules for clarity and maintainability.

## Directory Structure

FIS_4000/
├── Proyecto/
├── .vscode/
├── pycache/
├── data.dat
├── graph.py
├── main.py
├── readSerial.py
├── syssolver.py
├── values.py
├── xysums.py
├── *.pyc
├── *.png


- `main.py`: Main script for executing regression analysis and plotting.
- `readSerial.py`: Acquires experimental data via serial communication.
- `graph.py`: Contains functions for plotting and visualizing results.
- `syssolver.py`: Solves linear systems for regression coefficients.
- `values.py` and `xysums.py`: Utility scripts for data preparation.
- `data.dat`: Sample dataset for testing purposes.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Barreiro14/FIS_4000.git
   cd FIS_4000

    (Optional) Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

Install any required Python packages. If a requirements.txt file is missing, manually install packages like:

    pip install pyserial matplotlib numpy

Usage

    Collect Experimental Data

    Ensure your device is connected via USB. Configure the serial port in readSerial.py, then run:

python readSerial.py

This will create or update data.dat with experimental measurements.

Run Regression and Plot Results

After collecting data, run the main analysis pipeline:

    python main.py

    The script performs polynomial regression and saves plots as PNG files in the working directory.

Example Output

Example output plots (degree 2 and 3 regressions) will be saved in the directory and can be viewed directly. Plots illustrate the curve fitting over raw data points.
Contributing

Contributions are welcome. To propose changes:

    Fork this repository.

    Create a feature branch: git checkout -b feature/my-feature

    Commit your changes.

    Push to your fork.

    Open a pull request.

