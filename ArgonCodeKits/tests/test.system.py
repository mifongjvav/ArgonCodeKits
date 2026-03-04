from ArgonCodeKits import (
    filter_windows_invalid_chars,
    get_folder_size,
)

def test_filter_invalid_chars():
    s = 'test<>:"/\\|?*'
    result = filter_windows_invalid_chars(s, "_")
    assert "<" not in result
    assert ">" not in result

def test_get_folder_size(tmp_path):
    file = tmp_path / "a.txt"
    file.write_text("12345")
    size = get_folder_size(str(tmp_path))
    assert size == 5