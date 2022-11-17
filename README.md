# Foodgram, «Продуктовый помощник». Дипломный проект.
## Свой Чек-лист для проверки (по redoc):

### Пользователи:
:heavy_check_mark: /api/users/  
:heavy_check_mark: /api/users/{id}/  
:heavy_check_mark: /api/users/me/  
:heavy_check_mark: /api/users/set_password/  
:heavy_check_mark: /api/auth/token/login/  
:heavy_check_mark: /api/auth/token/logout/  
:heavy_check_mark: Список пользователей  
:heavy_check_mark: Регистрация пользователя  
:heavy_check_mark: Профиль пользователя  
:heavy_check_mark: Текущий пользователь  
:heavy_check_mark: Изменение пароля  
:heavy_check_mark: Получить токен авторизации  
:heavy_check_mark: Удаление токена авторизации
 
### Теги:
:heavy_check_mark: /api/tags/  
:heavy_check_mark: Список тегов  
:heavy_check_mark: Получение тега

### Рецепты:
:heavy_check_mark: GET api/recipes/  
:heavy_check_mark: POST api/recipes/   
:heavy_check_mark: GET api/recipes/{id}  
:heavy_check_mark: PATCH api/recipes/{id}  
:heavy_check_mark: DEL api/recipes/{id}  
:heavy_check_mark: теги  
:heavy_check_mark: автор  
:heavy_check_mark: игредниеты  
:heavy_check_mark: список избранного  
:heavy_check_mark: список покупок  
:heavy_check_mark: название  
:heavy_check_mark: фото, **закодированное в Base64**  
:heavy_check_mark: описание  
:heavy_check_mark: время приготовления

### Список покупок:
:heavy_check_mark: api/recipes/download_shopping_cart/  
:heavy_check_mark: POST api/users/{id}/favorite/  
:heavy_check_mark: DEL api/users/{id}/favorite/  
:heavy_check_mark: Скачать список покупок  
:heavy_check_mark: Добавить рецепт в список покупок  
:heavy_check_mark: Удалить рецепт из списка покупок

### Избранное:
:heavy_check_mark: POST api/users/{id}/favorite/  
:heavy_check_mark: DEL api/users/{id}/favorite/  
:heavy_check_mark: Добавить рецепт в избранное    
:heavy_check_mark: Удалить рецепт из избранного

### Подписки:
:heavy_check_mark: api/users/subscriptions/  
:heavy_check_mark: api/users/{id}/subscribe/  
:heavy_check_mark: Мои подписки  
:heavy_check_mark: Подписаться на пользователя   
:heavy_check_mark: Отписаться от пользователя

### Ингридиенты:
:heavy_check_mark: /api/ingredients/  
:heavy_check_mark: Список ингридиентов  
:heavy_check_mark: Получение ингридиентов

###  Пермишны:  
#### Админ может: 
:heavy_check_mark: изменять пароль любого пользователя  
:heavy_check_mark: создавать/блокировать/удалять аккаунты пользователей  
:heavy_check_mark: редактировать/удалять любые рецепты  
:heavy_check_mark: добавлять/удалять/редактировать ингредиенты  
:heavy_check_mark: добавлять/удалять/редактировать теги

#### Авторизованный пользователь может:
:heavy_check_mark: Входить в систему под своим логином и паролем  
:heavy_check_mark: Выходить из системы (разлогиниваться)  
:heavy_check_mark: Менять свой пароль  
:heavy_check_mark: Создавать/редактировать/удалять собственные рецепты  
:heavy_check_mark: Просматривать рецепты на главной  
:heavy_check_mark: Просматривать страницы пользователей  
:heavy_check_mark: Просматривать отдельные страницы рецептов  
:heavy_check_mark: Фильтровать рецепты по тегам  
:heavy_check_mark: Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов  
:heavy_check_mark: Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок  
:heavy_check_mark: Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок

#### Гость может: 
:heavy_check_mark: Создать аккаунт  
:heavy_check_mark: Просматривать рецепты на главной  
:heavy_check_mark: Просматривать отдельные страницы рецептов  
:heavy_check_mark: Просматривать страницы пользователей  
:heavy_check_mark: Фильтровать рецепты по тегам

### Фильтрация и поиск
:heavy_check_mark: На странице списка рецептов доступна фильтрация по избранному, автору, списку покупок и тегам  
:heavy_check_mark: На странице ингредиентов доступен поиск по имени ингридиента  

### Паджинация и лимиты
:heavy_check_mark: Список пользователей (по 6 на странице)  
:heavy_check_mark: Список рецептов (по 6 на странице)  
:heavy_check_mark: Мои подписки (по 6 на странице, с 3 рецептами у каждого автора)  

### Валидация  
:heavy_check_mark: Валидация тегов (отсутствие в базе, повтор, пустой список в рецепте)  
:heavy_check_mark: Валидация ингредиентов (отсутствие в базе, повтор, пустой список в рецепте)  
:heavy_check_mark: Валидация самоподписки  

### Админ-панель:
:heavy_check_mark: Пользователь  
:heavy_check_mark: Рецепты  
:heavy_check_mark: Теги  
:heavy_check_mark: Ингридиенты  

## При подключении фронтенда (локально через docker) выявлено и устранено:
:heavy_check_mark: Отображение рецептов на главной странице и странице избранного *(ничего не отображалось из-за фильтрации по тегам)*  
:heavy_check_mark: Поиск по имени ингридиента *(при вводе имени вылезал весь список)*  
:heavy_check_mark: Фильтрация по тегам *(не работала)*  
:heavy_check_mark: Отображение рецептов в избранном и списке покупок **(в избранном отображались все существующие рецепты а счетчик у списка покупок соответствовал колличеству всех существующих рецептов)*  
:heavy_check_mark: Отображение рецептов на странице подписок *(отображалось по 6 рецептов в соответствии с глобальной паджинацией из файла настроек)*  

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