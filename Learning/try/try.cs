
using EasyModbus;
using System;
class Modbus{


    int num;
    Modbus(int num)
    {
        this.num = num;
    }


 
    static void Main(string [] args){
        Modbus md = new Modbus(0);

        //string ipAddress = "klvnlkd";
        int portNumber = 0;

        ModbusClient client = new ModbusClient(ipAddress,portNumber);

        Console.WriteLine("Hello World");
        Console.WriteLine("Modbus connection");
        Console.ReadLine();
    }

}