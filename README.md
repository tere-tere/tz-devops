

Описание

Проект состоит из двух сервисов:
    Backend — простой HTTP-сервер на Python(flask), который отвечает на путь / текстом с html:
    <Hello from Effective Mobile!>
    Слушает порт 8080 внутри Docker-сети.

Nginx — reverse proxy, который принимает запросы на порт 80 и проксирует их на backend.
Схема работы:
    Client → Nginx → backend

Nginx под двумя сетями frontend,backend.
Backend только backend.

Для запуска проекта нужно сначало собрать образ
docker build backend/.  -t my-web-app:1.0  
После этого можно собрать контейнеры, благодоря инструкции docker-compose.yml
(--build — заставляет Docker Compose пересобрать все образы, если они были изменены)
docker compose up -d  --build 
Останавливает контейнеры из docker-compose.yml, также удаляет их и удаляет сети.
docker compose down
Проверить статус контейнеров
docker ps
Если статус например unhealty, можем узнать почему
docker inspect <container_name> --format='{{json .State.Health}}' 
Также можно узнать логи
docker logs <container_name>
