import os


def get_folder_size(folder: str) -> int:
    """获取文件夹大小

    Args:
        folder (str): 要计算大小的文件夹路径

    Returns:
        int: 文件夹的总大小（字节）
    """
    total = 0
    for entry in os.scandir(folder):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_folder_size(entry.path)  # 递归子文件夹（如果需要）
    return total


def filter_windows_invalid_chars(s: str, o: str = "[x]") -> str:
    r"""将字符串中的 Windows 非法字符（\ / : * ? " < > |）全部替换为 指定内容

    Args:
        s (str): 输入字符串
        o (str, optional): 替换内容，默认为 "[x]"
    Returns:
        str: 替换后的字符串
    """
    invalid_chars = set(r'\/:*?"<>|')
    return "".join(o if c in invalid_chars else c for c in s)

def check_working_directory() -> str:
    """切换目录到脚本位置

    Returns:
        str: 脚本所在目录的路径
    """
    script_dir = os.path.normcase(os.getcwd())
    current_dir = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
    
    if script_dir != current_dir:
        os.chdir(current_dir)
    return current_dir