using System;
using System.Windows.Forms;

namespace _18_csharp_dialogy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Open_Button_Click(object sender, EventArgs e)
        {
            switch (Open_Dialog.ShowDialog())
            {
                case DialogResult.OK:
                    Content_Text.Text = System.IO.File.ReadAllText(Open_Dialog.FileName);
                    break;
            }
        }

        private void Save_Button_Click(object sender, EventArgs e)
        {
            switch (Save_Dialog.ShowDialog())
            {
                case DialogResult.OK:
                    System.IO.File.WriteAllText(Save_Dialog.FileName, Content_Text.Text);
                    break;
            }
        }

        private void Font_Button_Click(object sender, EventArgs e)
        {
            switch (Font_Dialog.ShowDialog())
            {
                case DialogResult.OK:
                    Content_Text.Font = Font_Dialog.Font;
                    break;
            }
        }

        private void BackColor_Button_Click(object sender, EventArgs e)
        {
            switch (BackColor_Dialog.ShowDialog())
            {
                case DialogResult.OK:
                    Content_Text.BackColor = BackColor_Dialog.Color;
                    break;
            }
        }

        private void TextColor_Button_Click(object sender, EventArgs e)
        {
            switch (TextColor_Dialog.ShowDialog())
            {
                case DialogResult.OK:
                    Content_Text.ForeColor = TextColor_Dialog.Color;
                    break;
            }
        }
    }
}
