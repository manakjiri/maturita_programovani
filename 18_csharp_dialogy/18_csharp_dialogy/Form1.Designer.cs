namespace _18_csharp_dialogy
{
    partial class Form1
    {
        /// <summary>
        /// Vyžaduje se proměnná návrháře.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Uvolněte všechny používané prostředky.
        /// </summary>
        /// <param name="disposing">hodnota true, když by se měl spravovaný prostředek odstranit; jinak false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Kód generovaný Návrhářem Windows Form

        /// <summary>
        /// Metoda vyžadovaná pro podporu Návrháře - neupravovat
        /// obsah této metody v editoru kódu.
        /// </summary>
        private void InitializeComponent()
        {
            this.BackColor_Dialog = new System.Windows.Forms.ColorDialog();
            this.Font_Dialog = new System.Windows.Forms.FontDialog();
            this.Open_Dialog = new System.Windows.Forms.OpenFileDialog();
            this.Save_Dialog = new System.Windows.Forms.SaveFileDialog();
            this.Content_Text = new System.Windows.Forms.RichTextBox();
            this.Open_Button = new System.Windows.Forms.Button();
            this.Save_Button = new System.Windows.Forms.Button();
            this.Font_Button = new System.Windows.Forms.Button();
            this.BackColor_Button = new System.Windows.Forms.Button();
            this.TextColor_Dialog = new System.Windows.Forms.ColorDialog();
            this.TextColor_Button = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // BackColor_Dialog
            // 
            this.BackColor_Dialog.Color = System.Drawing.Color.White;
            // 
            // Open_Dialog
            // 
            this.Open_Dialog.DefaultExt = "txt";
            this.Open_Dialog.Filter = "Textové soubory|*.txt|Všechny soubory|*.*";
            this.Open_Dialog.InitialDirectory = "C:/Documents";
            this.Open_Dialog.Title = "Otevřít soubor";
            // 
            // Save_Dialog
            // 
            this.Save_Dialog.DefaultExt = "txt";
            this.Save_Dialog.Filter = "Textové soubory|*.txt|Všechny soubory|*.*";
            this.Save_Dialog.InitialDirectory = "C:/Documents";
            this.Save_Dialog.Title = "Uložit soubor";
            // 
            // Content_Text
            // 
            this.Content_Text.Location = new System.Drawing.Point(12, 12);
            this.Content_Text.Name = "Content_Text";
            this.Content_Text.Size = new System.Drawing.Size(650, 412);
            this.Content_Text.TabIndex = 0;
            this.Content_Text.Text = "";
            // 
            // Open_Button
            // 
            this.Open_Button.Location = new System.Drawing.Point(668, 12);
            this.Open_Button.Name = "Open_Button";
            this.Open_Button.Size = new System.Drawing.Size(120, 23);
            this.Open_Button.TabIndex = 1;
            this.Open_Button.Text = "Otevřít";
            this.Open_Button.UseVisualStyleBackColor = true;
            this.Open_Button.Click += new System.EventHandler(this.Open_Button_Click);
            // 
            // Save_Button
            // 
            this.Save_Button.Location = new System.Drawing.Point(668, 41);
            this.Save_Button.Name = "Save_Button";
            this.Save_Button.Size = new System.Drawing.Size(120, 23);
            this.Save_Button.TabIndex = 2;
            this.Save_Button.Text = "Uložit";
            this.Save_Button.UseVisualStyleBackColor = true;
            this.Save_Button.Click += new System.EventHandler(this.Save_Button_Click);
            // 
            // Font_Button
            // 
            this.Font_Button.Location = new System.Drawing.Point(668, 70);
            this.Font_Button.Name = "Font_Button";
            this.Font_Button.Size = new System.Drawing.Size(120, 23);
            this.Font_Button.TabIndex = 3;
            this.Font_Button.Text = "Font";
            this.Font_Button.UseVisualStyleBackColor = true;
            this.Font_Button.Click += new System.EventHandler(this.Font_Button_Click);
            // 
            // BackColor_Button
            // 
            this.BackColor_Button.Location = new System.Drawing.Point(668, 99);
            this.BackColor_Button.Name = "BackColor_Button";
            this.BackColor_Button.Size = new System.Drawing.Size(120, 23);
            this.BackColor_Button.TabIndex = 4;
            this.BackColor_Button.Text = "Barva pozadí";
            this.BackColor_Button.UseVisualStyleBackColor = true;
            this.BackColor_Button.Click += new System.EventHandler(this.BackColor_Button_Click);
            // 
            // TextColor_Button
            // 
            this.TextColor_Button.Location = new System.Drawing.Point(668, 128);
            this.TextColor_Button.Name = "TextColor_Button";
            this.TextColor_Button.Size = new System.Drawing.Size(120, 23);
            this.TextColor_Button.TabIndex = 5;
            this.TextColor_Button.Text = "Barva textu";
            this.TextColor_Button.UseVisualStyleBackColor = true;
            this.TextColor_Button.Click += new System.EventHandler(this.TextColor_Button_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.TextColor_Button);
            this.Controls.Add(this.BackColor_Button);
            this.Controls.Add(this.Font_Button);
            this.Controls.Add(this.Save_Button);
            this.Controls.Add(this.Open_Button);
            this.Controls.Add(this.Content_Text);
            this.Name = "Form1";
            this.Text = "Dialogy";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ColorDialog BackColor_Dialog;
        private System.Windows.Forms.FontDialog Font_Dialog;
        private System.Windows.Forms.OpenFileDialog Open_Dialog;
        private System.Windows.Forms.SaveFileDialog Save_Dialog;
        private System.Windows.Forms.RichTextBox Content_Text;
        private System.Windows.Forms.Button Open_Button;
        private System.Windows.Forms.Button Save_Button;
        private System.Windows.Forms.Button Font_Button;
        private System.Windows.Forms.Button BackColor_Button;
        private System.Windows.Forms.ColorDialog TextColor_Dialog;
        private System.Windows.Forms.Button TextColor_Button;
    }
}

