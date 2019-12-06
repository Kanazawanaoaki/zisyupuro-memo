const int Pin1 = 4;
const int Pin2 = 5;
const int Pwm = 6;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
  pinMode(Pin1,OUTPUT);
  pinMode(Pin2,OUTPUT);
  pinMode(Pwm,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("start 40\n");
  digitalWrite(Pin1,HIGH);
  digitalWrite(Pin2,LOW);
  analogWrite(Pwm,80);
  delay(3000);

  Serial.print("stop\n");
  digitalWrite(Pin1,LOW);
  digitalWrite(Pin2,LOW);
  //analogWrite(Pwm,40);
  delay(3000);
//  
//  Serial.print("200\n");
//  digitalWrite(Pin1,HIGH);
//  digitalWrite(Pin2,LOW);
//  analogWrite(Pwm,80);
//  delay(5000);
//  
//  Serial.print("100\n");
//  digitalWrite(Pin1,LOW);
//  digitalWrite(Pin2,HIGH);
//  analogWrite(Pwm,40);
//  delay(5000);
//
//  Serial.print("200\n");
//  digitalWrite(Pin1,LOW);
//  digitalWrite(Pin2,HIGH);
//  analogWrite(Pwm,80);
//  delay(5000);
//
//  Serial.print("free\n");
//  digitalWrite(Pin1,LOW);
//  digitalWrite(Pin2,HIGH);
//  delay(5000);
}
