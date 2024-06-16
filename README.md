Решение команды NoLosJune для алгоритма для поиска предложенных скидок в телефонных разговорах с клиентами

## Сборка Docker-образа



## Развертывание



## Пример запроса

```python
import requests
r = requests.post("http://0.0.0.0:8000/predict", json={"data":"скидка два процента"})
print(r.content)
```

```python
b'{"result":["B-discount","B-value","I-value"]}'
```

## Диаграмма

Техническая реализация экспертной системы представлена диаграммой ниже

![diagram](pictures/diagram.jpg)

