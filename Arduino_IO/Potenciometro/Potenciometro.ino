void setup()
{
  //Configuracion del pin 3 como salida
  //solo pines ~ (PWM)
  pinMode(3, OUTPUT);
  
}

void loop()
{
  digitalWrite(3,0);
  delay(300);
  digitalWrite(3,30);
  delay(300);
  digitalWrite(3,60);
  delay(300);
  digitalWrite(3,120);
  delay(300);
  digitalWrite(3,255);
  delay(300);
}
