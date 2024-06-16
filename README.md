Решение команды NoLosJune для алгоритма для поиска предложенных скидок в телефонных разговорах с клиентами

## Сборка Docker-образа

1. Создание образа:
   ```bash
   docker build -t plane .
   ```
3. Запуск контейнера:
   ```bash
   docker run -p 8000:8000 -d --name plane-container plane
   ```

## Пример запроса

Наш сервер уже развернут, Вы можете попробовать его по адресу: 158.160.116.205:8000

```python
import requests
r = requests.post("http://158.160.116.205:8000/predict", json={"data":"скидка два процента"})
print(r.content)
```

```python
b'{"result":["B-discount","B-value","I-value"]}'
```

## Диаграмма

Техническая реализация экспертной системы представлена диаграммой ниже

![diagram](pictures/diagram.jpg)

