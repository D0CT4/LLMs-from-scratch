#!/usr/bin/env python3
# Copyright (c) Sebastian Raschka under Apache License 2.0 (see LICENSE.txt).
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch

"""
Termux-specific environment check for LLMs-from-scratch project.
This script verifies that essential packages are installed and working correctly
in the Termux Android environment.
"""

import os
import platform
import sys
from importlib.metadata import PackageNotFoundError, import_module, version as get_version


def check_termux_environment():
    """Check if running in Termux environment."""
    termux_indicators = [
        os.environ.get('PREFIX', '').startswith('/data/data/com.termux'),
        'com.termux' in os.environ.get('PREFIX', ''),
        os.path.exists('/data/data/com.termux'),
        'termux' in platform.platform().lower()
    ]
    
    if any(termux_indicators):
        print("[OK] Running in Termux environment")
        return True
    else:
        print("[INFO] Not detected as Termux environment (this is OK if running elsewhere)")
        return False


def check_python_version():
    """Check Python version compatibility."""
    python_version = platform.python_version()
    if platform.python_version_tuple()[0] != '3':
        print(f"[FAIL] Python 3.x required, found {python_version}")
        return False
    elif int(platform.python_version_tuple()[1]) < 9:
        print(f"[WARN] Python 3.9+ recommended, found {python_version}")
        return True
    else:
        print(f"[OK] Python version {python_version}")
        return True


def check_storage_space():
    """Check available storage space."""
    try:
        import shutil
        total, used, free = shutil.disk_usage('.')
        free_gb = free / (1024**3)
        if free_gb < 1:
            print(f"[WARN] Low storage space: {free_gb:.1f}GB available")
        else:
            print(f"[OK] Storage space: {free_gb:.1f}GB available")
        return True
    except Exception as e:
        print(f"[INFO] Could not check storage space: {e}")
        return True


def check_core_packages():
    """Check core packages required for LLMs-from-scratch."""
    required_packages = {
        'torch': '2.2.2',
        'numpy': '1.26',
        'pandas': '2.2',
        'matplotlib': '3.7',
        'tqdm': '4.66',
        'tiktoken': '0.5'
    }
    
    optional_packages = {
        'jupyterlab': '4.0',
        'tensorflow': '2.16'
    }
    
    success = True
    
    print("\nChecking core packages:")
    for package, min_version in required_packages.items():
        try:
            module = import_module(package)
            version = getattr(module, '__version__', None)
            if version is None:
                try:
                    version = get_version(package)
                except PackageNotFoundError:
                    version = 'unknown'
            
            print(f"[OK] {package} {version}")
        except ImportError:
            print(f"[FAIL] {package} not found")
            success = False
    
    print("\nChecking optional packages:")
    for package, min_version in optional_packages.items():
        try:
            module = import_module(package)
            version = getattr(module, '__version__', None)
            if version is None:
                try:
                    version = get_version(package)
                except PackageNotFoundError:
                    version = 'unknown'
            
            print(f"[OK] {package} {version}")
        except ImportError:
            print(f"[INFO] {package} not found (optional)")
    
    return success


def check_torch_functionality():
    """Test basic PyTorch functionality."""
    try:
        import torch
        # Test tensor creation
        x = torch.tensor([1, 2, 3])
        y = x + 1
        
        # Check if CUDA is available (will be False in Termux)
        cuda_available = torch.cuda.is_available()
        if cuda_available:
            print("[INFO] CUDA is available")
        else:
            print("[INFO] CUDA not available (expected in Termux)")
        
        print("[OK] PyTorch basic functionality works")
        return True
    except Exception as e:
        print(f"[FAIL] PyTorch functionality test failed: {e}")
        return False


def check_memory():
    """Check available system memory."""
    try:
        import psutil
        memory = psutil.virtual_memory()
        available_gb = memory.available / (1024**3)
        total_gb = memory.total / (1024**3)
        
        if available_gb < 1:
            print(f"[WARN] Low memory: {available_gb:.1f}GB available of {total_gb:.1f}GB total")
        else:
            print(f"[OK] Memory: {available_gb:.1f}GB available of {total_gb:.1f}GB total")
        return True
    except ImportError:
        print("[INFO] psutil not available, cannot check memory")
        return True
    except Exception as e:
        print(f"[INFO] Could not check memory: {e}")
        return True


def print_termux_tips():
    """Print helpful tips for Termux users."""
    print("\n" + "="*60)
    print("TERMUX-SPECIFIC TIPS:")
    print("="*60)
    print("1. Grant storage access: termux-setup-storage")
    print("2. Keep session active: pkg install termux-api")
    print("3. For large models, close other apps to free RAM")
    print("4. Use 'pkg install nano vim' for text editing")
    print("5. Monitor battery usage during long operations")
    print("6. Consider using smaller batch sizes in examples")
    print("7. Jupyter Lab: jupyter lab --ip=0.0.0.0 --no-browser")
    print("="*60)


def main():
    """Main environment check function."""
    print("Termux Environment Check for LLMs-from-scratch")
    print("=" * 50)
    
    all_checks_passed = True
    
    # Run all checks
    check_termux_environment()
    all_checks_passed &= check_python_version()
    all_checks_passed &= check_storage_space()
    all_checks_passed &= check_core_packages()
    all_checks_passed &= check_torch_functionality()
    all_checks_passed &= check_memory()
    
    print("\n" + "="*50)
    if all_checks_passed:
        print("[SUCCESS] Environment check completed successfully!")
        print("You should be able to run the LLMs-from-scratch examples.")
    else:
        print("[ISSUES FOUND] Some checks failed.")
        print("Please review the output above and install missing packages.")
    
    print_termux_tips()


if __name__ == "__main__":
    main()