import logging
import random
import base64

space = " " * 100

def input(prompt: str, level: str = "info") -> str:
    """显示提示信息并记录日志，然后获取用户输入并记录。

    Args:
        prompt (str): 提示信息
        level (str): 日志等级，可选值：debug, info, warning, error, critical

    Returns:
        str: 用户输入的文本
    """
    level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    log_level = level_map.get(level.lower(), logging.INFO)

    # 记录提示信息（纯文本，不含控制字符）
    logging.log(log_level, f"提示信息：{prompt}")

    # 获取用户输入
    user_input = __builtins__.input(prompt)

    # 记录用户输入
    logging.log(log_level, f"用户输入：{user_input}")

    return user_input


def encrypt(text: str, password: str, rounds: int = 10) -> bytes:
    """混淆：文本 -> 多次base64 + 打乱
    
    Args:
        text (str): 需要加密的文本
        password (str): 用于生成随机种子的密码
        rounds (int): 加密轮数

    Returns:
        str: 加密后的数据
    """
    data = text.encode('utf-8')
    for i in range(rounds):
        # 每轮使用独立的随机生成器，种子 = 密码 + 轮次
        r = random.Random(password + str(i))
        # base64编码
        data = base64.b64encode(data)
        # 转列表打乱
        chars = list(data)
        r.shuffle(chars)
        data = bytes(chars)
    return data


def decrypt(ciphertext: bytes, password: str, rounds: int = 10) -> str:
    """反混淆：恢复打乱顺序 + base64解码
    Args:
        ciphertext (bytes): 加密后的数据
        password (str): 用于生成随机种子的密码
        rounds (int): 加密轮数
        
    Returns:
        str: 解密后的文本
    """
    data = ciphertext
    for i in range(rounds - 1, -1, -1):  # 从最后一轮逆向操作
        # 使用与加密时相同的独立随机生成器
        r = random.Random(password + str(i))
        # 获取这轮的乱序索引（和加密时完全一样）
        indices = list(range(len(data)))
        r.shuffle(indices)
        # 恢复原始顺序
        chars = [None] * len(data)
        for new_pos, old_pos in enumerate(indices):
            chars[old_pos] = data[new_pos]
        data = bytes(chars)
        # base64解码
        data = base64.b64decode(data)
    return data.decode('utf-8')
