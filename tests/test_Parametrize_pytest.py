import pytest


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

# 2.4 Самостоятельныйтест:

@pytest.mark.parametrize("r", [0, 255], ids=["0_red", "255_red"])
@pytest.mark.parametrize("g", [0, 15, 150, 255], ids=["0_green", "15_green", "150_green", "255_green"])
@pytest.mark.parametrize("b", [0, 30, 255], ids=["0_blue", "30_blue", "255_blue"])
def test_color_picker(r, g, b):
    print("r: {0}, g: {1}, b: {2}".format(r, g, b))
    assert True
