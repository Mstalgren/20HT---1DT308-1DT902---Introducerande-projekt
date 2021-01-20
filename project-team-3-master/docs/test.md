# Test

# Kravspecifikation
1. Bygga en prototyp som visualiserar olika situationer
1. Sensorer som registrerar rörelse
   - a) Ultrasonic sensor
   - b) PIR sensor
1. ~~Standardläge/Säkert läge (t.ex. om något slutar fungera, låt lamporna lysa)~~
1. ~~Ev. en grafisk dashboard som visualiserar datan som registreras~~


## Krav 1: Bygga en prototyp som visualiserar olika situationer
Steg 1 i detta krav var att testa sensorernas möjlighet att registrera rörelse från människor. Detta gjordes genom att gå framför sensorn eller sträcka ut en hand framför sensorn. Sensorerna ställdes in på olika känsligheter (se mer information i krav 2).

Steg 2 var att testa hur sensorerna reagerade på bilar eller cyklar. Detta testet genomfördes tyvärr inte.

## Krav 2: Sensorer som registrerar rörelse
### Ultrasonic sensor
Det minst uppmätta avståndet som Ultrasonic-sensorn verkade reagera på var 5 cm. Under tiden prototypen testades var den inställd på 20 cm eller närmare. Denna sensorns känslighet styrs med hjälp av kod. En del problem uppstod och programmet frös. För att hitta felet letade vi upp stället där programmet fastnade genom att skriva print('valfri-text') på olika ställen. Programmet verkade fastna på nedanstående del i koden (rad 31-34) men varför detta skedde och bara ibland kom vi inte fram till:  
```
    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()
```

### PIR sensor
PIR-sensorn registrerade alltid rörelse på max-avståndet (7 meter). Den här sensorn behövde inte ställas in via kod vilket innebar mindre kodtest.

## Krav 3: Standardläge/Säkert läge (t.ex. om något slutar fungera, låt lamporna lysa)
Ej implementerat.

## Krav 4: Ev. en grafisk dashboard som visualiserar datan som registreras
I början skulle projektet vara kopplat till LoRa och TTN och därigenom skulle en dashboard skapas med Ubidots. När LoRa inte fungerade som tänkt (se nedan) blev detta kravet inte klart.

## Övrigt: LoRa 
Test på hur projektet reagerade utan LoRa testades genom att koppla upp prototyperna hemifrån då LoRa oftast inte fungerade på det avståndet från skolan där mottagen finns. Programmet var skrivet så att enheterna väntade tills en LoRa-uppkoppling var upprättad. I slutet av projektet fungerade det inte att ta emot data som tänkt och därför ändrades funktionen "skicka/ta emot data" från att använda LoRa till att använda wifi och mqtt. 



