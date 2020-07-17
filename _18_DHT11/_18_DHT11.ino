#include <dht11.h>
#include <LiquidCrystal.h>
#define DHT11PIN 2
 
dht11 DHT11;
LiquidCrystal lcd(4, 6, 10, 11, 12, 13);

void setup()
{ 
    Serial.begin(9600);
    lcd.begin(16, 2);
    lcd.clear();
    delay(1000);
}
 
void loop()
{
    if(Serial.available() > 0){
        Serial.print((float)DHT11.humidity, 2);
        Serial.print("|");
        Serial.println((float)DHT11.temperature, 2);
    }

    int chk = DHT11.read(DHT11PIN);
    lcd.setCursor(0, 0);
    lcd.print("Humidade: ");
    lcd.print((float)DHT11.humidity, 2);
    lcd.print("%");
    
    lcd.setCursor(0, 1);
    lcd.print("Temp:    ");
    lcd.print((float)DHT11.temperature, 2);
    lcd.print(" C");
    delay(1000);
}
