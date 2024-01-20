# Елена Леверкина, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.GET_ENDPOINT}"
    par = {'t': track_number}
    response = requests.get(get_order_url, par)
    return response