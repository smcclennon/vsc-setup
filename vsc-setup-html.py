# Set up vs-code for HTML development
# github.com/smcclennon



import os



# VS Code extensions to install
# [Extension ID, Extension description]
vscode_extensions = [
    ['tht13.html-preview-vscode', 'Provides ability to preview HTML documents'],
    ['naumovs.color-highlight', 'Highlight web colours in your editor (Ctrl+Shift+V)'],
    ['pranaygp.vscode-css-peek', 'Peak into css ID and class strings'],
    ['whizkydee.material-palenight-theme', 'My favourite theme to code with in VS Code']
]






print('Set up Visual Studio Code for HTML development with one click\n')





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






print('''\n\n\n\n\
All done!

What to do now:
1)  Right click your HTML file and click "Open with Code"
    OR open VS Code and drag your file into the window
    OR open VS code and press CTRL+O, then select the HTML file you want to edit/run

2)  [Optional] Press CTRL+K CTRL+T, and then select the theme you want to apply (my favourite is 'Palenight italic')

3)  Edit your HTML file to your hearts content. If you want to know what a module does, (such as print()),
    simply hover over it and you'll be presented with loads of information and options you can choose from

4)  When you want to preview your HTML code, press CTRL+SHIFT+V or right click the tab in VSC and press 'Open Preview'


TLDR;
1) Right click your HTML file and press "Open with code"
2) Press CTRL+K CTRL+O to choose a theme (my favourite is 'Palenight Italic')
3) Hover over CSS classes to peak them
4) Press CTRL+SHIFT+V to open the HTML preview
''')



input('     > Press enter to launch Visual Studio Code <\n               Made with <3 by Shiraz\n')


print('Launching Visual Studio Code...')
os.system('code') # Launch VS code