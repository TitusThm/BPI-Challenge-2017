# BPI Challenge 2017 Process Mining Analysis

This project analyzes the BPI Challenge 2017 event log using process mining techniques with pm4py.

## Files

- `overview.py` - Basic event log analysis and statistics
- `processDiscovery.py` - Process discovery using Directly-Follows Graph (DFG)
- `BPI Challenge 2017_1_all/` - Contains the event log data files

## Setup

1. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install pm4py pandas
```

3. Run the analysis:
```bash
python overview.py
python processDiscovery.py
```

## Data

The BPI Challenge 2017 dataset contains loan application processes. The event log includes:
- Loan application events
- Various process steps and activities
- Timestamps and case information

## Requirements

- Python 3.7+
- pm4py
- pandas
