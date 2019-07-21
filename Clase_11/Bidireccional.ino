String codigo;
int longitud;
char dato;
int valor; 

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  //pinMode(2,INPUT_PULLUP);
  //pinMode(3,INPUT_PULLUP);
}
void loop() {

//int pul1;
//int pul2;

  //Verifica si hay datos en el buffer
  if(Serial.available()){
    //Guarda los datos del buffer en codigo
    codigo = Serial.readString();
    //Guarda la longitud del mensaje en la variable longitud
    longitud = codigo.length();
    //Extrae el ultimo caracter del mensaje en dato
    dato = codigo[longitud-1]; 
    //Remueve el ultimo caracter del mensaje
    codigo.remove(longitud-1,1);
    //convierte el mensaje en un entero
    valor = codigo.toInt();
    
    Serial.print(valor);
    Serial.print("    ");
    Serial.println(dato);
//    delay(1000);
    }

// pul1 = digitalRead(2);
// pul2 = digitalRead(3);
// Serial.print("PULSADOR1: ");
// Serial.print(pul1);
// Serial.print("           ");
// Serial.print("PULSADOR2: ");
// Serial.println(pul2);
// delay(20);
}
