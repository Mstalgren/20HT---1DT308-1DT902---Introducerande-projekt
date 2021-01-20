# Setup

## Huvudprogram
### main.py
För att köra programmet måste id ändras till ett unikt namn.
main loopen kollar först om sensorn hittar något, om den gör det skickar den en signal till de andra enheterna och tänder sin egen lampa på hög styrka efter 5 sekunder dimmar den ner och efter 10 sekunder slocknar den. Sedan kollar den om någon annan sensor har skickat en signal, då tänds lampan på låg styrka och släcks efter 10 sekunder
## Sensorer / lib
Nedanstående filer placerades i en mapp kallad "lib".
### PIR sensor _(main.py)_
Pir sensorn ger värde 1 när den detekterar rörelse och 0 när den inte gör det.
### Ultrasonic sensor _(sensor_ultrasonic.py)_
Koden för Ultrasonic-sensorn är till stor del från en tutorial (källa: https://core-electronics.com.au/tutorials/hc-sr04-ultrasonic-sensor-with-pycom-tutorial.html) med små justeringar.
Sensorn mäter avståndet med ultraljud. Det görs en kalkylering där mätvärdet delas med 2 eftersom ljudet färdas sträckan två gånger (framåt tills den når ett objekt och sedan tillbaka efter pulsen har studsat tillbaka)
När ett objekt registreras skickar sensorn värdet "1" och annars skickas "0".
### Dimmerfunktion _(dimmer.py)_
Justerar en LEDs ljusstyrka genom att ändra dess duty cycle.
Den tar emot en variabel mellan 0-1 för ljusstyrka och en för vilken pin lampan är kopplad till
### MQTT _(main.py, mqtt.py)_
För att koppla upp till mqtt måste man först ange wifi namn och lösenord.
För att koppla till en mqtt server måste man ange adress namn och lösenord för servern.
