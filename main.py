from upload_yandex_disk import YaUploader

# task_1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def get_russian_city(geo_logs):
    geo_logs_sort = [i for i in geo_logs if 'Россия' in list(i.values())[0]]
    return geo_logs_sort


# task_2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def get_unique_ids(ids):
    new_list_id = []
    for i in ids:
        new_list_id.extend(ids.get(i))
    return list((set(new_list_id)))


# task_3
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_max_value(dict_):
    for channel, value in stats.items():
        if value == max(stats.values()):
            return value


# task_check_status_code

class YaDirectories:

    def __init__(self, token):
        self.token = token
        self.yandex = YaUploader(self.token)

    def create_directories(self, list_dir):
        for i in list_dir:
            self.yandex.create_directory(i)

    def get_status_code(self, directory):
        return self.yandex.get_status_code(directory).status_code


def main():
    directories = ['My_directory', 'New_directory', 'Other_dir']
    token = ''

    YaDirectories(token).create_directories(directories)


if __name__ == '__main__':
    main()
