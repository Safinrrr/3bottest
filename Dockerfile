# Используем образ Python в качестве базы
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем необходимые зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем точку входа для запуска бота
CMD ["python", "bot.py"]
