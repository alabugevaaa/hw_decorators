import hashlib
from datetime import datetime


def logging(path):
    def decor(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            str = f'{datetime.now()} - {function.__name__}; {args} {kwargs}; {result}\n'
            with open(path, 'a', encoding='utf-8') as f:
                f.write(str)
            return result
        return wrapper
    return decor


@logging('logs/log.txt')
def hash_line(path):
    with open(path, encoding='utf8') as hosts_file:
        for line in hosts_file:
            line = line.strip().encode('utf-8')
            hash = hashlib.md5(line).hexdigest()
            yield hash


if __name__ == '__main__':

    for hash_password in hash_line('passwords.list'):
        print(hash_password)

