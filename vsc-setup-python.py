# VSCode Setup
# Set up Visual Studio Code with essential extensions for development in various languages
# github.com/smcclennon/vsc-setup



import os  # Shell commands





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
#Package ID,Package description]
python_packages = [
    ['pylint', 'Linting and debugging for python in VS Code']
]





print('Set up Visual Studio Code with essential extensions for development in various languages')
print('Learn more: github.com/smcclennon/vsc-setup\n')





for position, extension in enumerate(vscode_extensions, start=1):
    print(f'\nInstalling VS Code extension: {extension[0]}... ({position}/{len(vscode_extensions)})')
    print(f'Description: {extension[1]}')
    os.system(f'code>nul --install-extension {extension[0]} --force')



for position, package in enumerate(python_packages, start=1):
    print(f'\nInstalling Python package: {package[0]}... ({position}/{len(python_packages)})')
    print(f'Description: {package[1]}')
    os.system(f'python -m pip install -U {package[0]} --user --quiet --quiet')





print(f'''\n\n\n\n\
All done!

What to do now:
1)  Right click your file and click "Open with Code"
    OR open VS Code and drag your file into the window
    OR open VS code and press CTRL+O, then select the file you want to open

2)  Press CTRL+K CTRL+T, and then select the theme you want to apply
    (my favourite is 'Palenight italic')



To learn more about the true power of the extensions you just installed, visit the GitHub Repo!

GitHub Repo: {clr('github.com/smcclennon/vsc-setup', 'brown')}
''')





# Animate the print of a separator -------
from time import sleep
print('     ', end='')
for _ in range(45):
    print('-', end='', flush=True)
    sleep(0.001)



print('\n     > Press enter to launch Visual Studio Code <')
sleep(0.1)
print(f'               {clr("Made with", "cyan")} <3 {clr("by Shiraz", "cyan")}')
input('')



print('Launching Visual Studio Code...')
os.system('code') # Launch VS code