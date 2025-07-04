# Clipboard Manager 📋

A simple yet powerful menu bar utility for macOS that extends the system clipboard by allowing you to save and manage a history of copied items.

## Description

This application lives in your macOS menu bar and keeps a running list of text snippets that you choose to save. It's designed for anyone who frequently needs to reuse multiple pieces of text, such as code snippets, email templates, or common links. Your clipboard history is automatically saved to your computer, so your items will still be there even after a restart.

## Features

* **Persistent History**: Automatically saves your clipboard history to a local file, so your items are always available.
* **Unlimited History**: Save as many items as you need.
* **Menu Bar Access**: Easily access your saved items from the macOS menu bar.
* **One-Click Copy**: Simply click any item in the menu to copy it back to your system clipboard, ready to be pasted.
* **Selective Deletion**: Enter "Delete Mode" to safely remove specific items from your history one by one.
* **Clear All**: Instantly clear your entire clipboard history.

## How to Use

This application is built as a standalone `.app` file.

1.  **Grant Permissions:** Before you run the app for the first time, you must give it permission to read the clipboard.
    * Go to `System Settings > Privacy & Security > Input Monitoring`.
    * Drag `Clipboard Manager.app` into the list and ensure the switch next to it is **ON**.

2.  **Run the App:**
    * Double-click `Clipboard Manager.app` to launch it.
    * The 📋 icon will appear in your menu bar.

## Building from Source

To build the application from the source code, you will need:
* Python 3
* The following Python packages: `rumps`, `pyperclip`, `pyinstaller`

You can install these into a virtual environment and build using the provided `.spec` file.

```bash
# Navigate to the project folder
cd /path/to/ClipboardApp

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install rumps pyperclip pyinstaller

# Build the app
pyinstaller "Clipboard Manager.spec" --noconfirm