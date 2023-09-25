# Gaijin Entertement Demo Project

## Запуск тестов
### Запуск тестов локально
1. Клонировать репозиторий
```
git clone git@github.com:ivkhokhlov/store_gaijin_demo.git
```
2. Перейти в папку
```
cd store_gaijin_demo
```
3. Инициализировать виртуальное окружение
```
python -m venv venv
```
4. Активировать виртуальное окружение
```
source ./venv/bin/activate
```
5. Установить зависимости
```
pip install -r requirements.txt
```
6. Положить .env файл в папку с проектом
```
GAIJIN_LOGIN = 'xokev83191@ipnuc.com'
GAIJIN_PASSWORD = 123456
SELENE_LOGIN = 'user1'
SELENE_PASSWORD = 1234
```
7. Запустить тесты
```
python -m pytest
```
## Удаленный запуск проекта в Jenkins
1. Открыть проект в Jenkins
2. Нажать "Собрать с параметрами"
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/856de153-56cf-4511-975e-473a0479eede)
3. Заполнить параметры, нажать "Собрать"
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/8f318a87-a210-4293-af4c-f0b92d9e086d)
4. После успешной сборки, Allure-отчет с результатами будет доступен в истории сборок
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/8a3e48cf-a4fd-4a82-bc6c-c41b0213d6e3)
### Пример оповещений в Telegram
![image](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/167cd8d9-a7c0-45ef-9118-abe0579dc69e)
### Видео запуска теста
Браузеры запускаются удаленно на Selenide
![selene](https://github.com/ivkhokhlov/store_gaijin_demo/assets/58159018/cac8b732-daf2-44d6-b572-41cbd0edef7e)
