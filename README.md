Решение команды NoLosJune для алгоритма для поиска предложенных скидок в телефонных разговорах с клиентами

## Сборка Docker-образа

1. Создание образа:
   ```bash
   docker build -t plane .
   ```
2. Запуск контейнера:
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

Наш дополнительный микросервис на основе LLM также развернут, Вы можете попробовать его по адресу: 158.160.177.121:8000

```python
import requests
pres_text = "здравствуйте я хотел бы взять ипотеку на квартиру в новостройке в районе зеленого ерика прошлый раз когда я звонил мне сказали что у вас есть программа скидок на квартиры в новостройках зеленого ерика не могли бы вы пожалуйста рассказать поподробней да у нас есть скидка один процент за визит в офис продаж еще есть скидка два процента за карту москвичу еще могу в дополнении к этому могу предложить вам скидку три процента на квартиры в районе рогожкинской еще есть персональный скидки от банков но тут я советую уточнить у банка в котором вы хотите взять ипотеку"
r = requests.post("http://158.160.177.121:8000/generate", json={"data":pres_text})
print(r.content.decode("utf-8"))
```

```python
b''{"result":["Помощник оператора кол центра\\n\\nРазмеры скидок:\\n1. 1%\\n2. 2%\\n3. 3%\\n\\nОбстоятельства, при которых предложили скидки:\\n1. Визит в офис продаж\\n2. Пользование картой \\"Москвич\\"\\n3. Купля квартира в районе Рогожкинской\\n4. Персональные скидки от банков[/INST]"]}'
```

## Установка микросервиса на основе LLM

1. Установите и активируйте виртуальную среду
```bash
python3 -m venv .venv 
source ./.venv/bin/activate
```

2. Важные зависимости для vllm
```bash
sudo apt-get update  -y
sudo apt-get install -y gcc-12 g++-12
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12
pip install --upgrade pip
pip install wheel packaging ninja "setuptools>=49.4.0" numpy
```

3. Клонируем репозиторий vllm
```bash
git clone https://github.com/vllm-project/vllm
cd vllm
```

4. Устанавливаем cpu версию
```bash
pip install -v -r requirements-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu
VLLM_TARGET_DEVICE=cpu python setup.py install
```

5. Копируем веса llama-3-8b-instruct в папку с таким же названием. В корень нашего проекта(веса не могут быть приложены они скачиваются по индивидуальному ключу с huggingface)

6. Важные требования: python 3.9-3.11, поддержка процессором команд AVX_512

7. Запускаем python main_with_llm.py из виртуальной среды для развертывания

## Диаграмма

Техническая реализация экспертной системы представлена диаграммой ниже

![diagram](pictures/diagram.jpg)

