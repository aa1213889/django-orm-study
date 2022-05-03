import hashlib


def password_encrypt(pwd):
    md5 = hashlib.md5()       # 2，实例化md5() 方法
    md5.update(pwd.encode())      # 3，对字符串的字节类型加密
    result = md5.hexdigest()        # 4，加密
    return result
