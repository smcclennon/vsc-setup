# VSCode Setup
# Set up Visual Studio Code with essential extensions for development in various languages
# github.com/smcclennon/vsc-setup



import os





# Colours! (just aesthetic)
# More colour codes: https://gist.github.com/smcclennon/a42e2e3819a01d2429a430fb57d545c0
colours = dict(  # ANSI colour codes
    BROWN = "\033[0;33m",
    CYAN = "\033[0;36m",
    END = "\033[0m"
)

def clr(body, colour_code):
    colour_code = colour_code.upper()
    if colour_code in colours:
        return colours[colour_code]+body+colours["END"]
    else:
        return body





# VS Code extensions to install
# [Extension ID, Extension description]
vscode_extensions = [
    ['ms-python.python', 'Linting (incorrect syntax highlighting) and debugging for Python (press F5 in VSC to debug)'],
    ['CoenraadS.bracket-pair-colorizer-2', 'Colourise brackets (amazing for when you (nest(brackets)))'],
    ['oderwat.indent-rainbow', 'Colourise indents'],
    ['whizkydee.material-palenight-theme', 'My favourite theme to code with in VS Code']
]



# Python packages to install
python_packages = [
    ['pylint', 'Linting and debugging for python in VS Code']
]





print('Set up Visual Studio Code with essential extensions for development in various languages')
print('Learn more: github.com/smcclennon/vsc-setup\n')





# Install VS Code extensions
# Command breakdown:
# 'code' call the Visual Studio Code executable
# '>nul' Windows shell feature to prevent any output (VS Code does not have a --quiet flag)
# '--install-extension' specify the extension ID to install
# 'extension[0]' == extension ID
# 'extension[1]' == extension description
# '--force' avoid any prompts asking you if you're sure
for extension in vscode_extensions:
    print(f'\nInstalling VS Code extension: {extension[0]}...')
    print(f'Description: {extension[1]}')
    os.system(f'code>nul --install-extension {extension[0]} --force')



# Install/update Python package in your user data folder (so elevated permissions are not required to write to C:\)
# Command breakdown:
# 'python' call the Python executable
# '-m pip' use the 'pip' module
# '-U' update if already installed
# 'package[0]' == package ID
# 'package[1]' == package description
# '--user' install into user data folder (not public program files)
# '--quiet' hide spammy loading bars, only show warning, error, and critical log levels
for package in python_packages:
    print(f'\nInstalling Python package: {package[0]}')
    print(f'Description: {package[1]}')
    os.system(f'python -m pip install -U {package[0]} --user --quiet')





print(f'''\n\n\n\n\
All done!

What to do now:
1)  Right click your HTML file and click "Open with Code"
    OR open VS Code and drag your file into the window
    OR open VS code and press CTRL+O, then select the HTML file you want to edit/run

2)  Press CTRL+K CTRL+T, and then select the theme you want to apply
    (my favourite is 'Palenight italic')



To learn more about the true power of the extensions you just installed, visit the GitHub Repo!

GitHub Repo: {clr('github.com/smcclennon/vsc-setup', 'brown')}
''')





# Animate the print of a separator -------
from time import sleep
print('     ', end='')
for i in range(45):
    print('-', end='', flush=True)
    sleep(0.001)



print('\n     > Press enter to launch Visual Studio Code <')
sleep(0.1)
print(f'               {clr("Made with", "cyan")} <3 {clr("by Shiraz", "cyan")}')
input('')



print('Launching Visual Studio Code...')
os.system('code') # Launch VS code