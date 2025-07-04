Clipboard Manager 📋
A simple yet powerful menu bar utility for macOS that extends the system clipboard by allowing you to save and manage a history of copied items.

Description
This application lives in your macOS menu bar and keeps a running list of text snippets that you choose to save. It's designed for anyone who frequently needs to reuse multiple pieces of text, such as code snippets, email templates, or common links. Your clipboard history is automatically saved to your computer, so your items will still be there even after a restart.

Features
Persistent History: Automatically saves your clipboard history to a local file, so your items are always available.

Unlimited History: Save as many items as you need.

Menu Bar Access: Easily access your saved items from the macOS menu bar.

One-Click Copy: Simply click any item in the menu to copy it back to your system clipboard, ready to be pasted.

Selective Deletion: Enter "Delete Mode" to safely remove specific items from your history one by one.

Clear All: Instantly clear your entire clipboard history.

Requirements
To run the script directly or build the application, you will need:

Python 3

The following Python packages:

rumps

pyperclip

pyinstaller (for building the app)

You can install these using pip:

Bash

pip install rumps pyperclip pyinstaller
How to Use
There are two ways to use this application: running the script directly or building a standalone .app.

Option 1: Running the Script Directly
This is the easiest way to test and run the application without building it.

Grant Permissions: Before you start, you must give your Terminal application permission to read the clipboard.

Go to System Settings > Privacy & Security > Input Monitoring.

Add your Terminal app (e.g., Terminal.app or iTerm.app) to the list and ensure the switch next to it is ON.

Important: Completely quit and restart your Terminal for the changes to take effect.

Run the script: Open your Terminal, navigate to the project folder, and run:

Bash

python3 clipboard_manager.py
The 📋 icon will appear in your menu bar. The script will continue running in that terminal window.

Option 2: Building a Standalone Application
This process bundles the script and its dependencies into a standard macOS application (.app) that you can run from anywhere.

Navigate to Project Folder: Open your Terminal and go to the project directory where clipboard_manager.py is located.

Create the Build Configuration File: Run the following command to have PyInstaller generate a configuration file named Clipboard Manager.spec:

Bash

pyinstaller --name="Clipboard Manager" --windowed clipboard_manager.py
Edit the .spec File: Open the new Clipboard Manager.spec file. Delete all of its contents and replace it with the code below. This configuration is essential for a menu-bar-only app.

Python

# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['clipboard_manager.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Clipboard Manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Clipboard Manager',
)
app = BUNDLE(
    coll,
    name='Clipboard Manager.app',
    icon=None,
    bundle_identifier=None,
    info_plist={'LSUIElement': True},
)
Build the App: Run PyInstaller again, this time pointing to the .spec file:

Bash

pyinstaller "Clipboard Manager.spec" --noconfirm
Run Your App:

Find your new Clipboard Manager.app in the dist folder.

Drag it to System Settings > Privacy & Security > Input Monitoring and ensure it's enabled.

Double-click Clipboard Manager.app to launch it!

License
This project is licensed under the MIT License.