import subprocess, platform


str_lst = ['разработка', 'сокет', 'декоратор']

for _ in str_lst:
    b_str = _.encode()
    print(type(b_str), b_str)

str_lst = [b'class', b'function', b'method']

for _ in str_lst:
    print(type(_), _, len(_))


str_lst = ['attribute', 'класс', 'функция', 'type']
for _ in str_lst:
    try:
        print(_.encode())
    except:
        pass


hostnames = {"yandex.ru", "youtube.com"}
for _ in hostnames:
    cmd = "ping -{} 4 {}".format('n' if platform.system().lower()=="windows" else 'c', _)
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode('cp866'))
