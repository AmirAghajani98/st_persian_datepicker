def test_import_date_picker():
    """Import the package and ensure date_picker is importable and callable.

    This test verifies the package can be imported in CI and that the
    `date_picker` symbol exists (smoke-test for packaging/importability).
    """
    try:
        from st_persian_datepicker import date_picker
    except Exception as e:
        raise AssertionError(f"Importing st_persian_datepicker failed: {e}")

    assert callable(date_picker), "date_picker should be callable"
