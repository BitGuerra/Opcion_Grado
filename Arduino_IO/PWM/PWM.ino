void setup()
{
  //Configuracion del pin 2 como entrada
  //DOWN => Con resistencia
  pinMode(2, INPUT);
  Serial.begin(9600);
}

void loop()
{
  //Lectura en el pin digital #2
  int pul = digitalRead(2);
  
  if (pul==1){
  
    Serial.println("Precionado");
    
  }else{
   
    Serial.println("No Precionado");
  }
}
