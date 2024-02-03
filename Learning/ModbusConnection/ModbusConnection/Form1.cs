using EasyModbus;
using System.Windows.Forms.DataVisualization.Charting;
using System.Threading.Tasks;

namespace ModbusConnection
{
    public partial class Form1 : Form
    {

        private bool isReading = false;
        private Chart chart;
        private Series series;
        ChartArea chartArea;

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
            chart = new Chart();
            chart.Size = new Size(250, 250);
            chart.Location = new Point(10, 10);
            this.Controls.Add(chart);
            chartArea = new ChartArea();
            chart.ChartAreas.Add(chartArea);
            chartArea.AxisX.MajorGrid.Enabled = false;
            chartArea.AxisY.MajorGrid.Enabled = false;

            series = new Series
            {
                Name = "Series1",
                ChartType = SeriesChartType.Line
            };
            //series.ChartType = SeriesChartType.Point;

            chart.Series.Add(series);

        }

        private async void button1_Click(object sender, EventArgs e)
        {
            this.client.UnitIdentifier = (byte)(2);
            int i = 0;
            this.isReading = true;
            Console.WriteLine("Reading Started");

            while (this.isReading)
            {
                this.series.Points.AddXY(i, this.client.ReadHoldingRegisters(0, 1)[0]/100);
                await Task.Delay(1000);
                i++;
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
            
            Console.WriteLine("Set");
            this.client.WriteSingleRegister(0, 1000);
            this.client.WriteSingleRegister(1, 750);
            this.client.WriteSingleRegister(2, 250);
            this.client.WriteSingleRegister(3, 0);
            */
            this.isReading = false;
            this.client.UnitIdentifier = (byte)(1);
            string str1 = textBox5.Text;
            string str2 = textBox6.Text;
            string str3 = textBox7.Text;
            string str4 = textBox8.Text;
            int value;
            if (str1.Length != 0)
            {
                value = int.Parse(str1);
                this.client.WriteSingleRegister(0, value);
                
            }
            if (str2.Length != 0)
            {
                value = int.Parse(str2);
                this.client.WriteSingleRegister(1, value);
                
            }
            if (str3.Length != 0)
            {
               value = int.Parse(str3);
               this.client.WriteSingleRegister(2, value);
       
            }
            if (str4.Length != 0)
            {
               
              value = int.Parse(str4);
              this.client.WriteSingleRegister(3, value);
              
            }
            this.isReading = false;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.client.Connect();
            if (this.client.Connected)
                Console.WriteLine("Connected");
        }

        
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            string str = textBox1.Text;
            Console.WriteLine(int.Parse(str));
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox2.Text);
        }
       
        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox3.Text);
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox4.Text);
        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox5.Text);
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox6.Text);
        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox7.Text);
        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {
            Console.WriteLine(textBox8.Text);
        }
     
        
    }
}
