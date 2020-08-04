#define trig 7 // Emisor de pulso o señal

#define echo 6 // Receptor "del eco" del pulso o señal

#define buzzer 12 //Zumbador

void setup() {
  // Sólo se activa una vez al iniciarse el programa. Definimos entradas y salidas

  pinMode(trig, OUTPUT); //Emisor

  pinMode(echo, INPUT); //Receptor

  pinMode(buzzer, OUTPUT); //Emisor

}

void loop() {
  // Bucle

  long duration, distance; //Establecemos duration y distance como variables numéricas extensas

  digitalWrite(trig, LOW); //Para tener un pulso limpio empezamos con 2 microsegundos en apagado

  delay(2);

  digitalWrite(trig, HIGH); //Mandamos un pulso de 5 microsegundos

  delay(5);

  digitalWrite(trig, LOW); //Apagamos

  duration = pulseIn(echo, HIGH); //Medimos el tiempo que la señal tarda en volver al sensor en microsegundos

  distance = (duration/2)*0.0343; //La distancia es el tiempo por la velocidad del sonido (343 m/s = 0.0343 cm/microseg)

  if (distance < 10) //Si la distancia es menor de un metro y medio
  
{ tone(buzzer, 1000); //Suena el zumbador con una frecuencia de 1000Hz

  delay(5000); //durante 5 segundos
}
else //De lo contrario
{
  noTone(buzzer);//no suena
}
}


 
