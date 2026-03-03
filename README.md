🚀 Effective Mobile — DevOps Test Project

📌 Описание
Проект состоит из двух сервисов:
1️⃣ Backend — простой HTTP-сервер на Python(flask), который отвечает на путь / текстом с html:
    
    <Hello from Effective Mobile!>
Слушает порт 8080 внутри Docker-сети.

2️⃣ Nginx — reverse proxy, который принимает запросы на порт 80 и проксирует их на backend, также использует свой отдельный nginx.conf

Схема работы:
    Client → Nginx → backend

🌐 Сети
Nginx подключён к сетям:    

    - frontend
    - backend
Backend подключён только к сети:
    
    - backend
Backend не публикует порт наружу — доступ к нему возможен только через Nginx.  

📂 Структура проекта
```
│   .dockerignore
│   .env
│   .gitignore
│   docker-compose.yml
│   Effective_Mobile_ТЗ_DevOps_github.pdf
│   README.md
│
├───backend
│   │   Dockerfile
│   │   http_server.py
│   │   requirements.txt
│   │
│   └───templates
│           index.html
│
└───nginx
        nginx.html
```

▶️ Запуск проекта

Для запуска проекта нужно сначало собрать образ backend
  
    docker build backend/.  -t my-web-app:1.0  
После этого можно собрать контейнеры, благодоря инструкции docker-compose.yml (--build — заставляет Docker Compose пересобрать все образы, если они были изменены)
    
    docker compose up -d  --build 
Останавливает контейнеры из docker-compose.yml, также удаляет их и удаляет сети.
    
    docker compose down
    
🔍 Диагностика

Проверить статус контейнеров
    
    docker ps
Если статус например unhealty, можем узнать почему
    
    docker inspect <container_name> --format='{{json .State.Health}}' 
Также можно узнать логи
    
    docker logs <container_name>

✅ Проверка работоспособности

После запуска выполните:

    curl http://localhost
Ожидаемый результат:
 
     Hello from Effective Mobile!
