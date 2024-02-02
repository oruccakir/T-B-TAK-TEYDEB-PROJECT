namespace ModbusConnection
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Reading started");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Serting started");
        }
    }
}
