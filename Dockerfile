FROM python:3.10-alpine

# Устанавливаем рабочую директорию
WORKDIR /src

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Копируем весь код проекта

