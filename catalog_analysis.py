import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# ============================================================
# Этап 1.
# ============================================================
def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до одного знака."""
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый, самый новый, среднее),
    где возраст = current_year - year, среднее округлено вверх math.ceil."""
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Переводит минуты в формат "2ч 35м"."""
    return f"{minutes // 60}ч {minutes % 60}м"


# ============================================================
# Этап 2.
# ============================================================
def rating_tier(rating):
    """Возвращает категорию оценки:
    "шедевр" (>=9), "хорошо" (7-8.9), "средне" (5-6.9), "слабо" (<5)."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 5:
        return "хорошо" if rating >= 7 else "средне"
    else:
        return "слабо"


def decade_label(year):
    """Метка по году выпуска:
    "новые" (>2020), "недавние" (2015-2020), "старые" (<2015)."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# ============================================================
# Этап 3. Циклы
# ============================================================
def print_non_comedies(movies):
    """Печатает названия фильмов, которые НЕ относятся к жанру "comedy"."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies, threshold=9.0):
    """Находит первый по порядку фильм с рейтингом выше threshold.
    Если такого нет — печатает "Шедевров не найдено"."""
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > threshold:
            print("Первый шедевр:", movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# ============================================================
# Этап 4. Строки
# ============================================================
def normalize_title(title):
    """Приводит строку к Title Case без str.title():
    разбивает по пробелам и вручную поднимает первую букву каждого слова."""
    words = title.split()
    normalized = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized)


def make_slug(title):
    """Превращает название в слаг: "Silent Hours" -> "silent-hours"."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Собирает строку-описание фильма через f-строку."""
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — '
        f"{movie['rating']}/10, "
        f"{duration_in_hours(movie['duration_min'])}, "
        f"жанры: {genres}"
    )


# ============================================================
# Этап 5. Списки
# ============================================================
def titles_sorted_by_rating(movies):
    """Список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]


# ============================================================
# Этап 6. Словари
# ============================================================
def count_by_genre(movies):
    """Словарь {жанр: количество фильмов}, построенный вручную через dict.get()."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography


def above_average_ratings(movies):
    """Словарь {title: rating} только для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg
    }


# ============================================================
# Этап 7. Множества
# ============================================================
def all_genres(movies):
    """Множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Множество актёров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры, встречающиеся в movies_a, но не в movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)


# ============================================================
# Этап 8. Итераторы и генераторы
# ============================================================
def iter_high_rated(movies, min_rating=8.0):
    """Лениво отдаёт фильмы с рейтингом не ниже min_rating (yield)."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_minutes_above(movies, min_rating=7.0):
    """Суммарная длительность фильмов с рейтингом выше min_rating
    (генераторное выражение в sum())."""
    return sum(m["duration_min"] for m in movies if m["rating"] > min_rating)


# ============================================================
# Демонстрация этапов 3 и 8
# ============================================================
def demo(movies):
    """Демонстрирует циклы (этап 3) и генераторы (этап 8)."""
    print("=== Демонстрация функций этапов 3 и 8 ===\n")

    print("Фильмы не из жанра comedy:")
    print_non_comedies(movies)

    print("\nПоиск шедевра (рейтинг > 9.0):")
    find_first_masterpiece(movies)
    print("Поиск шедевра в каталоге без The Quiet Algorithm:")
    find_first_masterpiece(movies[:7])

    print(f"\nФильмов длиннее 120 минут: {count_long_movies(movies)}")

    print("\nФильмы с рейтингом от 8.0:")
    for movie in iter_high_rated(movies):
        print("  " + format_report_line(movie))

    print(f"\nСуммарная длительность (рейтинг > 7): {total_minutes_above(movies)} мин")


# ============================================================
# Демонстрация / Этап 9
# ============================================================
def build_report(movies):
    """Полный отчет по каталогу"""
    print("ОТЧЕТ ПО КАТАЛОГУ")

    avg_rating = average_rating(movies)
    age_stats = catalog_age_stats(movies)
    avg_age = age_stats[2]

    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    for title, rating in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print("  " + format_report_line(movie))

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(genre_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {genre} — {count}")

    genres_line = ", ".join(sorted(all_genres(movies)))
    print(f"\nВсе жанры каталога: {genres_line}")


if __name__ == "__main__":
    demo(movies)
    print()
    build_report(movies)
