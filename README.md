"# Krasnov---Lab01" 
## Инструкция по запуску
### Запуск с использованием Docker
**Пересобираете и запускаете контейнеры с помощью команды:**
```bash
docker-compose up --build
```
**После у вас появится 4 контейнера:**
* Три экземляра сервиса
* Балансировщик nginx

**Сделайте запрос через Nginx или вставьте URL-адрес страницы**
```bash
curl http://localhost/api/v1/contact/
```

### Запуск без Docker-a
**Запустите главный скрипт "main.py" и перейдите по ссылке:** `http://127.0.0.1:6080`
В открывшейся странице выберите одну из предложенный ссылок:
![image](https://github.com/user-attachments/assets/9f4659dc-9027-48c0-ad29-b83b1f243418)

**Откройте один из файлов** `requests(contacts).py` **или** `requests(groups).py`
В самом конце кода будет написано основное тело запроса. Можете убрать коментарии и наблюдать за изменениями на странице или в консоли VS Code.