String codigo;
int longitud;
char dato;
int valor; 

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
}

void loop() {

//int analogo0;
//int analogo1;

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
    //delay(1000);
    }

 //analogo0 = analogRead(A0);
 //analogo1 = analogRead(A1);
 //Serial.print("Analogo0: ");
 //Serial.print(analogo0);
 //Serial.print("           ");
 //Serial.print("Analogo1: ");
 //Serial.println(analogo1);
 //delay(20);
}
