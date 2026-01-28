# Clinker GUI - Gene Cluster Comparison Visualization Tool

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

**A modern GUI interface for the [clinker](https://github.com/gamcil/clinker) command-line tool**

Making gene cluster comparison accessible to researchers unfamiliar with command-line interfaces

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation-guide) • [Usage](#-usage-guide) • [FAQ](#-faq)

</div>

---

## 📖 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation Guide](#-installation-guide)
  - [Step 1: Install Python](#step-1-install-python)
  - [Step 2: Install Clinker](#step-2-install-clinker)
  - [Step 3: Install GUI Dependencies](#step-3-install-gui-dependencies)
- [Usage Guide](#-usage-guide)
  - [Starting the Program](#starting-the-program)
  - [Adding Files](#adding-files)
  - [Configuring Parameters](#configuring-parameters)
  - [Running Analysis](#running-analysis)
- [Advanced Features](#-advanced-features)
- [Building Executable](#-building-standalone-executable)
- [Changelog](#-changelog)
- [FAQ](#-faq)
- [Support](#-support)

---

## ✨ Features

### Core Functionality

- 🌍 **Multilingual** - Automatic language detection (Chinese/English) with manual switcher
- 🎨 **Modern Interface** - Built with CustomTkinter, dark mode support
- 🖱️ **Drag & Drop** - Drag files directly to window, no need to browse
- ⚙️ **Visual Configuration** - Configure all clinker parameters graphically
- 📊 **Real-time Log** - Display running process without freezing
- 🚀 **Async Execution** - Background processing keeps GUI responsive
- 🌐 **Path Compatible** - Handles paths with spaces and non-ASCII characters

### User Experience (v1.2 - v2.0)

- 📜 **Scrollable Panels** - Resize window freely, access content via scrollbar
- 👻 **No Console Window** - No black command window pops up during execution
- 💾 **Intelligent Logging** - Distinguishes INFO from ERROR messages
- 🎯 **Quick Open** - Open HTML results in browser with one click

---

## 🚀 Quick Start

**If you already have Python and Clinker installed**, just 3 steps:

```bash
# 1. Navigate to project directory
cd clinker-gui

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the program
python clinker_gui.py
```

Or simply **double-click** the `ClinkerGUI.bat` file!

---

## 📦 Installation Guide

**Complete beginner? Follow these step-by-step instructions!**

### Step 1: Install Python

#### 1.1 Download Python

Visit Python official website: https://www.python.org/downloads/

- Recommended version: Python 3.9 or higher (supports 3.7+)
- Select **Windows installer (64-bit)** for download

#### 1.2 Install Python

1. Double-click the downloaded installer (e.g., `python-3.9.X-amd64.exe`)
2. ⚠️ **Important**: Check the **"Add Python to PATH"** option
3. Click **"Install Now"** to begin installation
4. Wait for completion, click **"Close"**

#### 1.3 Verify Installation

Open Command Prompt (press `Win + R`, type `cmd`, press Enter), then type:

```bash
python --version
```

If it displays something like `Python 3.9.X`, installation succeeded!

If it says "not recognized as an internal or external command":
- Reinstall Python, ensure "Add Python to PATH" is checked
- Or manually add Python to system environment variables

---

### Step 2: Install Clinker

Clinker is the actual gene cluster comparison tool. Two installation methods:

#### Method A: Install via npm (Recommended)

**Prerequisite**: Needs Node.js installed first

1. **Download Node.js**
   - Visit: https://nodejs.org/
   - Download LTS version (Long Term Support)
   - Use default options during installation

2. **Install Clinker**
   ```bash
   npm install -g clinker
   ```

3. **Verify Installation**
   ```bash
   clinker --version
   ```

#### Method B: Install via pip

```bash
pip install clinker-py
```

Verify installation:
```bash
clinker --version
```

**Note**:
- Method A (npm) installs JavaScript version, receives faster updates
- Method B (pip) installs Python version, no need for Node.js
- **Both methods work**, this GUI supports both

---

### Step 3: Install GUI Dependencies

#### 3.1 Navigate to Project Directory

```bash
cd /path/to/clinker-gui
```

Or in File Explorer:
1. Open the project folder
2. Type `cmd` in the address bar, press Enter

#### 3.2 Install Dependencies

**Method 1: Using requirements.txt (Recommended)**

```bash
pip install -r requirements.txt
```

**Method 2: Manual Installation**

```bash
pip install customtkinter tkinterdnd2
```

#### 3.3 Verify Installation

```bash
python -c "import customtkinter; import tkinterdnd2; print('Dependencies installed successfully!')"
```

If it displays "Dependencies installed successfully!", you're ready to run the program!

---

## 📖 Usage Guide

### Starting the Program

**Method 1: Double-click (Simplest)**

Double-click the `ClinkerGUI.bat` file in the folder

**Method 2: Command Line**

```bash
cd /path/to/clinker-gui
python clinker_gui.py
```

The program will start and display the main window:

```
┌─────────────────────────────────────────────────────────┐
│    Clinker GUI - Gene Cluster Comparison Tool           │
│    Language: [English ▼]                                │
├──────────────────────┬──────────────────────────────────┤
│ 📁 Input Files       │ 🚀 Execution Control             │
│ [Drag Area]          │ [▶️ Start Analysis]              │
│ [📂 Browse Files]    │                                  │
│                      │ 📋 Run Log                       │
│ Selected Files:      │ ┌──────────────────────────────┐ │
│ 1. file1.gbk         │ │ Welcome to Clinker GUI!      │ │
│ 2. file2.gbk         │ │ Please add .gbk or .gb...    │ │
│                      │ │                              │ │
│ ⚙️ Parameters        │ │                              │ │
│ Identity: [━━━] 0.30 │ │                              │ │
│ Output: [________]   │ │                              │ │
│ Dir: [________] 📁   │ │                              │ │
│                      │ │                              │ │
│ ▶ Advanced Options   │ │                              │ │
└──────────────────────┴──────────────────────────────────┘
```

---

### Adding Files

#### Method 1: Drag & Drop (Recommended)

1. Find your genome files in File Explorer (`.gbk`, `.gb`, `.gff3`)
2. Select one or multiple files
3. Drag them directly to the "Drag Area" in the GUI
4. Files will be automatically added to the list

#### Method 2: Browse Files

1. Click the **"📂 Browse Files"** button
2. Select files in the dialog (hold `Ctrl` for multiple selection)
3. Click "Open" to confirm

#### Managing File List

- **Remove last file**: Click **"❌ Remove Selected"** button
- **Clear all files**: Click **"🗑️ Clear List"** button

**Supported file formats**:
- `.gbk` / `.gb` - GenBank format (most common)
- `.gff3` - GFF3 format (requires corresponding FASTA file)

---

### Configuring Parameters

#### Basic Parameters

**1. Sequence Identity**
- Slider range: 0.0 - 1.0
- Default: 0.30
- Description: Minimum sequence identity threshold, only shows gene links above this value
- Recommendations:
  - `0.3` - Permissive, shows more links
  - `0.5` - Moderate, balanced
  - `0.7+` - Strict, only highly similar genes

**2. Output Filename**
- Default format: `clinker_result_YYYYMMDD_HHMM.html`
- Customizable, `.html` extension added automatically
- Example: Enter `my_result` → generates `my_result.html`

**3. Output Directory**
- Default: Directory of the first input file
- Click 📁 button to customize save location

#### Advanced Options

Click **"▶ Advanced Options"** to expand:

| Option | Description | Default |
|--------|-------------|---------|
| Do not align clusters | Skip sequence alignment, only generate visualization | ❌ Unchecked |
| Use file order | Arrange by input file order instead of similarity | ❌ Unchecked |
| Hide link headers | Simplify visualization, hide column headers | ❌ Unchecked |
| Hide alignment headers | Hide cluster name headers | ❌ Unchecked |
| Force overwrite | Allow overwrite of existing result files | ✅ Checked |

---

### Running Analysis

#### Start Analysis

1. Confirm at least 2 files are added
2. Check parameter configuration is correct
3. Click **"▶️ Start Analysis"** button

#### During Execution

- Button changes to **"⏳ Running..."** and is disabled
- Progress bar animation appears
- Log area displays real-time running information:
  ```
  ============================================================
  🚀 Starting Clinker analysis...
  Command: clinker file1.gbk file2.gbk -i 0.3 -p result.html -f
  ============================================================
  
  [09:00:00] INFO - Starting clinker
  [09:00:00] INFO - Parsing files:
  [09:00:00] INFO -   file1.gbk
  [09:00:00] INFO -   file2.gbk
  [09:00:03] INFO - Starting cluster alignments
  [09:00:05] INFO - Building clustermap.js visualisation
  [09:00:05] INFO - Writing to: result.html
  [09:00:05] INFO - Done!
  
  ============================================================
  ✅ Analysis complete!
  Result file: C:\path\to\result.html
  ============================================================
  ```

#### After Completion

1. Completion dialog appears
2. Asks whether to open result immediately
   - Click **"Yes"** - Open result HTML in default browser
   - Click **"No"** - Open manually later
3. Or click **"📊 Open Result"** button anytime

---

## 🎯 Advanced Features

### Scrollable Window Support (v1.2)

**Problem**: Some components hidden when window is too small

**Solution**: Left panel supports scrolling
- Window can be freely resized to any size
- Scrollbar appears automatically when content exceeds window height
- Access all hidden content via scrollbar

**Operations**:
- Mouse wheel: Scroll on left panel
- Drag scrollbar: Directly drag the right-side scrollbar
- Touch screen: Swipe gestures

### No Console Window (v1.3)

**Before optimization**: Black command-line window pops up when clicking "Start Analysis"

**After optimization**: ✅ No extra windows during execution
- All output displayed in GUI log area
- More professional and cleaner interface
- Prevents user from accidentally closing console

**Technical implementation**:
```python
# Automatically hide console window on Windows
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = 0x08000000  # CREATE_NO_WINDOW
```

### Intelligent Log Display (v1.1)

**Before optimization**: clinker's INFO logs incorrectly marked as "errors"

**After optimization**: ✅ Intelligently determines real errors
- INFO logs displayed normally
- Only real errors marked as "⚠️ Error information"
- Detects keywords: ERROR, Traceback, Exception, FAILED

### Multilingual Interface (v2.0)

**Features**:
- ✅ Auto-detect system language (Chinese/English)
- ✅ Manual language switcher in top menu
- ✅ All interface text supports multiple languages
- ✅ Language preference remembered

**Usage**:
- Click language dropdown in top-right corner
- Select "中文" or "English"
- Interface instantly updates to selected language

---

## 📦 Building Standalone Executable

To distribute to colleagues without Python environment, package as `.exe` file.

### Install PyInstaller

```bash
pip install pyinstaller
```

### Build Commands

**Method 1: Directory Mode (Recommended, best compatibility)**

```bash
pyinstaller --windowed --name "ClinkerGUI" --hidden-import tkinterdnd2 --hidden-import tkinterdnd2.tkdnd clinker_gui.py
```

After building:
- Executable located at: `dist\ClinkerGUI\ClinkerGUI.exe`
- Distribute entire `dist\ClinkerGUI\` folder

**Method 2: Single File Mode (advanced)**

```bash
pyinstaller --onefile --windowed --name "ClinkerGUI" --hidden-import tkinterdnd2 --hidden-import tkinterdnd2.tkdnd --add-data "C:\Python39\Lib\site-packages\tkinterdnd2\tkdnd;tkdnd" clinker_gui.py
```

⚠️ **Note**: Replace `C:\Python39` with your actual Python installation path

### Distribution Notes

1. Send packaged folder/file to colleagues
2. **Important**: Recipients still need clinker installed
   ```bash
   npm install -g clinker
   # or
   pip install clinker-py
   ```
3. Double-click `ClinkerGUI.exe` to run

### Common Issues

**Q: Package shows missing tkdnd files?**
A: Use directory mode (Method 1) for better compatibility

**Q: Windows Defender flags as virus?**
A: Common with PyInstaller packages, add to trusted list

**Q: Program won't start after packaging?**
A:
1. Check all dependencies installed
2. Run from command line to see error messages
3. Use directory mode instead of single file

---

## 🔄 Changelog

### v2.0 (2026-01-28) - Current Version

**New**:
- ✅ Multilingual support: Chinese/English with auto-detection
- ✅ Language switcher in top menu bar
- ✅ All UI text supports multiple languages

**Improvements**:
- ✅ Better internationalization support
- ✅ Cross-platform compatibility enhanced

### v1.3 (2026-01-28)

**New**:
- ✅ Hidden console window: No black cmd window during execution
- ✅ Improved user experience: More professional appearance

**Technical**:
- Uses `subprocess.STARTUPINFO` and `CREATE_NO_WINDOW` flag
- Platform detection: Only applies on Windows

### v1.2 (2026-01-28)

**New**:
- ✅ Scrollbar support: Left panel is scrollable
- ✅ Free window resizing: No minimum size restriction
- ✅ Responsive layout: Access content via scrollbar

**Technical**:
- Uses `CTkScrollableFrame` instead of regular frame

### v1.1 (2026-01-28)

**Fixes**:
- ✅ Log error reporting: Intelligently distinguish INFO and ERROR
- ✅ Bat startup optimization: Cmd window auto-hides

### v1.0 (2026-01-28)

**Initial Release**:
- ✅ Basic GUI functionality
- ✅ Drag & drop support
- ✅ Parameter configuration panel
- ✅ Real-time log display
- ✅ Async execution

---

## ❓ FAQ

### Installation

**Q1: Error during pip dependency installation?**

A: Try these solutions:
```bash
# 1. Update pip
python -m pip install --upgrade pip

# 2. Use mirror (faster in some regions)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 3. Install packages individually
pip install customtkinter
pip install tkinterdnd2
```

**Q2: "clinker command not found"?**

A:
1. Verify clinker is installed: `clinker --version`
2. If not installed, run:
   - npm method: `npm install -g clinker`
   - pip method: `pip install clinker-py`
3. Restart command prompt and GUI

**Q3: Python still not recognized after installation?**

A:
1. Reinstall Python, ensure "Add Python to PATH" is checked
2. Or manually add to environment variables:
   - Right-click "This PC" → Properties → Advanced system settings
   - Environment Variables → System variables → Path
   - Add Python path (e.g., `C:\Python39\`)

### Usage

**Q4: Error with paths containing spaces or special characters?**

A: This program automatically handles this
- Uses absolute paths
- Forces UTF-8 encoding (`PYTHONUTF8=1`)
- If issues persist, check log for details

**Q5: GFF3 files not recognized?**

A: GFF3 files require matching FASTA files
- Ensure corresponding FASTA file exists in same directory
- Filenames must match (e.g., `cluster1.gff3` and `cluster1.fa`)
- Supported FASTA extensions: `.fa`, `.fsa`, `.fna`, `.fasta`, `.faa`

**Q6: Interface freezes during execution?**

A: Program uses async execution, shouldn't freeze normally
- Check if clinker is running properly
- View log area for details
- If freezes, restart program and check input files

**Q7: Analysis fails, no results generated?**

A: Check the following:
1. Verify input file format is correct (`.gbk`, `.gb`, `.gff3`)
2. Check log area for error messages
3. Confirm clinker is properly installed
4. Try running clinker manually from command line

**Q8: Window too small, can't see all content?**

A: ✅ Fixed in v1.2
- Left panel supports scrolling
- Use mouse wheel or drag scrollbar to view hidden content
- Window can be freely resized

**Q9: Black window pops up during execution?**

A: ✅ Fixed in v1.3
- Program automatically hides console window
- If still appears, ensure you're using latest version

### Packaging

**Q10: Error when running packaged exe?**

A:
1. Use directory mode for packaging (recommended)
2. Ensure `--hidden-import` parameters are correct
3. Check if tkdnd files are included
4. Run from command line to see detailed errors

**Q11: Antivirus blocks packaged exe?**

A:
- Common with PyInstaller packages
- Add program to antivirus whitelist
- Or use code signing certificate (for official releases)

---

## 💻 Technical Details

### Technology Stack

- **Python**: 3.7+
- **GUI Framework**: CustomTkinter 5.2+
- **Drag & Drop**: tkinterdnd2 0.4+
- **Process Management**: subprocess (standard library)
- **Threading**: threading (standard library)
- **Internationalization**: Built-in locale detection

### Special Handling

**Encoding**:
```python
os.environ["PYTHONUTF8"] = "1"  # Force UTF-8
```

**Path Handling**:
```python
cmd.extend(self.file_paths)  # List passing, avoid string concatenation
```

**Async Execution**:
```python
threading.Thread(target=self._execute_clinker, daemon=True).start()
```

**Hide Console** (Windows):
```python
if sys.platform == 'win32':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.wShowWindow = subprocess.SW_HIDE
    creationflags = 0x08000000  # CREATE_NO_WINDOW
```

**Language Detection**:
```python
system_lang = locale.getdefaultlocale()[0]
if system_lang.startswith('zh'):
    return 'zh_CN'
else:
    return 'en_US'
```

### Project Structure

```
clinker-gui/
├── clinker_gui.py              # Main program (single file)
├── requirements.txt            # Python dependencies
├── ClinkerGUI.bat             # Windows launch script
├── README.md                   # Main documentation
├── README_EN.md               # English documentation (this file)
├── README_CN.md               # Chinese documentation
├── Bug修复报告.md             # Bug fix history
└── 开发报告.md                # Development summary
```

---

## 📧 Support

### Get Help

- **Issue Reporting**: Submit an Issue or contact developer
- **Feature Requests**: Welcome to suggest improvements
- **Technical Discussion**: Share usage experiences

### References

- [Clinker GitHub](https://github.com/gamcil/clinker) - Original command-line tool
- [CustomTkinter Docs](https://github.com/TomSchimansky/CustomTkinter) - GUI framework
- [Python subprocess Docs](https://docs.python.org/3/library/subprocess.html) - Process management

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **[clinker](https://github.com/gamcil/clinker)** - Excellent gene cluster comparison tool
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern GUI framework
- **[tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)** - Drag and drop support

---

<div align="center">

**Developer**: CodeWong  
**Version**: 2.0 (International Edition)  
**Last Update**: 2026-01-28

**⭐ If this project helps you, please give it a star!**

</div>

