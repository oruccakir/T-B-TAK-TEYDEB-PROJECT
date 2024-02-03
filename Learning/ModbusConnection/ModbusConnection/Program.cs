using System.Runtime.InteropServices;
using EasyModbus;

namespace ModbusConnection
    
{
    internal static class Program
    {

        [DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool AllocConsole();

        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            AllocConsole();
            Console.WriteLine("Connection Started");
            ModbusClient client = new ModbusClient();
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.Run(new Form1("COM12",1,9600,0));
            Console.ReadLine();
        }
    }
}