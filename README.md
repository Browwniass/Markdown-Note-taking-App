# Markdown-Note-taking-API
API для приложения составления заметок
## Основной функционал
### Пользователи
**Возможности:**
1. Идентификация и аутентификация по JWT-токену (вход по никнейму или почте)
2. Подтверждение по email

### Заметки
Заметки (или Notes) может создавать любой зарегистрированный пользователь.

**Особенности:**

Пользователь видит и взаимодействует только со своими заметками

**Возможности:**
1. Просмотр пользователем всех своих Заметок
2. Фильтрация заметок по времени создания и изменения
3. Поиск заметок по названию
4. Упорядочивание по названию, времени создания и изменения
5. Создание новой заметки
6. Изменение (описания, названия), Просмотр и Удаление отдельной заметки
7. Проверка грамотности написанного текста с использованием внешней API 
8. Загрузка в бд текста в виде .md файла и его выгрузка
