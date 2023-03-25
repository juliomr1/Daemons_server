import network
import time
import urequests

#wifi = network.WLAN(network.AP_IF) Para crear una red wifi
wifi = network.WLAN(network.STA_IF)
timeout = 0
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

#wifi.config(essid = 'TE VI PERRO2', password = '1083019146',authmode= network.AUTH_WPA_WPA2_PSK) crear uma red wifi
#networks = wifi.scan() ESCANEA LAS REDES WIFI
#print(networks) IMPRIMER LAS REDES WIFI ESCANEADAS
wifi.connect('TE VI PERRO','1083019146')

if not wifi.isconnected():
    print('connecting...')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)


if wifi.isconnected():
    print('connected')
    # req=urequests.get('http://127.0.0.1:8000/recibir_datos/')
    # print(req.status_code)
    # print(req.text)
    auth_data = {'id': 1,'corriente': 12, 'voltaje': 120}
    resp = urequests.post('http://127.0.0.1:8000/recibir_datos/', data=auth_data)

else:
    print('Tiem Out')
    print('Not Connected')
