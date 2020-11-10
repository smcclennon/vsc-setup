# Set up vs-code for python development
# github.com/smcclennon



import os



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





print('Set up Visual Studio Code for Python development with one click\n')





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





print('''\n\n\n\n\
All done!

What to do now:
1)  Right click your python file and click "Open with Code"
    OR open VS Code and drag your file into the window
    OR open VS code and press CTRL+O, then select the python file you want to edit/run

2)  [Optional] Press CTRL+K CTRL+T, and then select the theme you want to apply (my favourite is 'Palenight italic')

3)  Edit your python file to your hearts content. If you want to know what a module does, (such as print()),
    simply hover over it and you'll be presented with loads of information and options you can choose from

4)  When you're ready to try running your code (it is very rare for your code to work first time, don't worry),
    simply press F5 and you should see a powershell terminal open up on the bottom of your VS code window
    running your code


TLDR;
1) Right click your python file and press "Open with code"
2) Press CTRL+K CTRL+O to choose a theme (my favourite is 'Palenight Italic')
3) Hover over modules such as print() to learn more about them
4) Press F5 to run your code
''')



input('     > Press enter to launch Visual Studio Code <\n               Made with <3 by Shiraz\n')


print('Launching Visual Studio Code...')
os.system('code') # Launch VS code