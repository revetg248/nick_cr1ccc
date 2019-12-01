# AKOAZM
from telethon.sync import TelegramClient
from telethon import functions, types
import time
import codecs

try:
	file = codecs.open("names1.txt", 'r', "utf-8" )
	pause = '36'
	all_names = list()
	for line in file.readlines():
		all_names.extend(line.rstrip().split(' '))

	while True:
		for name in all_names:
			with TelegramClient('session', '972783', 'af13025a476bf0fc6c7a72402c1f1da2') as client:
				client(functions.account.UpdateProfileRequest(first_name=str(name)))
			print('Имя изменено на ' + name)
			time.sleep(int(pause))
except Exception as e:
	print('Ошибка -', e)
	wait = input('Нажмите ENTER для завершения:')
# AKOAZM