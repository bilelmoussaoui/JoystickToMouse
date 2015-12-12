const int xPin = 0;
const int yPin = 1;
const int btPin = 7;
 
void setup()
{
    pinMode(btPin,INPUT);
    digitalWrite(btPin, HIGH);
    Serial.begin(9600);
}
 
void loop()
{
  	if (Serial.available() > 0) {
		Serial.print(analogRead(xPin));
		Serial.print(analogRead(yPin));
		delay(100);
	}
}
