#!/usr/bin/env bash
# Quick setup script for LLMs-from-scratch on Termux
# This script automates the installation process described in README.md

set -e  # Exit on any error

echo "=========================================="
echo "LLMs-from-scratch Termux Setup Script"
echo "=========================================="
echo ""

# Check if running in Termux
if [[ ! "$PREFIX" =~ .*termux.* ]]; then
    echo "Warning: This script is designed for Termux. You may need to adapt commands for your environment."
    read -p "Continue anyway? (y/N): " continue_anyway
    if [[ ! "$continue_anyway" =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 1
    fi
fi

echo "Step 1: Updating package lists..."
pkg update -y

echo ""
echo "Step 2: Installing essential dependencies..."
pkg install -y python git clang make libjpeg-turbo libpng rust binutils-is-llvm

echo ""
echo "Step 3: Upgrading pip..."
pip install --upgrade pip

echo ""
echo "Step 4: Installing Python dependencies..."
echo "This may take several minutes, especially for PyTorch..."

# Try to install requirements.txt first
if [ -f "../../requirements.txt" ]; then
    echo "Installing from requirements.txt..."
    pip install -r ../../requirements.txt
else
    echo "requirements.txt not found, installing core packages individually..."
    
    # Install PyTorch first (CPU-only for Termux)
    echo "Installing PyTorch (CPU-only)..."
    pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu
    
    # Install other core dependencies
    echo "Installing other dependencies..."
    pip install numpy pandas matplotlib tqdm tiktoken jupyterlab
    
    # Optional packages
    echo "Installing optional packages..."
    pip install psutil || echo "Warning: psutil installation failed (optional)"
fi

echo ""
echo "Step 5: Setting up storage access..."
echo "You may be prompted to grant storage permission."
termux-setup-storage || echo "Note: termux-setup-storage failed or not available"

echo ""
echo "=========================================="
echo "Installation completed!"
echo "=========================================="
echo ""
echo "To verify your installation, run:"
echo "  python termux_environment_check.py"
echo ""
echo "To start JupyterLab, run:"
echo "  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
echo ""
echo "For more information, see README.md in this directory."
echo "=========================================="