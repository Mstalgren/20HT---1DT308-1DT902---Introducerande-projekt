# Hårdvara
Här nedan presenteras beskrivning av hårdvaran. Projektet innefattade tre olika varianter.

## Grunduppsättning: Pycomenhet
Enheter från Pycom:
- Expansion Board 3.1
- LoPy 4


## Sensorer / LED
Pycomenheterna ovan kopplas ihop genom någon av nedanstående varianter (PIR sensor, Ultrasonic sensor eller LED-lampa.)

### PIR Sensor
- [PIR MOTION SENSOR VMA314](https://www.velleman.eu/products/view/?id=435542)
- LED
- sladdar

<img src="/img/pir_led.jpg" width="500">

Kopplingschema
![PIR sensor schema](/img/cicuit_pir.png)

### Ultrasonic Sensor
- [HC-SCR05 Ultrasonic sensor](https://www.velleman.eu/products/view/?id=435526)
- 1 st grön LED
- 3 st resistorer (1kΩ)
- sladdar/ledare

Bild på uppsättning med LoRa-antenn (LoRa användes inte i slutresultatet):

![Ultrasonic sensor](/img/ultrasonic_edit_W600px.jpg)

Kopplingschema (utan LoRa-antenn):  
![Ultrasonic sensor koppling](/img/1DT308-circuit_ultrasonic_utanLoRa.jpg)

### LED-lampa
- 1 st grön LED
- sladdar/ledare

Kopplingschema (utan LoRa-antenn):

![Pycom och vanlig LED-lampa, koppling](/img/1DT308-circuit_lampa_utanLoRa.jpg)
![Pycom och vanlig LED-lampa, koppling](/img/878B7261-3C98-4478-85B5-CCB6F25E4DDB_1_105_c.jpeg)

