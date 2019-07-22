//Importar libreria
#include <Servo.h>
//Crear variable tipo servo
Servo m1;

void setup()
{
  Serial.begin(9600);
  //Se especifica el pin donde esta conectado el servo  
  m1.attach(2);
}

void loop()
{
  //Mueve a 0 grados
  m1.write(0);
  delay(1000);
  //Mueve a 90 grados
  m1.write(90);
  delay(1000);
  //Mueve a 180 grados
  m1.write(180);
  delay(1000);
}
