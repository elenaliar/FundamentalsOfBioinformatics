#!/bin/bash

# Step 1: Create a virtual environment named 'venv'
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Upgrade pip (optional but recommended)
pip install --upgrade pip

# Step 4: Install requirements from requirements.txt
pip install -r requirements.txt

# Step 5: Deactivate virtual environment after installation (optional)
deactivate

echo "Setup complete! Run 'source venv/bin/activate' to activate the virtual environment."

# Run this in the command line
#chmod +x setup.sh