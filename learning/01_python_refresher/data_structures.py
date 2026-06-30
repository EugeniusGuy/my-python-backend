# """
# Learning Python Data Structures: List, Dict, Set, Tuple.

# This module demonstrates understanding of when and how to use
# each data structure in real-world scenarios.
# """

from typing import List

# # ============================================================================
# # ПРИМЕР 1: Список (List) — когда нужен порядок и изменяемость
# # ============================================================================


# def demonstrate_lists() -> None:
#     """Show common list operations and their time complexities."""

#     print("=" * 60)
#     print("LISTS")
#     print("=" * 60)

#     # Создание
#     numbers: List[int] = [1, 2, 3, 4, 5]

#     # Доступ по индексу: O(1)
#     first = numbers[0]  # быстро
#     print(f"First element: {first}")

#     # Добавление в конец: O(1)
#     numbers.append(6)
#     print(f"After append: {numbers}")

#     # Удаление по индексу: O(n) если в начале, O(1) если в конце
#     numbers.pop()  # удалить последний — быстро
#     print(f"After pop: {numbers}")

#     # Поиск: O(n) — медленно для больших списков!
#     if 3 in numbers:  # проходит по всем элементам в худшем случае
#         print("3 found in list")

#     # Срезы (slicing): O(k) где k — размер среза
#     subset = numbers[1:3]  # элементы с индекса 1 до 3 (не включая 3)
#     print(f"Slice [1:3]: {subset}")

#     # Итерация: O(n)
#     print("Iteration:")
#     for i, num in enumerate(numbers):
#         print(f"  Index {i}: {num}")


# # ============================================================================
# # ПРИМЕР 2: Словарь (Dict) — когда нужен быстрый поиск по ключу
# # ============================================================================


# def demonstrate_dicts() -> None:
#     """Show common dict operations and their use cases."""

#     print("\n" + "=" * 60)
#     print("DICTIONARIES")
#     print("=" * 60)

#     # Создание
#     user: Dict[str, str | int] = {
#         "name": "Alice",
#         "email": "alice@example.com",
#         "age": 30,
#     }

#     # Доступ: O(1)
#     name = user["name"]
#     print(f"Name: {name}")

#     # Безопасный доступ с дефолтом: O(1)
#     phone = user.get("phone", "not provided")
#     print(f"Phone: {phone}")

#     # Проверка наличия ключа: O(1)
#     if "email" in user:
#         print("Email exists in user dict")

#     # Изменение: O(1)
#     user["age"] = 31

#     # Добавление нового ключа: O(1)
#     user["phone"] = "123-456-7890"

#     # Итерация по ключам: O(n)
#     print("All keys:")
#     for key in user.keys():
#         print(f"  {key}: {user[key]}")

#     # Итерация по парам (key, value): O(n)
#     print("Items:")
#     for key, value in user.items():
#         print(f"  {key} -> {value}")


# # ============================================================================
# # ПРИМЕР 3: Сет (Set) — когда нужна уникальность и быстрая проверка
# # ============================================================================


# def demonstrate_sets() -> None:
#     """Show set operations and their use cases."""

#     print("\n" + "=" * 60)
#     print("SETS")
#     print("=" * 60)

#     # Создание (автоматически удаляет дубликаты)
#     tags: Set[str] = {"python", "backend", "fastapi", "python"}
#     print(f"Tags (duplicates removed): {tags}")

#     # Проверка наличия: O(1) — очень быстро!
#     if "python" in tags:
#         print("'python' is in tags")

#     # Добавление: O(1)
#     tags.add("docker")
#     print(f"After adding 'docker': {tags}")

#     # Удаление: O(1)
#     tags.remove("backend")
#     print(f"After removing 'backend': {tags}")

#     # Операции над сетами
#     skills_1: Set[str] = {"python", "javascript", "go"}
#     skills_2: Set[str] = {"python", "rust", "c++"}

#     # Пересечение (общие элементы): O(min(len(a), len(b)))
#     common = skills_1 & skills_2
#     print(f"Common skills: {common}")

#     # Объединение: O(len(a) + len(b))
#     all_skills = skills_1 | skills_2
#     print(f"All skills: {all_skills}")

