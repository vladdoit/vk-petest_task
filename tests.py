import pytest


# Класс тестов для Float
class TestFloat:
    # Негативный тест преобразования значения переменной в тип float
    def test_get_value_error_exception(self):
        value = "String"
        try:
            assert float(value)
        except ValueError:
            pass

    # Позитивный тест нахожения произведения двух float значений
    @pytest.mark.parametrize("a, b, expected", [(2.1, 3.2, 6.720000000000001), (6.1, 0.0, 0.0), (5.1, -4.2, -21.419999999999998), (0.0, 0.0, 0.0), (-4.2, 2.5, -10.5), (-6.5, -4.5, 29.25)])
    def test_get_sum_of_two_values(self, a, b, expected):
        assert a * b == expected


# Класс тестов для List
class TestList:

    # Позитивный тест проверки сортировки списка
    def test_get_list_length(self):
        list = [4, 2, 1, 5, 3]
        assert sorted(list) == [1, 2, 3, 4, 5]

    # Позитивный тест объединения элементов двух списков
    @pytest.mark.parametrize("list1, list2, expected", [([1, 2], [3], [1, 2, 3]), ([1, 2], [], [1, 2]), ([], [], []), ([], [1, 2], [1, 2]), ([3], [1, 2], [3, 1, 2]), ([], [1], [1]), ([1], [], [1])])
    def test_get_union_of_two_list(self, list1, list2, expected):
        assert list1 + list2 == expected

    # Негативный тест выхода за границы списка
    def test_get_index_error_exception(self):
        list = [1, 2, 3]
        try:
            assert list[4]
        except IndexError:
            pass


# Класс тестов для Tuple
class TestTuple:

    # Позитивный тест проверки длины кортежа
    def test_get_tuple_length(self):
        my_tuple = (1, 2, 3, 4, 5, 6)
        assert len(my_tuple) == 6

    # Позитивный тест получения среза из кортежа
    @pytest.mark.parametrize("my_tuple, i, j, expected", [(("a", "b", "c"), 0, 2, ("a", "b")), (("a", "b", "c"), 0, 3, ("a", "b", "c")), (("a", "b", "c"), -1, 3, ("c",)), (("a", "b", "c"), 1, -1, ("b",)), (("a", "b", "c"), -1, -1, ())])
    def test_get_cut_of_tuple(self, my_tuple, i, j, expected):
        assert my_tuple[i:j] == expected

    # Негативный тест на объединение элементов кортежа со строкой
    def test_get_value_error_exception(self):
        my_tuple = (4, 5, 6)
        string_value = "String"
        try:
            assert my_tuple + string_value
        except TypeError:
            pass
