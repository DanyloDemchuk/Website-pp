gitignore_content = """
# Python ігнорування
*.pyc
*.pyo
*.pyd
__pycache__/
*.env
*.venv
.env
.venv
venv/
ENV/
env/
env.bak/
venv.bak/
*.egg
*.egg-info/
dist/
build/
eggs/
parts/
var/
*.log
*.pot
*.py[cod]
*.sqlite3
*.coverage
*.mypy_cache/
.dmypy.json
.pytest_cache/
cover/
docs/_build/
*.mo
*.pot
*.log
*.log/
*.pot

# Django ігнорування
*.sqlite3
db.sqlite3
/static/
static/
media/
local_settings.py

# MacOS ігнорування
.DS_Store

# Windows ігнорування
Thumbs.db
ehthumbs.db
Desktop.ini

# VS Code
.vscode/

# PyCharm
.idea/
"""

# Створення та запис файлу .gitignore
with open('.gitignore', 'w') as file:
    file.write(gitignore_content)

print("Файл .gitignore створено і налаштовано.")