#     # Разность: O(len(a))
#     unique_to_1 = skills_1 - skills_2
#     print(f"Unique to first: {unique_to_1}")


# # ============================================================================
# # ПРИМЕР 4: Кортеж (Tuple) — когда данные не должны меняться
# # ============================================================================


# def demonstrate_tuples() -> None:
#     """Show tuple operations and their use cases."""

#     print("\n" + "=" * 60)
#     print("TUPLES")
#     print("=" * 60)

#     # Создание
#     point: Tuple[int, int] = (10, 20)
#     print(f"Point: {point}")

#     # Доступ: O(1)
#     x, y = point  # распаковка
#     print(f"x={x}, y={y}")

#     # Кортежи неизменяемы — это защита от случайных изменений
#     # point[0] = 30  # ❌ TypeError

#     # Кортежи можно использовать как ключи словаря (списки нельзя!)
#     locations: Dict[Tuple[int, int], str] = {
#         (10, 20): "Office",
#         (5, 5): "Home",
#         (15, 15): "Cafe",
#     }
#     print(f"Locations: {locations}")

#     # Кортежи в возвращаемых значениях функций
#     result: Tuple[bool, str] = (True, "Success")
#     success, message = result
#     print(f"Success: {success}, Message: {message}")


# # ============================================================================
# # ПРИМЕР 5: Практический сценарий — управление пользователями в API
# # ============================================================================


# def manage_users_example() -> None:
#     """Real-world example: managing users with different data structures."""

#     print("\n" + "=" * 60)
#     print("REAL-WORLD EXAMPLE: User Management")
#     print("=" * 60)

#     # Словарь для быстрого поиска пользователя по ID
#     users_by_id: Dict[int, Dict[str, str | int]] = {
#         1: {"name": "Alice", "email": "alice@example.com", "role": "admin"},
#         2: {"name": "Bob", "email": "bob@example.com", "role": "user"},
#         3: {"name": "Charlie", "email": "charlie@example.com", "role": "user"},
#     }

#     # Сет для быстрой проверки уникальности email
#     used_emails: Set[str] = {
#         "alice@example.com",
#         "bob@example.com",
#         "charlie@example.com",
#     }

#     # Список для сохранения порядка действий (логирование)
#     actions: List[Tuple[int, str, str]] = [
#         (1, "login", "2026-06-26 10:00:00"),
#         (2, "create_post", "2026-06-26 10:05:00"),
#         (1, "logout", "2026-06-26 10:30:00"),
#     ]

#     # Поиск пользователя: O(1)
#     user_id = 1
#     user = users_by_id.get(user_id)
#     if user:
#         print(f"Found user: {user['name']}")

#     # Проверка email: O(1)
#     new_email = "david@example.com"
#     if new_email not in used_emails:
#         print(f"Email '{new_email}' is available")

#     # История действий
#     print("User actions:")
#     for user_id, action, timestamp in actions:
#         print(f"  User {user_id}: {action} at {timestamp}")


# ============================================================================
# ЗАПУСК ПРИМЕРОВ
# ============================================================================

# ============================================================================
# ТВОИ УПРАЖНЕНИЯ (заполни эти функции)
# ============================================================================


def exercise_1_find_unique_elements(items: List[int]) -> List[int]:
    """
    Задача 1: Удалить дубликаты из списка и вернуть в исходном порядке.

    Примеры:
        find_unique_elements([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
        find_unique_elements([5, 5, 5]) -> [5]
        find_unique_elements([]) -> []

    Подсказка: используй dict.fromkeys() или другой способ сохранить порядок.
    """
    # Создадим список, заранее преобразованный в set данных значений

    return list(dict.fromkeys(items))


def exercise_2_count_word_frequency(words: List[str]) -> dict[str, int]:
    """
    Задача 2: Подсчитать, сколько раз каждое слово встречается.

    Примеры:
        count_word_frequency(["hello", "world", "hello"]) -> {"hello": 2, "world": 1}
        count_word_frequency([]) -> {}

    Подсказка: используй dict.get() или setdefault().
    """
    # создаём словарь для подсчёта слов
    count_word_dict: dict[str, int] = {}

    # запускаем цикл по списку
    for i in words:
        # если слова есть в словаре, то счётчик увеличивается - иначе становится равным единице
        if i in count_word_dict:
            count_word_dict[i] += 1
        else:
            count_word_dict[i] = 1

    return count_word_dict


