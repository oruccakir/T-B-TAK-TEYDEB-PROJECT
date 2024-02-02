

using EasyModbus;

namespace ModbusConnection
{
    public partial class Form1 : Form
    {
        private ModbusClient client;
        public Form1(ModbusClient client)
        {
            InitializeComponent();
            this.client = client;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Reading started");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Serting started");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            
            //this.client.Connect();
            Console.WriteLine("Connection Completed");
        }
    }
}
