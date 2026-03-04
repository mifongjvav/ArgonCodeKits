import logging
from ArgonCodeKits import init_log_file

def test_init_log_file():
    init_log_file("INFO")
    logging.info("test log")
    assert True  # 只要不报错就算通过