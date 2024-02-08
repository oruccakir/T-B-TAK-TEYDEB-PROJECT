namespace ModbusConnection
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            read_button = new Button();
            set_button = new Button();
            connect_button = new Button();
            set_MFC1Box = new TextBox();
            set_MFC2Box = new TextBox();
            set_MFC3Box = new TextBox();
            set_MFC4Box = new TextBox();
            read_Box4 = new TextBox();
            timer1 = new System.Windows.Forms.Timer(components);
            flowLayoutPanel1 = new FlowLayoutPanel();
            set_MFC1Button = new Button();
            set_MFC2Button = new Button();
            set_MFC3Button = new Button();
            set_MFC4Button = new Button();
            read_Box2 = new TextBox();
            read_Box1 = new TextBox();
            read_Box3 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            SuspendLayout();
            // 
            // read_button
            // 
            read_button.BackColor = Color.Cornsilk;
            read_button.Font = new Font("Segoe UI", 9F, FontStyle.Bold | FontStyle.Underline, GraphicsUnit.Point, 162);
            read_button.Location = new Point(50, 209);
            read_button.Name = "read_button";
            read_button.Size = new Size(174, 79);
            read_button.TabIndex = 0;
            read_button.Text = "Read All";
            read_button.UseVisualStyleBackColor = false;
            read_button.Click += read_Click;
            // 
            // set_button
            // 
            set_button.BackColor = Color.FromArgb(224, 224, 224);
            set_button.Font = new Font("Segoe UI", 9F, FontStyle.Bold | FontStyle.Underline, GraphicsUnit.Point, 162);
            set_button.Location = new Point(675, 220);
            set_button.Name = "set_button";
            set_button.Size = new Size(207, 79);
            set_button.TabIndex = 1;
            set_button.Text = "Set All";
            set_button.UseVisualStyleBackColor = false;
            set_button.Click += set_Click;
            // 
            // connect_button
            // 
            connect_button.BackColor = Color.DarkGray;
            connect_button.ForeColor = Color.DarkCyan;
            connect_button.Location = new Point(372, 459);
            connect_button.Name = "connect_button";
            connect_button.Size = new Size(177, 71);
            connect_button.TabIndex = 2;
            connect_button.Text = "Connect";
            connect_button.UseVisualStyleBackColor = false;
            connect_button.Click += connect_Click;
            // 
            // set_MFC1Box
            // 
            set_MFC1Box.BackColor = Color.LightYellow;
            set_MFC1Box.Location = new Point(813, 351);
            set_MFC1Box.Name = "set_MFC1Box";
            set_MFC1Box.Size = new Size(74, 23);
            set_MFC1Box.TabIndex = 7;
            // 
            // set_MFC2Box
            // 
            set_MFC2Box.BackColor = Color.Ivory;
            set_MFC2Box.Location = new Point(813, 405);
            set_MFC2Box.Name = "set_MFC2Box";
            set_MFC2Box.Size = new Size(72, 23);
            set_MFC2Box.TabIndex = 8;
            // 
            // set_MFC3Box
            // 
            set_MFC3Box.BackColor = Color.Ivory;
            set_MFC3Box.Location = new Point(814, 459);
            set_MFC3Box.Name = "set_MFC3Box";
            set_MFC3Box.Size = new Size(74, 23);
            set_MFC3Box.TabIndex = 9;
            // 
            // set_MFC4Box
            // 
            set_MFC4Box.BackColor = Color.Ivory;
            set_MFC4Box.Location = new Point(815, 512);
            set_MFC4Box.Name = "set_MFC4Box";
            set_MFC4Box.Size = new Size(73, 23);
            set_MFC4Box.TabIndex = 10;
            // 
            // read_Box4
            // 
            read_Box4.Location = new Point(154, 512);
            read_Box4.Name = "read_Box4";
            read_Box4.Size = new Size(79, 23);
            read_Box4.TabIndex = 11;
            // 
            // timer1
            // 
            timer1.Tick += timer1_Tick;
            // 
            // flowLayoutPanel1
            // 
            flowLayoutPanel1.BackColor = Color.Red;
            flowLayoutPanel1.Location = new Point(372, 391);
            flowLayoutPanel1.Name = "flowLayoutPanel1";
            flowLayoutPanel1.Size = new Size(177, 36);
            flowLayoutPanel1.TabIndex = 13;
            // 
            // set_MFC1Button
            // 
            set_MFC1Button.BackColor = Color.FromArgb(255, 192, 128);
            set_MFC1Button.Location = new Point(672, 350);
            set_MFC1Button.Name = "set_MFC1Button";
            set_MFC1Button.Size = new Size(78, 23);
            set_MFC1Button.TabIndex = 14;
            set_MFC1Button.Text = "set_MFC1";
            set_MFC1Button.UseVisualStyleBackColor = false;
            set_MFC1Button.Click += set_MFC1Button_Click;
            // 
            // set_MFC2Button
            // 
            set_MFC2Button.BackColor = Color.FromArgb(255, 192, 128);
            set_MFC2Button.Location = new Point(672, 404);
            set_MFC2Button.Name = "set_MFC2Button";
            set_MFC2Button.Size = new Size(75, 23);
            set_MFC2Button.TabIndex = 15;
            set_MFC2Button.Text = "set_MFC2";
            set_MFC2Button.UseVisualStyleBackColor = false;
            set_MFC2Button.Click += set_MFC2Button_Click;
            // 
            // set_MFC3Button
            // 
            set_MFC3Button.BackColor = Color.FromArgb(255, 192, 128);
            set_MFC3Button.Location = new Point(672, 457);
            set_MFC3Button.Name = "set_MFC3Button";
            set_MFC3Button.Size = new Size(75, 23);
            set_MFC3Button.TabIndex = 16;
            set_MFC3Button.Text = "set_MFC3";
            set_MFC3Button.UseVisualStyleBackColor = false;
            set_MFC3Button.Click += set_MFC3Button_Click;
            // 
            // set_MFC4Button
            // 
            set_MFC4Button.BackColor = Color.FromArgb(255, 192, 128);
            set_MFC4Button.Location = new Point(675, 515);
            set_MFC4Button.Name = "set_MFC4Button";
            set_MFC4Button.Size = new Size(75, 23);
            set_MFC4Button.TabIndex = 17;
            set_MFC4Button.Text = "set_MFC4";
            set_MFC4Button.UseVisualStyleBackColor = false;
            set_MFC4Button.Click += set_MFC4Button_Click;
            // 
            // read_Box2
            // 
            read_Box2.Location = new Point(156, 405);
            read_Box2.Name = "read_Box2";
            read_Box2.Size = new Size(77, 23);
            read_Box2.TabIndex = 18;
            // 
            // read_Box1
            // 
            read_Box1.Location = new Point(154, 351);
            read_Box1.Name = "read_Box1";
            read_Box1.Size = new Size(79, 23);
            read_Box1.TabIndex = 19;
            // 
            // read_Box3
            // 
            read_Box3.Location = new Point(154, 458);
            read_Box3.Name = "read_Box3";
            read_Box3.Size = new Size(79, 23);
            read_Box3.TabIndex = 20;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.ForeColor = Color.RosyBrown;
            label1.Location = new Point(50, 350);
            label1.Name = "label1";
            label1.Size = new Size(66, 15);
            label1.TabIndex = 21;
            label1.Text = "read_MFC1";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.ForeColor = Color.RosyBrown;
            label2.Location = new Point(50, 404);
            label2.Name = "label2";
            label2.Size = new Size(66, 15);
            label2.TabIndex = 22;
            label2.Text = "read_MFC2";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.ForeColor = Color.RosyBrown;
            label3.Location = new Point(50, 457);
            label3.Name = "label3";
            label3.Size = new Size(66, 15);
            label3.TabIndex = 23;
            label3.Text = "read_MFC3";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.ForeColor = Color.RosyBrown;
            label4.Location = new Point(50, 515);
            label4.Name = "label4";
            label4.Size = new Size(66, 15);
            label4.TabIndex = 24;
            label4.Text = "read_MFC4";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.DarkSlateGray;
            ClientSize = new Size(934, 569);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(read_Box3);
            Controls.Add(read_Box1);
            Controls.Add(read_Box2);
            Controls.Add(set_MFC4Button);
            Controls.Add(set_MFC3Button);
            Controls.Add(set_MFC2Button);
            Controls.Add(set_MFC1Button);
            Controls.Add(read_button);
            Controls.Add(flowLayoutPanel1);
            Controls.Add(read_Box4);
            Controls.Add(set_MFC4Box);
            Controls.Add(set_MFC3Box);
            Controls.Add(set_MFC2Box);
            Controls.Add(set_MFC1Box);
            Controls.Add(connect_button);
            Controls.Add(set_button);
            ForeColor = Color.Black;
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button read_button;
        private Button set_button;
        private Button connect_button;
        private TextBox set_MFC1Box;
        private TextBox set_MFC2Box;
        private TextBox set_MFC3Box;
        private TextBox set_MFC4Box;
        private TextBox read_Box4;
        private System.Windows.Forms.Timer timer1;
        private FlowLayoutPanel flowLayoutPanel1;
        private Button set_MFC1Button;
        private Button set_MFC2Button;
        private Button set_MFC3Button;
        private Button set_MFC4Button;
        private TextBox read_Box2;
        private TextBox read_Box1;
        private TextBox read_Box3;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
    }
}
