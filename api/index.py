import os
import sys
from pathlib import Path

# Ensure the project directory is on sys.path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentproject.settings')

from studentproject.wsgi import app
