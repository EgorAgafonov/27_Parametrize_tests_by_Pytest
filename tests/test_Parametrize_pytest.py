import pytest
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password


# 1 Параметризация с помощью фикстуры.

# Параметризация тестов с помощью фикстуры с  параметрами params=(количество объектов (тестов) тестирования) и
# ids=(название тестов для удобства, которое должно быть равно количеству объектов (тестов) тестирования,
# переданных в params=):
# def python_string_slicer(str):
#     if len(str) < 50 or "python" in str:
#         return str
#     else:
#         return str[0:50]
# #
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
# ], ids=["len < 50", "len > 50", "len < 50 contains python", "len > 50 contains python"])
# def param_fun(request):
#     return request.param
#
#
# def test_python_string_slicer(param_fun):
#     (input, expected_output) = param_fun
#     result = python_string_slicer(input)
#     print("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
#     assert result == expected_output

# 1.2
# Вынесем генерацию названий в отдельную функцию:

# def generate_id(val):
#    return "params: {0}".format(str(val))
#
#
# def python_string_slicer(str):
#     if len(str) < 50 or "python" in str:
#         return str
#     else:
#         return str[0:50]
#
#
# @pytest.fixture(scope="function", params=[
#    ("Короткая строка", "Короткая строка"),
#    ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#     , "Длинная строка, не то чтобы прям очень длинная, но"),
#    ("Короткая строка со словом python", "Короткая строка со словом python"),
#    ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#     , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
# ], ids=generate_id)
# def param_fun_generated(request):
#    return request.param
#
#
# def test_python_string_slicer_generated(param_fun_generated):
#    (input, expected_output) = param_fun_generated
#    result = python_string_slicer(input)
#    print("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
#    assert result == expected_output

# 2 Параметризация с помощью pytest.mark.parametrize.

# 2.1
# Если указать несколько меток с разными параметрами, то тест будет запущен со всеми возможными наборами параметров
# (то есть мы имеем декартово произведение). Напишем простой тест, чтобы это продемонстрировать:

# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [10, 11])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True

# 2.2
# Точно так же нам доступны два варианта передачи ids в фикстуру — в виде имени функции или набора значений.
# Для начала давайте посмотрим, как передаётся набор значений:

# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True


# 2.3
# Проделаем аналогичные операции с генератором имён параметров:
# def ids_x(val):
#     return "x=({0})".format(str(val))
#
#
# def ids_y(val):
#     return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
# @pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True

# 2.4 Самостоятельный тест:

# @pytest.mark.parametrize("r", [0, 255], ids=["0_red", "255_red"])
# @pytest.mark.parametrize("g", [0, 15, 150, 255], ids=["0_green", "15_green", "150_green", "255_green"])
# @pytest.mark.parametrize("b", [0, 30, 255], ids=["0_blue", "30_blue", "255_blue"])
# def test_color_picker(r, g, b):
#     print("r: {0}, g: {1}, b: {2}".format(r, g, b))
#     assert True

                                        # 3 Параметризации для REST API тестов

# 3.1

# pf = PetFriends()
#
# def generate_string(num):
#    return "x" * num
#
#
# def russian_chars():
#    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def chinese_chars():
#    return '的一是不了人我在有他这为之大来以个中上们'
#
#
# def special_chars():
#    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
#
#
# @pytest.fixture(autouse=True)
# def get_api_key():
#    #""" Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""
#
#    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#    status, pytest.key = pf.get_api_key(valid_email, valid_password)
#
#    # Сверяем полученные данные с нашими ожиданиями
#    assert status == 200
#    assert 'key' in pytest.key
#
#    yield
#
#
# @pytest.mark.parametrize("filter",
#                         [
#                             generate_string(255)
#                             , generate_string(1001)
#                             , russian_chars()
#                             , russian_chars().upper()
#                             , chinese_chars()
#                             , special_chars()
#                             , 123
#                         ],
#                         ids =
#                         [
#                             '255 symbols'
#                             , 'more than 1000 symbols'
#                             , 'russian'
#                             , 'RUSSIAN'
#                             , 'chinese'
#                             , 'specials'
#                             , 'digit'
#                         ])
# def test_get_all_pets_with_negative_filter(filter):
#    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#    # Проверяем статус ответа
#    assert pytest.status == 400
#
#
# @pytest.mark.parametrize("filter",
#                         ['', 'my_pets'],
#                         ids=['empty string', 'only my pets'])
# def test_get_all_pets_with_valid_key(filter):
#    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#    # Проверяем статус ответа
#    assert pytest.status == 200
#    assert len(result['pets']) > 0

                                            # 3 Параметризации для REST API тестов.


