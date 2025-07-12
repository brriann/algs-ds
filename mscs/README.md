# omscs

Data Structures and Algorithms practice during MSCS

# dev environment

1. create a python virtual environment and install python requirements

```bash
python3 -m venv ~/.venvs/algs
source ~/.venvs/algs/bin/activate
pip install -r ~/dev/algs-ds/omscs/requirements.txt
```

2. install Python & Python Debugger VSCode extensions

- https://code.visualstudio.com/docs/python/debugging

3. create a debugging config in ~/.vscode/launch.json file 

```json
{
    "name": "Python Debugger: Current File",
    "type": "debugpy",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal"
},
```

4. associate VS Code with venv

- Ctrl + Shift + P
- Select Python Interpreter
- ~/.venv/algs/bin





