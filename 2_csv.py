import csv
import re


def getdata(list_of_files):

    regex_prod = r'Изготовитель системы:' + '' '+'
    regex_name = r'Название ОС:' + '' '+'
    regex_code = r'Код продукта:' + '' '+'
    regex_type = r'Тип системы:' + '' '+'

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in list_of_files:
        with open(file) as f:
            os_prod_list = []
            os_name_list = []
            os_code_list = []
            os_type_list = []
            lines = f.read().split('\n')
            for line in lines:
                if re.match(regex_prod, line):
                    sprod = re.sub(regex_prod, '', line).strip()
                    os_prod_list.append(sprod)
                elif re.match(regex_name, line):
                    sname = re.sub(regex_name, '', line).strip()
                    os_name_list.append(sname)
                elif re.match(regex_code, line):
                    scode = re.sub(regex_code, '', line).strip()
                    os_code_list.append(scode)
                elif re.match(regex_type, line):
                    stype = re.sub(regex_type, '', line).strip()
                    os_type_list.append(stype)
                else:
                    pass
            try:
                row_data = [os_prod_list[0], os_name_list[0], os_code_list[0], os_type_list[0]]
                file_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
                file_data.append(row_data)
                main_data.append(row_data)
            except IndexError:
                pass

        with open('main_data' + file.split('.')[0] + '.csv', 'w', encoding='utf-8') as f_n:
            f_n_writer = csv.writer(f_n)
            for row in file_data:
                f_n_writer.writerow(row)

    print(main_data)
    return main_data


def write_to_csv(resultfile):
    files_to_import = ['info_1.txt']
    files_to_import.append('info_2.txt')
    files_to_import.append('info_3.txt')
    main_data = getdata(files_to_import)

    with open(resultfile, 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(main_data)


def main():

    resultfile = '123.csv'
    write_to_csv(resultfile)


main()
