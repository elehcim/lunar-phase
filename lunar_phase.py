#!/bin/env python3

import sys
from datetime import datetime, timedelta, date

# W zì Luigi e ‘ra Busona!
# http://laboratoriocamenzind.blogspot.be/2016/03/zi-luigi-e-la-patta-della-luna.html?m=1

PATTA = {2015: 10}

TIME_FMT = '%Y-%m-%d'

def giorni_str(g):
	return str(g) + (' giorno' if g==1 else ' giorni') 

def patta(data):
	# nel 2015 la patta e' 10
	if data.year < 2015:
		raise NotImplementedError("Il calcolo per anni precedenti al 2015 non e' stato ancora implementato")
	scarto = data.year - 2015
	# patta lasts from March to March
	if data.month < 3:
		scarto -= 1
	patta = (PATTA[2015] + scarto * 11 ) % 30
	return patta

def luna(data=None):
	if data is None:
		data = datetime.now()

	data_str = data.strftime(TIME_FMT)

	print("La patta al {} e' {}".format(data_str, patta(data)))

	# luna = (data.day + ((data.month - 2 + 12)) % 13 + patta(data)) % 30

	luna = (data.day + ((data.month - 2)) % 12 + patta(data)) % 30 # FIXME

	if luna == 15:
		print("{} e' luna piena!".format(data_str))
	elif luna == 30:
		print("{} e' luna nuova!".format(data_str))
	elif 0 <= luna < 15: # fase crescente
		print("{} e' il giorno '{}' di luna crescente".format(data_str, luna))
		giorni_per_piena = 15 - luna
		prossima_piena = (data + timedelta(days=giorni_per_piena)).strftime(TIME_FMT)
		print("Prossima luna piena tra {}: {}".format(giorni_str(giorni_per_piena), prossima_piena))
	else:  # fase calante
		print("{} e' il giorno '{}' di luna calante".format(data_str, luna))
		giorni_per_nuova = 30 - luna
		giorni_da_piena = luna - 15
		prossima_nuova = (data + timedelta(days=giorni_per_nuova)).strftime(TIME_FMT)
		piena_passata = (data - timedelta(days=giorni_da_piena)).strftime(TIME_FMT)
		print("La luna piena e' stata {} fa: {}".format(giorni_str(giorni_da_piena), piena_passata))

		print("Prossima luna nuova tra {}: {}".format(giorni_str(giorni_per_nuova), prossima_nuova))
	return luna

def test_luna():
	assert luna(date(2015,8,4)) == 20 # come nel video al link https://www.youtube.com/watch?v=wB765_NX9PY
	assert luna(date(2017,8,4)) == 12
	assert luna(date(2017,12,3)) == 15 # https://www.timeanddate.com/moon/phases/
	assert luna(date(2017,12,22)) == 4
	assert luna(date(2017,2,11)) == 15 # https://www.timeanddate.com/moon/phases/


if __name__ == '__main__':
	luna()
