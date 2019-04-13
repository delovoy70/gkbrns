import subprocess
import platform
import chardet


str_lst = {'разработка', 'сокет', 'декоратор'}

for _ in str_lst:
    b_str = _.encode()
    print(type(b_str), b_str)

str_lst = {b'class', b'function', b'method'}

for _ in str_lst:
    print(type(_), _, len(_))


str_lst = {'attribute', 'класс', 'функция', 'type'}
for _ in str_lst:
    try:
        print(_.encode())
    except:
        pass


hostnames = {"yandex.ru", "youtube.com"}
for _ in hostnames:
    cmd = "ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', _)
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode('cp866'))


tmp_file = 'test_file.txt'
with open(tmp_file, 'w+') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')
with open(tmp_file, 'rb') as f:
    print(chardet.detect(f.read()))
with open(tmp_file, 'r', encoding='utf-8') as f:
    print(f.read())
