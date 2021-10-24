using ScottPlot;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Text;
using System.Windows.Media.Imaging;

namespace lab_01
{
    public static class Chart
    {
        //private static string path = @"C:\Users\ASukocheva\source\repos\BMSTU7_MODELING\lab_01\lab_01\charts\chart.png";
        
        public static BitmapImage Draw(double[] xs, double[] ys, string xLable = "", string yLable = "", string title = "Titile")
        {
            var plt = new Plot(600, 400);

            //plt.AddScatter(xs, ys);
            plt.AddScatterLines(xs, ys, lineWidth: 3);

            plt.Title(title);
            plt.XLabel(xLable);
            plt.YLabel(yLable);

            Debug.WriteLine($"xs = {xs.Length} ys = {ys.Length}");
            //plt.SaveFig(path);

            return BitmapToImageSource(plt.Render());
        }

        private static BitmapImage BitmapToImageSource(Bitmap bitmap)
        {
            using (MemoryStream memory = new MemoryStream())
            {
                bitmap.Save(memory, System.Drawing.Imaging.ImageFormat.Bmp);
                memory.Position = 0;
                BitmapImage bitmapimage = new BitmapImage();
                bitmapimage.BeginInit();
                bitmapimage.StreamSource = memory;
                bitmapimage.CacheOption = BitmapCacheOption.OnLoad;
                bitmapimage.EndInit();

                return bitmapimage;
            }
        }
    }
}
