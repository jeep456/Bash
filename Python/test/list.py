list = [
    'обман',
    'Shaman',
    'газ',
    'пол',
    'выход',
    'соло',
    'снег',
    'град',
    'вьюга',
    'спасибо',
    'термос',
    'только',
    'для меня',
    'плохая',
    'как',
    'только',
    'ошибка',
    'любовь',
    'жду',
    'базиль'
]

list2 = [
    'Вестерн',
    'Комедия',
    'Драма',
    'Боевик',
    'Мультфильм',
    'Военный',
    'Исторический',
    'Документальный',
    'Детектив',
    'Политика',
    'Мелодрама',
    'Приключения',
    'Трагедия',
    'Трагикомедия',
    'Триллер',
    'Фантастика',
    'Ужасы',
    'Катастрофа',
    'Биография',
    'Сказка',
    'Фэнтези',
    'Концерт',
    'Научный',
    'Мистика'
]

list2 = sorted(list2)

for i in list2:
    print('<option value="' + i + '">' + i + '</option>')
