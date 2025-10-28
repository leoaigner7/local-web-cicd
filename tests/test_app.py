def test_import_app():
    """Check if Flask app can be imported."""
    import importlib
    app_module = importlib.import_module("app.main")
    assert app_module is not None
