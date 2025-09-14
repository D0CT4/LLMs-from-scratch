# Installing LLMs-from-scratch on Android using Termux

This guide provides step-by-step instructions for setting up and running the LLMs-from-scratch project on Android devices using the Termux app.

## Prerequisites

1. **Install Termux**: Download and install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) or [GitHub Releases](https://github.com/termux/termux-app/releases)
   - **Note**: The Google Play Store version is outdated and not recommended

2. **Device Requirements**:
   - Android 7.0 (API level 24) or higher
   - At least 4GB of available storage space
   - 3GB+ RAM recommended for running models

## Installation Steps

Follow these commands in your Termux terminal:

### Step 1: Update Package Lists

```bash
pkg update && pkg upgrade
```

### Step 2: Install Essential Dependencies

```bash
pkg install python git clang make libjpeg-turbo libpng
```

### Step 3: Install Python Package Manager

```bash
pip install --upgrade pip
```

### Step 4: Install Additional System Dependencies

Some Python packages require compilation, so install build tools:

```bash
pkg install rust binutils-is-llvm
```

### Step 5: Clone the Repository

```bash
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git
cd LLMs-from-scratch
```

### Step 6: Install Python Dependencies

Install the required packages (this may take several minutes):

```bash
pip install -r requirements.txt
```

**Alternative method** if you encounter compilation issues:

```bash
# Install core dependencies one by one
pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip install numpy pandas matplotlib tqdm tiktoken jupyterlab
```

## Verification

Check your installation by running the environment verification script:

```bash
cd setup/02_installing-python-libraries
python python_environment_check.py
```

If successful, you should see output similar to:
```
[OK] Your Python version is 3.x.x
[OK] torch 2.2.2
[OK] numpy 1.26.x
[OK] pandas 2.2.x
...
```

## Running Jupyter Notebooks

To run the Jupyter notebooks:

1. Start JupyterLab:
   ```bash
   jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
   ```

2. Open your web browser and navigate to: `http://localhost:8888`
   
3. Use the token displayed in the terminal output to access JupyterLab

## Performance Considerations

- **CPU Only**: Termux runs on CPU only, so training large models will be slower than GPU-enabled environments
- **Memory**: Close other apps to free up RAM when running larger examples
- **Storage**: Models and datasets can be large; monitor available storage space
- **Battery**: Long-running processes will drain battery; consider keeping device plugged in

## Troubleshooting

### Common Issues and Solutions

**Issue**: `pkg update` fails with network errors
- **Solution**: Ensure stable internet connection and try again

**Issue**: PyTorch installation fails
- **Solution**: Use the CPU-only version:
  ```bash
  pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu
  ```

**Issue**: Jupyter notebook kernel crashes
- **Solution**: Reduce batch sizes in examples and close other apps to free RAM

**Issue**: `clang` compilation errors
- **Solution**: Install additional build dependencies:
  ```bash
  pkg install clang python-dev
  ```

**Issue**: Permission denied errors
- **Solution**: Termux apps run in user space; avoid using `sudo`

### Limited Functionality Notes

Some features may have limitations on Termux:
- TensorFlow may not install properly (PyTorch is recommended)
- Some visualization features might be limited
- Large model training will be significantly slower than desktop/server environments

## Additional Termux Tips

1. **Storage Access**: Grant Termux storage permission to access device files:
   ```bash
   termux-setup-storage
   ```

2. **Keep Session Active**: Install `termux-wake-lock` to prevent process termination:
   ```bash
   pkg install termux-api
   ```

3. **Text Editing**: Install a text editor for quick edits:
   ```bash
   pkg install nano vim
   ```

## Alternative: Using Termux with proot

For a more complete Linux environment, consider using proot-distro:

```bash
pkg install proot-distro
proot-distro install ubuntu
proot-distro login ubuntu
```

Then follow standard Ubuntu installation procedures within the proot environment.

## Support

If you encounter issues specific to Termux installation:

1. Check the [Termux documentation](https://termux.dev/en/)
2. Visit the main project [discussions forum](https://github.com/rasbt/LLMs-from-scratch/discussions)
3. Ensure you're using the latest version of Termux from F-Droid

---

**Note**: Running large language models on mobile devices is primarily for educational purposes and light experimentation. For serious development and training, consider using cloud platforms or desktop environments as described in the main [setup documentation](../README.md).