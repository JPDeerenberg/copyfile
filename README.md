# CopyFile - Clipboard File Copier

A simple command-line Python script that copies the contents of a text file to the clipboard. Works with Linux X11 environments and uses `tkinter` to interface with the clipboard.

## Features

- Copy the contents of a file to the clipboard.
- Trim whitespace before copying (optional).
- Print the file contents to stdout (optional).
- Verbose output for debugging (optional).
- Supports running the script with a simple `copyfile` command after setup.

## Prerequisites

- Python 3.x
- X11 (for clipboard access)
- Tkinter (for clipboard management with X11)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JPDeerenberg/copyfile
cd copyfile
```

### 2. Make the script executable

```bash
chmod +x copyfile.py
```

### 3. Rename the script (optional)

```bash
mv copyfile.py copyfile
```

### 4. Add the script to your PATH

To run the `copyfile` command from anywhere, you need to add it to your system's `PATH`.

#### Option 1: Move the script to a directory in your `PATH` (e.g., `/usr/local/bin`)

```bash
sudo mv copyfile /usr/local/bin/
```

#### Option 2: Add the current directory to your `PATH`

Add this line to your shell config (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export PATH=$PATH:/path/to/your/script/directory
```

Then source the file:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

## Usage

Once installed, you can use the script from the command line.

### Basic Command

```bash
copyfile filename.txt
```

Copies the contents of `filename.txt` to the clipboard.

### Optional Flags

- `--trim`: Trim whitespace before copying.
- `--print`: Print file contents to stdout.
- `-v`, `--verbose`: Show verbose output during copying.

Example:

```bash
copyfile filename.txt --trim --verbose
```

### Error Handling

- The script checks for missing or unreadable files.
- It ensures you're running in an X11 environment with the `DISPLAY` variable set.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.