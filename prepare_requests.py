import requests
from datetime import datetime
#
# data = {
#     'name': 'test',
#     'phone': '123123',
#     'message': 'привет привет'
# }
#
# response = requests.post('http://77.244.65.15:9000/onepage/short/', data=data)
# print(response.status_code)
# print(response.headers)
# print(response.text)
#
# message_dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
# print(message_dt)
# print((datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
#


# TODO Создать в systemd/gunicorn.service
'''
sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart
'''

#
# for i in range(1000):
#     print(f'this is {i} time to request http://194.58.118.237/ ')
#     x = requests.get('http://194.58.118.237/')
#     print(x.status_code)
#
#
#
# modified fetch function with semaphore
import random
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


#data = {
#    'name': 'wwww',
#    'phone': '22222222',
#    'message': 'example msg',
#    'email': 'qwe@example.com'
#}
#x = requests.post('https://fl-bankrotstvo.ru/onepage/short/', data=data)
#print(x.status_code)
#print(x.text)