def exercise_3_find_common_tags(tags_1: set[str], tags_2: set[str]) -> set[str]:
    """
    Задача 3: Найти общие теги между двумя наборами.

    Примеры:
        find_common_tags({"python", "backend"}, {"python", "api"}) -> {"python"}
        find_common_tags({"a"}, {"b"}) -> set()

    Подсказка: операция пересечения сетов.
    """
    # объединяем множества
    tags_3 = tags_1 & tags_2

    return tags_3


def exercise_4_parse_user_data(
    raw_data: List[tuple[str, str, int]],
) -> dict[str, dict[str, str | int]]:
    """
    Задача 4: Преобразовать список кортежей в словарь пользователей.

    Входные данные: [("alice", "alice@example.com", 30), ("bob", "bob@example.com", 25)]

    Выходные данные: {
        "alice": {"email": "alice@example.com", "age": 30},
        "bob": {"email": "bob@example.com", "age": 25},
    }

    Подсказка: распаковка кортежей в цикле.
    """
    # создаём словарь для конвертации
    return {name: {"email": email, "age": age} for name, email, age in raw_data}


def exercise_5_filter_expensive_items(
    items: dict[str, int], max_price: int
) -> dict[str, int]:
    """
    Задача 5: Отфильтровать товары по цене.

    Примеры:
        filter_expensive_items({"apple": 10, "banana": 20, "cherry": 15}, 15)
        -> {"apple": 10, "cherry": 15}

    Подсказка: dict comprehension (словарное выражение).
    """

    return {key: value for key, value in items.items() if value <= max_price}


def exercise_6_merge_user_preferences(
    primary: dict[str, str], secondary: dict[str, str]
) -> dict[str, str]:
    """
    Задача 6: Объединить два словаря с приоритетом первого.

    Примеры:
        merge_user_preferences(
            {"theme": "dark", "language": "en"},
            {"theme": "light", "font_size": "large"}
        )
        -> {"theme": "dark", "language": "en", "font_size": "large"}

    Подсказка: используй .update() или |  (Python 3.9+).
    """
    # Объединяем два словаря
    return secondary | primary


def exercise_7_check_valid_credentials(
    username: str, password: str, valid_users: dict[str, str]
) -> tuple[bool, str]:
    """
    Задача 7: Проверить учётные данные. Вернуть кортеж (успех, сообщение).

    Примеры:
        check_valid_credentials("alice", "pass123", {"alice": "pass123"})
        -> (True, "Login successful")

        check_valid_credentials("alice", "wrong", {"alice": "pass123"})
        -> (False, "Invalid password")

        check_valid_credentials("bob", "pass", {"alice": "pass123"})
        -> (False, "User not found")

    Подсказка: используй .get() для безопасного доступа.
    """
    # создаём кортеж
    stored_password = valid_users.get(username)

    # проверка на совпадение пароля и логина
    if stored_password is None:
        return (False, "User not found")
    elif stored_password == password:
        return (True, "Login successful")
    else:
        return (False, "Invalid password")


if __name__ == "__main__":
    print(
        "Вывод уникальных значений словаря: ",
        exercise_1_find_unique_elements([1, 2, 2, 3]),
    )
    print(
        "Подсчёт слов: ", exercise_2_count_word_frequency(["hello", "world", "hello"])
    )
    print(
        "Поиск общих слов: ",
        exercise_3_find_common_tags({"python", "backend"}, {"python", "api"}),
    )
    print(
        "Конвертация кортежа: ",
        exercise_4_parse_user_data(
            [("alice", "alice@example.com", 30), ("bob", "bob@example.com", 25)]
        ),
    )
    print(
        "Фильтр цены: ",
        exercise_5_filter_expensive_items(
            {"apple": 10, "banana": 20, "cherry": 15}, 15
        ),
    )
    print(
        "Объединение словарей: ",
        exercise_6_merge_user_preferences(
            {"theme": "dark", "language": "en"},
            {"theme": "light", "font_size": "large"},
        ),
    )
    print(
        "Проверка пароля и логина: ",
        exercise_7_check_valid_credentials("alice", "pass123", {"alice": "pass123"}),
    )
