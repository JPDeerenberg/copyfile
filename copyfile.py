#!/usr/bin/env python3
import sys
import os
import argparse
import tkinter as tk
from pathlib import Path

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Copy a file's contents to the clipboard.")
    parser.add_argument('filename', metavar='FILE', type=str, nargs='?', help="Text file to copy.")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    parser.add_argument('--print', action='store_true', help='Print file contents to stdout.')
    parser.add_argument('--trim', action='store_true', help='Trim whitespace before copying.')
    return parser.parse_args()

def read_file(path):
    """Read the file contents safely."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{path}'.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: The file '{path}' contains invalid characters that can't be decoded.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file '{path}': {e}")
        sys.exit(1)

def copy_to_clipboard(text, verbose=False):
    """Copy text to the clipboard using tkinter (X11 dependent)."""
    if 'DISPLAY' not in os.environ:
        raise EnvironmentError("X11 DISPLAY not found. Is DISPLAY set?")
    
    root = tk.Tk()
    root.withdraw()
    
    if verbose:
        print("Copying to clipboard...")
        
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()
    
    if verbose:
        print("Done.")

def check_file_existence(filepath):
    """Check if the file exists."""
    if not filepath.is_file():
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def read_and_process_file(filepath, trim=False, print_content=False):
    """Read the file and process it according to the arguments."""
    content = read_file(filepath)
    if trim:
        content = content.strip()
    if print_content:
        print(content)
    return content

def main():
    """Main function that orchestrates reading, processing, and copying the file."""
    args = parse_args()

    if not args.filename:
        print("Error: No file specified.")
        sys.exit(1)

    filepath = Path(args.filename)
    check_file_existence(filepath)

    content = read_and_process_file(filepath, trim=args.trim, print_content=args.print)
    copy_to_clipboard(content, verbose=args.verbose)

if __name__ == '__main__':
    main()
