import yaml

def write_data_to_yaml():
    dict_for_yaml = {
        'key1': [1, 2],
        'key2': 2,
        'key3': {
            '1$': 500,
            '2$': 1000
        }
    }

    with open('data_write.yaml', 'w', encoding='utf-8') as f_n:
        yaml.dump(dict_for_yaml, f_n)

write_data_to_yaml()