pf = PetFriends()

def generate_string(num):
   return "x" * num


def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
#
#
# @pytest.fixture(autouse=True)
# def get_api_key():
#    #""" Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""
#
#    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#    status, pytest.key = pf.get_api_key(valid_email, valid_password)
#
#    # Сверяем полученные данные с нашими ожиданиями
#    assert status == 200
#    assert 'key' in pytest.key
#
#    yield
#
#
# @pytest.mark.parametrize("filter",
#                         [
#                             generate_string(255)
#                             , generate_string(1001)
#                             , russian_chars()
#                             , russian_chars().upper()
#                             , chinese_chars()
#                             , special_chars()
#                             , 123
#                         ],
#                         ids =
#                         [
#                             '255 symbols'
#                             , 'more than 1000 symbols'
#                             , 'russian'
#                             , 'RUSSIAN'
#                             , 'chinese'
#                             , 'specials'
#                             , 'digit'
#                         ])
# def test_get_all_pets_with_negative_filter(filter):
#    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#    # Проверяем статус ответа
#    assert pytest.status == 400
#
#
# @pytest.mark.parametrize("filter",
#                         ['', 'my_pets'],
#                         ids=['empty string', 'only my pets'])
# def test_get_all_pets_with_valid_key(filter):
#    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#    # Проверяем статус ответа
#    assert pytest.status == 200
#    assert len(result['pets']) > 0


                                             #  27.3. Сложная параметризация тестов

def is_age_valid(age):
   # Проверяем, что возраст - это число от 1 до 49 и целое
   return age.isdigit() \
          and 0 < int(age) < 50 \
          and float(age) == int(age)
#
#
# @pytest.mark.parametrize("name"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("animal_type"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("age"
#    , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
#    , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
# def test_add_new_pet_simple(name, animal_type, age):
#    """Проверяем, что можно добавить питомца с различными данными"""
#
#    # Добавляем питомца
#    pytest.status, result = pf.create_pet_simple(pytest.key, name, animal_type, age)
#
#    # Сверяем полученный ответ с ожидаемым результатом
#    if name == '' or animal_type == '' or is_age_valid(age):
#        assert pytest.status == 400
#    else:
#        assert pytest.status == 200
#        assert result['name'] == name
#        assert result['age'] == age
#        assert result['animal_type'] == animal_type


                            # 27.4. Автоматизация с параметризацией для негативных тестов

def is_age_valid(age):
   # Проверяем, что возраст - это число от 1 до 49 и целое
   return age.isdigit() \
          and 0 < int(age) < 50 \
          and float(age) == int(age)


# @pytest.mark.parametrize("name"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("animal_type"
#    , ['', generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(), '123']
#    , ids=['empty', '255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
# @pytest.mark.parametrize("age"
#    , ['', '-1', '0', '1', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()]
#    , ids=['empty', 'negative', 'zero', 'min', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials', 'russian', 'RUSSIAN', 'chinese'])
# def test_add_new_pet_simple(name, animal_type, age):
#    """Проверяем, что можно добавить питомца с различными данными"""

   # # Добавляем питомца
   # pytest.status, result = pf.create_pet_simple(pytest.key, name, animal_type, age)
   #
   # # Сверяем полученный ответ с ожидаемым результатом
   # if name == '' or animal_type == '' or is_age_valid(age):
   #     assert pytest.status == 400
   # else:
   #     assert pytest.status == 200
   #     assert result['name'] == name
   #     assert result['age'] == age
   #     assert result['animal_type'] == animal_type

@pytest.mark.parametrize("name", [''], ids=['empty'])
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age",
                        ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(),
                         russian_chars().upper(), chinese_chars()]
   , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials',
          'russian', 'RUSSIAN', 'chinese'])
def test_add_new_pet_simple_negative(name, animal_type, age):

   # Добавляем питомца
   pytest.status, result = pf.create_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   assert pytest.status == 400