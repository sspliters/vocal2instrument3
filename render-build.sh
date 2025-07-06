#!/usr/bin/env bash

# Install system dependencies (like fluidsynth)
apt-get update && apt-get install -y libfluidsynth1

# Then install Python dependencies
pip install -r requirements.txt
