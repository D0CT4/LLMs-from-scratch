# Termux Setup for LLMs-from-scratch

This directory contains Android/Termux-specific setup instructions and tools for running the LLMs-from-scratch project on mobile devices.

## Files in this directory:

- **README.md**: Complete installation guide for Termux
- **setup.sh**: Automated setup script for quick installation
- **termux_environment_check.py**: Environment verification script specific to Termux

## Quick Start

1. **Manual Setup**: Follow the detailed instructions in [README.md](README.md)

2. **Automated Setup**: Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Verify Installation**:
   ```bash
   python termux_environment_check.py
   ```

## Notes

- This setup is designed specifically for the Termux Android terminal emulator
- Installation may take 30+ minutes depending on device and network speed
- Large models will run slowly on mobile hardware - this setup is primarily for educational use
- See the main [setup documentation](../README.md) for alternative installation methods

## Troubleshooting

If you encounter issues, first check:
1. You're using Termux from F-Droid (not Google Play)
2. Your device has sufficient storage space (4GB+ free)
3. Your internet connection is stable

For more detailed troubleshooting, see the README.md file in this directory.