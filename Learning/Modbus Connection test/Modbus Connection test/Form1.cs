using System.Runtime.InteropServices;
using System;

namespace Modbus_Connection_test
{
    public partial class Form1 : Form
    {
        [DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool AllocConsole();

        public Form1()
        {
            InitializeComponent();
            AllocConsole();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Modbus Reading Started");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Modbus Setting Started");
        }
    }
}
