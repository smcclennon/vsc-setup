# Visual Studio Code - Setup for Development
Small scripts which install essential VS Code extensions for development in various languages.

## Download
To download, click on the `language` you would like to install, and then press CTRL+S to save the raw page

*For example: Click on `Python` (you will be sent to the RAW page of the file, simply pure code), then press CTRL+S, and save the code.*

The scripts support python 3.6+, and have only been tested on Windows 10.

[vscm_ms-python.python]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vscm_CoenraadS.bracket-pair-colorizer-2]: https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2
[vscm_oderwat.indent-rainbow]: https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow
[vscm_whizkydee.material-palenight-theme]: https://marketplace.visualstudio.com/items?itemName=whizkydee.material-palenight-theme

[vscm_tht13.html-preview-vscode]: https://marketplace.visualstudio.com/items?itemName=tht13.html-preview-vscode
[vscm_naumovs.color-highlight]: https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight
[vscm_pranaygp.vscode-css-peek]: https://marketplace.visualstudio.com/items?itemName=pranaygp.vscode-css-peek


|Development language|Extensions installed|Why the extension has been deemed *essential*
|:-|:-|:-|
|[**`Python`**](vsc-setup-python.py)|[ms-python.python][vscm_ms-python.python]|Linting (incorrect syntax highlighting) and debugging for Python</br></br>To debug (run) your Python code, press `F5` whilst viewing your code and a terminal will pop up at the bottom of your screen with your running code output|
||[CoenraadS.bracket-pair-colorizer-2][vscm_CoenraadS.bracket-pair-colorizer-2]|Colourise brackets (amazing for when you (nest(brackets)))|
||[oderwat.indent-rainbow][vscm_oderwat.indent-rainbow]|Colourise indents|
||[whizkydee.material-palenight-theme][vscm_whizkydee.material-palenight-theme]|My favourite theme to code with in VS Code (juicy and purple)</br></br>To change your theme in VS Code, press `CTRL+K` `CTRL+T`, and you will be presented with a list of installed themes|
||||
|[**`HTML`**](vsc-setup-html.py)|[tht13.html-preview-vscode][vscm_tht13.html-preview-vscode]|Provides ability to preview HTML documents **live**</br></br>To open the HTML preview, whilst viewing your HTML document in VS Code, press `Ctrl+Shift+V` (or right click the tab > Open Preview).</br>A new tab will open in VS Code with a **live** preview of your code. You can drag the tab to the side of VS Code to split screen yout HTML code and preview|
||[naumovs.color-highlight][vscm_naumovs.color-highlight]|Highlight web colours in your editor|
||[pranaygp.vscode-css-peek][vscm_pranaygp.vscode-css-peek]|Peak into css classes by hovering over them (in HTML)|
||[whizkydee.material-palenight-theme][vscm_whizkydee.material-palenight-theme]|My favourite theme to code with in VS Code (juicy and purple)</br></br>To change your theme in VS Code, press `CTRL+K` `CTRL+T`, and you will be presented with a list of installed themes|


## Story
I made these scripts for computer science and BTEC IT students at my college who will need to develop in Python and use HTML.

Previously, they have used IDLE and Notepad++ (even though VS Code has been installed on the computers).

The computer teachers now realise how much VS Code could benefit students with development in comparison to IDLE and Notepad++.

The problem in the past has been that users appdata folders reset when logging out, so when launching VS Code next time, all previously installed extensions will no longer be installed.

This was inconvenient enough to discourage students from using VS Code, especially those less technically inclined.

**Because of this, I created this repository, where python scripts which will run a few OS commands and install extensions I believe are either necessary for, or greatly improve development in Visual Studio Code.**

## Screenshot
![vsc-setup-python](https://smcclennon.github.io/assets/images/screenshots/vsc-setup/vsc-setup-python.png)
*Created with <3 by Shiraz, using Python 3.9 on Windows 10*