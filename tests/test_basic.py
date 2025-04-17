def test_import():
    """Test that the package can be imported."""
    import abbey_is_home1
    assert abbey_is_home1.__version__
    
def test_version():
    """Test that version is set correctly."""
    import abbey_is_home1
    assert abbey_is_home1.__version__ == "0.1.0"