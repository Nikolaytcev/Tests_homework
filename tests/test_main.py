import unittest

import pytest

from main import geo_logs, get_russian_city, ids, get_unique_ids, stats, get_max_value, YaDirectories


class TestHomework:

    @pytest.mark.parametrize("visits, expected", [(
            geo_logs,
            [
                {'visit1': ['Москва', 'Россия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}
            ]), (geo_logs, {'visit6': ['Лиссабон', 'Португалия']})])
    def test_get_max_values(self, visits, expected):
        result = get_russian_city(visits)
        assert result == expected

    @pytest.mark.parametrize("dict_users, expected", [(ids, [213, 15, 54, 119, 98, 35]),
                                                      (ids, [213, 15, 54, 119, 101, 35]),
                                                      (ids, [15, 54, 213, 119, 98, 35])], )
    def test_get_unique_ids(self, dict_users, expected):
        result = get_unique_ids(dict_users)
        assert sorted(result) == sorted(expected)

    @pytest.mark.parametrize("dict_stats, expected", [(stats, 120), (stats, 98)])
    def test_get_max_value(self, dict_stats, expected):
        result = get_max_value(stats)
        assert result == expected

    @pytest.mark.parametrize("directory_name, expected_status_code", [('My_directory', 200),
                                                                      ('New_directory', 200),
                                                                      ('Other_dir', 200)])
    def test_get_status_code(self, directory_name, expected_status_code):
        token = 'y0_AgAAAABm8ntQAADLWwAAAADWc2-D5PtMNsrYQrK0o3apSaifEmL54gw'
        result = YaDirectories(token).get_status_code(directory_name)
        assert result == expected_status_code
