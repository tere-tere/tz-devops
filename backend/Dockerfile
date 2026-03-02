#взять малый образ пайтона(Debian slim)
FROM python:3.14.3-slim

#создаем пользователя
#создаем пользователя -r(system) меньше прав
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

#установка библиотек пайтона
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Меняем владельца файлов
RUN chown -R appuser:appgroup /app
#был под рутом, стал аппюзер
USER appuser
#показыавет docker ps какой порт использует(документируем)
EXPOSE 8080
CMD ["python","http_server.py"]
