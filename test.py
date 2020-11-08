import requests

'''
import asyncio
from aiohttp import ClientSession
#
async def fetch(url, session):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print("{}:{} with delay {}".format(date, response.url, delay))
        return await response.read()
#
#
async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, session)
#
#
async def run(r):
    url = "http://194.58.118.237/"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)
#     # Create client session that will ensure we dont open new connection
     # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), session))
            tasks.append(task)
#
        responses = asyncio.gather(*tasks)
        await responses
#
number = 10000
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)
'''


quiz_data = {
    'sum': 'от 300 000 до 700 000 рублей',
    'amount': 'от 1 до 3',
    'has_delay': 'Да, менее 3-х месяцев',
    'income': 'от 20 000 до 30 000 рублей',
    'has_child': 'Нет',
    'is_marriage': 'Нет, в разводе',
    'property': 'Жилой дом, Коммерческая недвижимость, Единственное жилье',
    'own_per_marriage': 'Нет',
    'property_transaction': 'Нет',
    'pledge': 'Нет',
    'name': 'Артур',
    'city': 'Обнинск',
    'phone_number': '8 222 333 11 22',
    'email': 'www@nnn.com',
}
poll_data = {
    'summ': 'От 700 000 до 1 500 000 рублей',
    'amount': '4',
    'income': 'Более 30 000',
    'pledge': 'Да',
    'property': 'Гараж, Автомобиль',
    'city': 'Обниниск',
    'email': 'eee@ddd.com',
    'registration_city': 'Обнинск',
    'name': 'Артур',
    'phone_number': '8 222 333 99 00',
}



short_data = {
    'name': 'Artur',
    'phone': '8 222 333 77 88',
    'message': 'call me!',
    'email': 'rrr@xxx.com',
}


new_quiz_data = {
    'sum': 'от 300 000 до 700 000 рублей',
    'amount': 'от 1 до 3',
    'has_delay': 'Да, менее 3-х месяцев',
    'income': 'от 20 000 до 30 000 рублей',
    'has_child': 'Нет',
    'is_marriage': 'Нет, в разводе',
    'property': 'Жилой дом, Коммерческая недвижимость, Единственное жилье',
    'own_per_marriage': 'Нет',
    'property_transaction': 'Нет',
    'pledge': 'Нет',
    'name': 'Артур',
    'city': 'Обнинск',
    'phone_number': '8 222 333 11 22',
    'email': 'www@nnn.com',
}

post = requests.post('https://api.fl-bankrotstvo.ru/onepage/short/', data=short_data)
print(post.text)
post = requests.post('https://api.fl-bankrotstvo.ru/onepage/full/', data=poll_data)
print(post.text)
post = requests.post('https://api.fl-bankrotstvo.ru/onepage/quiz/', data=quiz_data)
print(post.text)
post = requests.post('https://api.fl-bankrotstvo.ru/onepage/new_quiz/', data=new_quiz_data)
print(post.text)

# from time import sleep
#
# for i in range(15):
#     try:
#         post = requests.post('https://api.fl-bankrotstvo.ru/onepage/quiz/', data=quiz_data)
#         print(post.text)
#     except Exception as e:
#         print(e)
#     sleep(2)

#194-58-118-237

# post = requests.post('http://194.58.118.237:9000/onepage/quiz/', data=quiz_data)
# print(post.text)
