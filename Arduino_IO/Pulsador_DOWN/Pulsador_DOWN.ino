void setup()
{
  //Configuracion del pin 2 como entrada
  //PULLUP => Sin resistencia
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop()
{
  //Lectura en el pin digital #2
  int pul = digitalRead(2);
  
  if (pul==0){
  
    Serial.println("Precionado");
    
  }else{
   
    Serial.println("No Precionado");
  }
}
