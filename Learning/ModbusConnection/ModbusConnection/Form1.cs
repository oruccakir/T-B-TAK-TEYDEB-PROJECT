using EasyModbus;
using System.Data;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace ModbusConnection
{
    public partial class Form1 : Form
    {

        const int MFC1 = 0;
        const int MFC2 = 1;
        const int MFC3 = 2;
        const int MFC4 = 3;
        const byte analogInput = 2;
        const byte analogOutput = 1;

        private ModbusClient client;
        public Form1(string portID, int slaveNumID, int baudrate, int parity)
        {
            InitializeComponent();
            this.client = new ModbusClient(portID);
            this.client.UnitIdentifier = (byte)(slaveNumID);
            this.client.Baudrate = baudrate;
            if (parity == 0)
                this.client.Parity = System.IO.Ports.Parity.None;
            else if (parity == 1)
                this.client.Parity = System.IO.Ports.Parity.Odd;
            else if (parity == 2)
                this.client.Parity = System.IO.Ports.Parity.Even;
            else
                this.client.Parity = System.IO.Ports.Parity.None;

            flowLayoutPanel1.BackColor = Color.Red;

        }

        private async void read_Click(object sender, EventArgs e)
        {

            if (this.client.Connected == false)
            {
                MessageBox.Show("Attempt to read without connected");
                return;
            }
            this.client.UnitIdentifier = analogInput;
            Console.WriteLine("Reading Started");
            timer1.Start();
        }

        private void set_Click(object sender, EventArgs e)
        {

            if (this.client.Connected == false)
            {
                MessageBox.Show("Attempt to set without connected");
                return;
            }

            this.client.UnitIdentifier = (analogOutput);
            string str1 = set_MFC1Box.Text;
            string str2 = set_MFC2Box.Text;
            string str3 = set_MFC3Box.Text;
            string str4 = set_MFC4Box.Text;
            if (str1.Length != 0)
            {
                set_button_helper(str1, MFC1);
            }
            if (str2.Length != 0)
            {
                set_button_helper(str2, MFC2);
            }
            if (str3.Length != 0)
            {
                set_button_helper(str3, MFC3);
            }
            if (str4.Length != 0)
            {
                set_button_helper(str4, MFC4);
            }

        }

        private void connect_Click(object sender, EventArgs e)
        {

            if (this.client.Connected == false)
            {
                this.client.Connect();
                flowLayoutPanel1.BackColor = Color.Green;
            }
            else
            {

                Console.WriteLine("Connected");
            }

        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            this.client.UnitIdentifier = analogInput;
            read_Box1.Text = ((float)this.client.ReadHoldingRegisters(MFC1 + 1, 1)[0] / (float)25).ToString();
            read_Box2.Text = ((float)this.client.ReadHoldingRegisters(MFC1 + 1, 1)[0] / (float)25).ToString();
            read_Box3.Text = ((float)this.client.ReadHoldingRegisters(MFC3 + 1, 1)[0] / (float)25).ToString();
            read_Box4.Text = ((float)this.client.ReadHoldingRegisters(MFC4 + 1, 1)[0] / (float)25).ToString();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Interval = 1000;
            timer1.Tick += timer1_Tick;
        }

        private void set_button_helper(string str, int mfc_num)
        {
            if (this.client.Connected == false)
            {
                MessageBox.Show("Attempt to set without connected");
                return;
            }
            this.client.UnitIdentifier = analogOutput;
            if (str.Length != 0)
            {
                int value = int.Parse(str);
                if (value < 0 || value > 20)
                {
                    MessageBox.Show("Value must be between 0 and 20 sscm");
                    return;
                }
                else
                {
                    value *= 25;
                    Console.WriteLine("Value: " + value);
                }
                this.client.WriteSingleRegister(mfc_num, value);
            }
        }

        private void set_MFC1Button_Click(object sender, EventArgs e)
        {
            set_button_helper(set_MFC1Box.Text, MFC1);
        }

        private void set_MFC2Button_Click(object sender, EventArgs e)
        {
            set_button_helper(set_MFC2Box.Text, MFC2);
        }

        private void set_MFC3Button_Click(object sender, EventArgs e)
        {
            set_button_helper(set_MFC3Box.Text, MFC3);
        }

        private void set_MFC4Button_Click(object sender, EventArgs e)
        {
            set_button_helper(set_MFC4Box.Text, MFC4);
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
