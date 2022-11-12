# Foodgram, «Продуктовый помощник». Дипломный проект.
## Свой Чек-лист для проверки (по redoc):
### Пользователи:
:heavy_check_mark: /api/users/  
:heavy_check_mark: /api/users/{id}/  
:heavy_check_mark: /api/users/me/  
:heavy_check_mark: /api/users/set_password/  
:heavy_check_mark: /api/auth/token/login/  
:heavy_check_mark: /api/auth/token/logout/  
:o: Список пользователей :warning: *не добавлено поле is_subscribed* :warning:  
:heavy_check_mark:  Регистрация пользователя  
:o: Профиль пользователя :warning: *не добавлено поле is_subscribed* :warning:  
:o: Текущий пользователь :warning: *не добавлено поле is_subscribed* :warning:  
:o: Изменение пароля :interrobang: *код 401 - другое описание* :interrobang:  
:heavy_check_mark: Получить токен авторизации  
:o: Удаление токена авторизации :interrobang: *код 401 - другое описание* :interrobang:  

### Теги
:heavy_check_mark: /api/tags/  
:o: Список тегов - *добавить валидатор на hex код (регулярное выражение)*  
:o: Получение тега - *добавить валидатор на hex код (регулярное выражение)*  

### Рецепты
:x: Список рецептов:  
    :heavy_check_mark: api/recipes/  
    :x: список избранного  
    :x: список покупок  
    :x: автор  
    :heavy_check_mark: теги  
    :heavy_check_mark: игредниеты  
    :x: фото  
### Список покупок
:x:
### Избранное
:x:
### Подписки
:heavy_check_mark: api/users/subscriptions/  
:heavy_check_mark: api/users/{id}/subscribe/  
:o: Мои подписки :warning: *не добавлены поля recipes и recipes_count* :warning:  
:o: Подписаться на пользователя :warning: *не добавлены поля recipes и recipes_count* :warning:  
:heavy_check_mark: Отписаться от пользователя  
### Ингридиенты
:heavy_check_mark: /api/ingredients/  
:heavy_check_mark: Список ингридиентов  
:heavy_check_mark: Получение ингридиентов  


:x: паджинация  
:x: фильтрация  
:x: лимиты  
:x: пермишны

## Чек-лист для проверки с Яндекса:
### Функциональность проекта
- [ ] Проект доступен по IP или доменному имени.
- [ ] Все сервисы и страницы доступны для пользователей в соответствии с их правами.
- [ ] Рецепты на всех страницах сортируются по дате публикации (новые — выше).
- [ ] Работает фильтрация по тегам, в том числе на странице избранного и на странице рецептов одного автора).
- [ ] Работает пагинатор (в том числе при фильтрации по тегам).
- [ ] Исходные данные предзагружены; добавлены тестовые пользователи и рецепты.
### Для авторизованных пользователей:
- [ ] Доступна главная страница.
- [ ] Доступна страница другого пользователя.
- [ ] Доступна страница отдельного рецепта.
- [ ] Доступна страница «Мои подписки».
    - [ ] Можно подписаться и отписаться на странице рецепта.
    - [ ] Можно подписаться и отписаться на странице автора.
    - [ ] При подписке рецепты автора добавляются на страницу «Мои подписки» и удаляются оттуда при отказе от подписки.
- [ ] Доступна страница «Избранное».
    - [ ] На странице рецепта есть возможность добавить рецепт в список избранного и удалить его оттуда.
    - [ ] На любой странице со списком рецептов есть возможность добавить рецепт в список избранного и удалить его оттуда.
- [ ] Доступна страница «Список покупок».
    - [ ] На странице рецепта есть возможность добавить рецепт в список покупок и удалить его оттуда.
    - [ ] На любой странице со списком рецептов есть возможность добавить рецепт в список покупок и удалить его оттуда.
    - [ ] Есть возможность выгрузить файл (.txt или .pdf) с перечнем и количеством необходимых ингредиентов для рецептов из «Списка покупок».
    - [ ] Ингредиенты в выгружаемом списке не повторяются, корректно подсчитывается общее количество для каждого ингредиента.
- [ ] Доступна страница «Создать рецепт».
    - [ ] Есть возможность опубликовать свой рецепт.
    - [ ] Есть возможность отредактировать и сохранить изменения в своём рецепте.
    - [ ] Есть возможность удалить свой рецепт.
- [ ] Доступна и работает форма изменения пароля.
- [ ] Доступна возможность выйти из системы (разлогиниться).
### Для неавторизованных пользователей:
- [ ] Доступна главная страница.
- [ ] Доступна страница отдельного рецепта.
- [ ] Доступна и работает форма авторизации.
- [ ] Доступна и работает система восстановления пароля.
- [ ] Доступна и работает форма регистрации.
### Администратор и админ-зона
- [ ] Все модели выведены в админ-зону.
- [ ] Для модели пользователей включена фильтрация по имени и email.
- [ ] Для модели рецептов включена фильтрация по названию, автору и тегам.
- [ ] На админ-странице рецепта отображается общее число добавлений этого рецепта в избранное.
- [ ] Для модели ингредиентов включена фильтрация по названию.
### Инфраструктура
- [ ] Проект работает с СУБД PostgreSQL.
- [ ] Проект запущен на сервере в Яндекс.Облаке в трёх контейнерах: nginx, PostgreSQL и Django+Gunicorn. Заготовленный контейнер с фронтендом используется для сборки файлов.
- [ ] Контейнер с проектом обновляется на Docker Hub.
- [ ] В nginx настроена раздача статики, запросы с фронтенда переадресуются в контейнер с Gunicorn. Джанго-админка работает напрямую через Gunicorn.
- [ ] Данные сохраняются в volumes.
### Оформление кода
- [ ] Код соответствует PEP8.