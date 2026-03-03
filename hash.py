import hashlib

def md5(s: str) -> str:
    """计算字符串的 MD5 哈希值

    Args:
        s (str): 输入字符串

    Returns:
        str: 字符串的 MD5 哈希值（32 位十六进制字符串）
    """
    
    return hashlib.md5(s.encode()).hexdigest()

def sha1(s: str) -> str:
    """计算字符串的 SHA-1 哈希值

    Args:
        s (str): 输入字符串

    Returns:
        str: 字符串的 SHA-1 哈希值（40 位十六进制字符串）
    """
    return hashlib.sha1(s.encode()).hexdigest()

def sha256(s: str) -> str:
    """计算字符串的 SHA-256 哈希值

    Args:
        s (str): 输入字符串

    Returns:
        str: 字符串的 SHA-256 哈希值（64 位十六进制字符串）
    """
    return hashlib.sha256(s.encode()).hexdigest()

def sha512(s: str) -> str:
    """计算字符串的 SHA-512 哈希值

    Args:
        s (str): 输入字符串

    Returns:
        str: 字符串的 SHA-512 哈希值（128 位十六进制字符串）
    """
    return hashlib.sha512(s.encode()).hexdigest()