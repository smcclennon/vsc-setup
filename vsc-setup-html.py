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
    ['tht13.html-preview-vscode', 'Preview HTML documents'],
    ['ritwickdey.liveserver', 'Create a local server with real-time updating to emulate webserver environment'],
    ['naumovs.color-highlight', 'Highlight web colours (Ctrl+Shift+V)'],
    ['pranaygp.vscode-css-peek', 'Peak into css classes'],
    ['whizkydee.material-palenight-theme', 'Beautiful purple theme']
]





print('Set up Visual Studio Code with essential extensions for development in various languages')
print('Learn more: github.com/smcclennon/vsc-setup\n')





for position, extension in enumerate(vscode_extensions, start=1):
    print(f'\nInstalling VS Code extension: {extension[0]}... ({position}/{len(vscode_extensions)})')
    print(f'Description: {extension[1]}')
    os.system(f'code>nul --install-extension {extension[0]} --force')





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
