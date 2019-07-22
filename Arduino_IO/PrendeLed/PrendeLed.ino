void setup()
{
  //Configuracion del pin 2 como salida
  pinMode(2, OUTPUT);
}

void loop()
{
  //Escritura en el pin digital #2
  digitalWrite(2, HIGH);
  delay(1000); 
  digitalWrite(2, LOW);
  delay(1000);
}
