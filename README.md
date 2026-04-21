# parse_primary_json_data.py

Модуль для парсинга данных из Yandex-форм в структурированный JSON-формат.

## Назначение

Преобразует сырые данные опросов, собранных через Yandex Forms, в удобный для дальнейшего анализа и визуализации JSON-формат с группировкой ответов по категориям.

## Выходной формат

Функция `read_base_dict_from_json` возвращает JSON-объект со следующими разделами:

| Поле | Описание |
|------|----------|
| `age` | Распределение по возрастным группам |
| `place_of_residence` | Распределение по месту жительства |
| `profession` | Распределение по роду деятельности |
| `frequency_of_using_bypass` | Частота использования средств обхода блокировок |
| `blocked_services_using` | Использование заблокированных сервисов |
| `political_activity_dynamic` | Динамика изменения политических взглядов |
| `technical_skills_dynamic` | Динамика изменения технических навыков |
| `blocks_efficiency_opinion` | Мнение об эффективности блокировок |
| `publish_opinion_in_media` | Практика публикации мнения в соцсетях |

## Пример выходных данных

```json
{
    "age": {
        "less 18": 57,
        "18-25": 38,
        "26-40": 9,
        "41-60": 22,
        "60 and elder": 10
    },
    "place_of_residence": {
        "Moscow": 98,
        "Moscow area": 15,
        "Saint-Petersburg": 0,
        "another million citizens town": 1,
        "another less than million citizens town": 21,
        "settlement or village": 1
    },
    "profession": {
        "schoolboy": 55,
        "technical student": 20,
        "humanities student": 12,
        "IT-sector worker": 8,
        "not IT-sector worker": 13,
        "entrepreneur": 1,
        "budgetary sphere": 10,
        "pensioner": 8,
        "another": 9
    }
}