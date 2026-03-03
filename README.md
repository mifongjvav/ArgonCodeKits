# Argon Code Kits

Argon的代码库，包含一些实用的工具函数，旨在提高开发效率和代码精简度。

## 功能模块

### hash - 哈希计算

- `md5(s)` - 计算字符串的 MD5 哈希值
- `sha1(s)` - 计算字符串的 SHA-1 哈希值
- `sha256(s)` - 计算字符串的 SHA-256 哈希值
- `sha512(s)` - 计算字符串的 SHA-512 哈希值

### os - 操作系统工具

- `get_folder_size(folder)` - 获取文件夹大小
- `filter_windows_invalid_chars(s, o="[x]")` - 过滤 Windows 文件名非法字符
- `check_working_directory()` - 切换目录到脚本位置

### pyplus - Python 增强功能

- `input(prompt, level="info")` - 带日志记录的输入函数
- `encrypt(text, password, rounds=10)` - 文本加密（基于 base64 和混淆）
- `decrypt(ciphertext, password, rounds=10)` - 解密

## 安装

```bash
pip install ArgonCodeKits
