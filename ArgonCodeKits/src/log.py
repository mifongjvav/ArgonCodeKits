import logging
import coloredlogs
import sys
from pathlib import Path

def init_log_file(lower_level: str = "INFO") -> None:
    """初始化日志系统

    Args:
        lower_level (str, optional): 最低日志级别. Defaults to "INFO".
    """

    log_path = Path.cwd() / "latest.log"
    
    # 清理现有的日志处理器
    for handler in logging.root.handlers[:]:
        handler.close()
        logging.root.removeHandler(handler)
    
    # 删除旧的日志文件（如果存在）
    try:
        log_path.unlink(missing_ok=True)
    except PermissionError:
        # 记录警告但继续执行
        print(f"警告：无法删除旧的日志文件 {log_path}，权限不足", file=sys.stderr)
    
    # 配置文件日志和控制台日志
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    
    # 安装彩色日志（仅对INFO及以上级别生效）
    coloredlogs.install(
        level=lower_level.upper(), 
        fmt="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
    )