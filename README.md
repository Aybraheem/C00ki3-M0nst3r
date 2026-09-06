<p align="center">
  <img src="CookieGrabber/images/C00ki3_M0nst3r.jpg" alt="C00ki3 M0nst3r Logo" width="800">
</p>

# 🍪 C00ki3 M0nst3r

**Version:** 1.0.0

A standalone Windows tool to extract `sessionid`, `csrftoken`, and `xsrftoken` cookies from popular browsers and websites.

---

## ⚠️ LEGAL DISCLAIMER

> **This tool is intended for educational purposes, security research, and recovering your own lost session tokens.**
> 
> - Do **not** use this tool on computers you do not own.
> - Do **not** use this tool without explicit written permission from the owner.
> - Unauthorized access to accounts is **illegal** under the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide.
> 
> **The author assumes zero liability for any misuse of this software.** You are solely responsible for how you use it.

---

## ✨ Features

- 🎯 Targets **24+ major websites** (Facebook, Instagram, Twitter/X, TikTok, Reddit, YouTube, Discord, Telegram, etc.).
- 🌐 Supports **9 browsers** (Chrome, Firefox, Edge, Brave, Opera, Vivaldi, Chromium, LibreWolf, Opera GX).
- 🔒 Automatically detects installed browsers and skips missing ones.
- 🛑 If a browser locks the cookie database, it prompts the user to close the browser automatically.
- 🖥️ **Standalone `.exe`** – No Python installation required on the target machine.
- 📋 Prints only the essential tokens (`sessionid`, `csrf`, `xsrf`) in a clean, readable format.
- ⏸️ Pauses after execution so users can read the output before the window closes.

---

## 📁 Project Structure

```
CookieGrabber/
├── script.py                       # Source code for developers and main python script
├── requirements.txt                # Dependencies for developers, Contains: browser_cookie3 (only lol)
├── images/                         # Logo and assets
│   └── C00ki3_Monst3r.jpg          # Project logo
├── executables/                    # ⬅️ THE EXE LIVES HERE
    └── C00ki3_M0nst3r.exe          # Standalone executable (no Python needed!)
```

---

## 🖥️ For End-Users (No Python Installed)

**You do NOT need Python installed to use this tool.**

1. Open the **`executables/`** folder.
2. **Double-click** `C00ki3_M0nst3r.exe`.
3. A black Command Prompt window will appear.
4. The tool will scan your browsers and display any found cookies.
5. **Press the `ENTER` key** when you are done reading to close the window.

> 💡 **Tip:** If you want to keep the output visible after the script finishes, open Command Prompt (`cmd`) first, navigate to the `executables/` folder, and run `C00ki3_M0nst3r.exe` manually. The window will stay open.

---

## 👨‍💻 For Developers (Running from Source)

If you want to run the Python script directly instead of using the `.exe`:

### Prerequisites
- Python 3.8 or higher installed.
- The target browsers must be installed on the system.

### Setup
1. Open a terminal in the project folder (where `script.py` is located).
2. Install the required dependency:
   ```bash
   pip install -r requirements.txt
   ```
   *(Or just run `pip install browser_cookie3`)*
3. Run the script:
   ```bash
   python script.py
   ```

---

## 🛠️ Building the `.exe` Yourself (First Time)

If you are building the executable from scratch for the first time:

### Step 1: Install PyInstaller
Open a terminal and run:
```bash
python -m pip install pyinstaller
```
*(If `python` doesn't work, try `py -m pip install pyinstaller`)*

### Step 2: Navigate to the project folder
Make sure your terminal is open in the folder where `script.py` is located.

### Step 3: Build the Executable
Run:
```bash
python -m PyInstaller --onefile --name C00ki3_M0nst3r script.py
```

### Step 4: Locate and Move Your `.exe`
After the build finishes, the new `.exe` will be inside the `dist/` folder. 
**Move it** to the `executables/` folder (overwrite the old one if it exists).

---

## 🔧 Customization: Adding More Websites + REBUILDING

Want to target additional websites? Follow this complete guide from start to finish:

1. **Open the script**  
   Open **`script.py`** in any text editor (VS Code, Notepad++, etc.).

2. **Locate the `websites` list**  
   Find this section near the top of the file:
   ```python
   websites = [
       'facebook.com',
       'instagram.com',
       'twitter.com',
       # ... existing sites ...
   ]
   ```

3. **Add your own websites**  
   Add your desired domain to the list. Make sure to wrap it in quotes and add a comma:
   ```python
   websites = [
       'facebook.com',
       'mynewwebsite.com',   # <-- ADD YOURS HERE
       'anothersite.com',    # <-- AND HERE
       # ...
   ]
   ```

4. **Save the file**  
   Press `Ctrl + S` to save your changes.

5. **Open your terminal**  
   Make sure you are in the project folder (where `script.py` is located).

6. **Rebuild the `.exe`**  
   Run the exact same PyInstaller command again:
   ```bash
   python -m PyInstaller --onefile --name C00ki3_M0nst3r script.py
   ```

7. **Replace the old executable**  
   Go to the `dist/` folder, copy the new `C00ki3_M0nst3r.exe`, and paste it into the **`executables/`** folder, replacing the old file.

> ⚠️ **CRITICAL:** You **must** rebuild the `.exe` every time you edit `script.py`. Changes do not apply to an already-built executable. You cannot edit a `.exe` file directly—only the source code (`script.py`), then rebuild.

---

## ⚙️ How It Works (Under the Hood)

1. The script loops through all supported browsers installed on your system.
2. For each browser, it attempts to read the cookie database for every website in the target list.
3. **If the browser is running and locks the database:**
   - You are prompted: *"Would you like to close the target's browser session?"*
   - Typing `yes` or `y` uses `taskkill` to force-close the browser and retry.
   - Typing `no` or `n` exits the script so you can close the browser manually.
4. Once cookies are successfully read, it filters and extracts:
   - `sessionid`
   - `csrftoken`
   - `xsrftoken`
5. The results are printed to the console in a pipe-delimited format for easy reading.

---

## 📝 Example Output

```
chrome | facebook.com | sessionid: abc123def456... | csrf: xyz789... | xsrf: None
firefox | instagram.com | sessionid: 987zyx... | csrf: None | xsrf: token123...
edge | twitter.com | sessionid: None | csrf: None | xsrf: None
```

---

## ❓ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"PermissionError" / Browser locked** | The browser is open and locking the cookie file. Type `yes` to let the tool close it, or close the browser manually and re-run. |
| **"pyinstaller is not recognized"** | Use `python -m PyInstaller --onefile --name C00ki3_M0nst3r script.py` instead of just `pyinstaller`. |
| **No cookies found** | Make sure you are actually logged into the website in that specific browser before running the tool. |
| **Chrome shows nothing even after logging in** | Try to update `browser_cookie3` with `pip install --upgrade browser_cookie3` and rebuild your `.exe`. Chrome recently changed its encryption. |
| **Window closes too fast** | The `input("GUI BUFFER...")` line is at the bottom of the script. If you removed it, add it back or run the `.exe` from an existing Command Prompt window. |
| **Antivirus flags the `.exe`** | PyInstaller executables are sometimes flagged by antivirus software due to the way they unpack themselves. This is a known false positive. Add the file to your antivirus exceptions if you trust the source. |

---

## 📜 License

This project is provided for **educational purposes only**. Use at your own risk. No warranty is provided.
