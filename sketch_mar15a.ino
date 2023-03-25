
const int speed = 9600;  //скорость COM-порта!!! обязательно должна совпадать со скоростью на компе

class SZI{
  public:
SZI(String n, int num) : nameSzi{ n }, number {num}
	{

    }
    void Szi_ON(){ //метод для включения СЗИ
      digitalWrite(number, HIGH); //"включаем" пин
      condition = true;
      Serial.println("SZI number " + nameSzi + " is ON"); // посылаем на комп сообщение
    }

    void Szi_OFF(){  //метод для выключения СЗИ
      digitalWrite(number, LOW); //"выключаем" пин
      condition = false;
      Serial.println("SZI number " + nameSzi + " is OFF");  // посылаем на комп сообщение
}
  private:
    bool condition = false;
    String nameSzi;
    int number;
};

SZI Szi1("Supra", 10);
SZI Szi2("Billy", 11);
SZI Szi3("Van", 12);

bool ReadCom(){ //читаем команду с компа
  String str = Serial.readString(); //пишем ее в строку
  if (str=="comm1\n"){ //сравниваем с захардкоженеми командами
    Szi1.Szi_ON(); // выполныем функцию и возвращаем успех
    return(1);
  }
  else
    if (str=="comm2\n"){
      Szi2.Szi_ON();
      return(1);
    }
    else
      if (str=="comm3\n"){
        Szi3.Szi_ON();
        return(1);
      }
      else
        if (str=="comm4\n"){
          Szi1.Szi_OFF();
          return(1);
        }
        else
          if (str=="comm5\n"){
            Szi2.Szi_OFF();
            return(1);
          }
          else
            if (str=="comm6\n"){
              Szi3.Szi_OFF();
              return(1);
            }
            else
              return(0); //возвращаем неудачу
  }

void setup() { //описываем что нужно из функций контроллера
  Serial.begin(speed); //СОМ-порт
  Serial.setTimeout(50); 
  pinMode(10, OUTPUT); //пины
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {     //основной цикл, выполняется покругу всегда
  if (Serial.available()) { //если в буфере СОМ-порта что-то есть, вызываем функцию чтения команды
    bool success = ReadCom();
    Serial.println(success ? "Command is correct" : "Command is shit"); //отправляем отчет на комп
  }
}
