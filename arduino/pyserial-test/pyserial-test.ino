void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}



void loop() {
  byte var1,var2,var3;
  var1 = Serial.read();
  var2 = Serial.read();
  var3 = Serial.read();


  if (var1 == '1' && var2 == '9'){
    Serial.println("come!");
  }

  //Serial.println(var);

//  int val = var - 0x30;
  int val = var1 - '0';
//  int val = int(var);


//  Serial.print(var-'0');
//  Serial.print("hoge\n");  

//  if (var1 != 207){
//    Serial.print(val);
//    Serial.print("\n");  
//  }
//
//  if (val == 1){
//    Serial.print("HEY");
//  }
//
  
  switch(var1){
    case '0':
      digitalWrite(13, LOW);
      //Serial.println(var-'0');
      break;
    case '1':
      digitalWrite(13, HIGH);
      //Serial.println(var-'0');
      break;
    default:
      break;
  }
}
