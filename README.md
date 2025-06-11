# pytest_ui_api_template

## Шаблон для автоматизации тестирования на Python

### Шаги
1. Склонировать проект: `git clone https://github.com/Exesauer/pytest_ui_api_template.git`
2. Установить все зависимости: `pip install -r requirements.txt`
3. Запустить тесты: `pytest`
4. Сгенерировать отчет: `allure generate allure-results --clean -o allure-report`
5. Открыть отчет: `allure open allure-report`

### Стек:
- **pytest**: Необходим для запуска тестов.
- **selenium**: Используется для автоматизации браузера.
- **webdriver-manager**: Помогает автоматически управлять драйверами для браузеров.
- **requests**: Библиотека для HTTP-запросов, полезна для API-тестов.
- **sqlalchemy**: Используется для взаимодействия с базами данных.
- **allure**: Необходим для генерации красивых отчетов Allure на основе тестов PyTest.
- **config**: Для работы с конфигурациями.

### Структура:
- ./tests - Тесты
- ./pages - Описание страниц
- ./api - Вспомогательные модули для работы с API
- ./db - Вспомогательные модули для работы с БД

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Официальный репозиторий библиотек Python](https://pypi.org/)