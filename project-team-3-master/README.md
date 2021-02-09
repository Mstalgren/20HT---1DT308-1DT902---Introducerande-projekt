# project-team-3: Öka/minska ljusstyrka

## Bakgrund och idé 
Öka ljusstyrka på belysning vid aktivitet exempelvis gång- och cykelvägar. 
Bakgrunden till idén är att spara energi och öka tryggheten i Kalmar genom att tända/släcka belysningen efter olika situationer.

## Abstrakt
Genom att få lampor att tända och släcka vid behov, sparar kommunen inte bara energi, men även lampornas livslängd ökar. Dessutom så ger det lite mer trygghet för samhället, som t.ex. bilister som tydligare kan se ungefär vart människor rör sig i närheten där de kör, då lamporna lyser i samband med rörelse. 

## Metod
- [timelog.md](/docs/timelog.md)
- [requirements.md](/docs/requirements.md)
- [hardware.md](/docs/hardware.md)
- [setup.md](/docs/setup.md)
- [test.md](/docs/test.md)


## Resultat
I projektet användes 3 pycomenheter.

Två olika sensorer testades (PIR sensor och Ultrasonic sensor). Varje sensor kopplades till varsin pycomenhet.  
PIR sensor:  
![PIR sensor](/project-team-3-master/img/pir.jpg)

Ultrasonic sensor:  
![Ultrasonic sensor](/project-team-3-master/img/VideoCapture_20210114-201823_W900px.jpg)

En uppsättning hade en LED-lampa kopplad till en pycomenhet:  
![LED](/project-team-3-master/img/878B7261-3C98-4478-85B5-CCB6F25E4DDB_1_105_c.jpeg)

Data skickades via MQTT. Mqtt-servern som användes var Linnéuniversitetets mqtt-server.
PIR sensorn registrerar rörelse i 120 graders vinkel upp till 7 meter.
Ultrasonic sensorn mäter avstånd genom ljudvågor upp till 4,5 meter.
Båda sensorerna skickar värdet "1" när de upptäcker rörelse/objekt, annars skickar de värdet "0".

**Video om projektet:**  
[Kurs: 1DT308, Team 3: Öka/minska ljusstyrka](https://youtu.be/pWuaXn1YJ48)

### Reflektion
**LoRa**   
Detta projektet var tänkt att användas med LoRa eftersom det skickar små mängder data som LoRa passar för. Först användas TTN som mqtt-server där det gick bra att skicka data men inte ta emot på samma sätt som med Linnéuniversitets mqtt-server. Vi lyckades inte koppla ihop LoRa med en annan mqtt-server än TTN i det här projektet. Därför visar vår prototyp en variant med wifi och Linnéuniversitetets mqtt-server.

**Batteri**  
I verkligheten kommer en strömförsörjning alltid finnas tillgänglig då projektidén är tänkt för gatubelysning. I detta projektet har vi inte kopplat in batteri men den skulle fungera på det sättet även om det inte är syftet för en verklig produkt av den här prototypen.

**Dashboard**  
Ett av våra krav var att skapa en Dashboard. Dashboarden tänkte skapas via Ubidots via TTN men eftersom vi valde bort TTN i slutet av projektet skapades ingen Dashboard.
