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

message_dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
print(message_dt)
print((datetime.now().strftime('%d.%m.%Y %H:%M:%S')))



# TODO Создать в systemd/gunicorn.service

'''
sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart
'''