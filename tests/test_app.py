import os
import sys
import importlib

# Damit "app" importierbar ist:
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_import_app():
    """Check if Flask app can be imported."""
    app_module = importlib.import_module("app.main")
    assert app_module is not None
