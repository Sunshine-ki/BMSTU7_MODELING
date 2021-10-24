using ScottPlot;
using System;
using System.Windows;
using System.Diagnostics;
using System.Windows.Media.Imaging;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace lab_01
{
    public partial class MainWindow : Window,  INotifyPropertyChanged
    {
        public MainWindow()
        {
            InitializeComponent();
            DataContext = this;
        }

        private BitmapImage _bitmap = null;
        private BitmapImage _bitmapFunc = null;

        public string A { get; set; } = "-5";
        public string B { get; set; } = "5";

        public string M { get; set; } = "5,0";
        public string Sigma { get; set; } = "0,5";


        public string Begin { get; set; } = "-10";
        public string End { get; set; } = "10";
        public string Spacing { get; set; } = "0,1";
        public BitmapImage BitMapImg
        { 
            get => _bitmap; 
            set { _bitmap  = value; OnPropertyChanged(); } 
        }

        public BitmapImage BitMapImgFunc
        {
            get => _bitmapFunc;
            set { _bitmapFunc = value; OnPropertyChanged(); }
        }
        

        public void OnClick_UniformDistribution(object sender, RoutedEventArgs e)
        {
            double a = Convert.ToDouble(A);
            double b = Convert.ToDouble(B);

            double[] xs = getXs();
            double[] ys = Distribution.Apply(xs, a, b, Distribution.UniformDistribution);
            double[] ysFunc = Distribution.Apply(xs, a, b, Distribution.UniformDistributionFunc);

            BitMapImg = Chart.Draw(xs, ys, title: "Плотность распределения");

            BitMapImgFunc = Chart.Draw(xs, ysFunc, title: "Распределение");
        }

        public void OnClick_NormalDistribution(object sender, RoutedEventArgs e)
        {
            double m = Convert.ToDouble(M);
            double sigma = Convert.ToDouble(Sigma);

            double[] xs = getXs();
            double[] ys = Distribution.Apply(xs, m, sigma, Distribution.NormalDistribution);
            double[] ysFunc = Distribution.Apply(xs, m, sigma, Distribution.NormalDistributionFunc);

            BitMapImg = Chart.Draw(xs, ys, title: "Плотность распределения");

            BitMapImgFunc = Chart.Draw(xs, ysFunc, title: "Распределение");
        }

        private double[] getXs()
        {
            var begin = Convert.ToDouble(Begin);
            var end = Convert.ToDouble(End);
            var spacing = Convert.ToDouble(Spacing);
            int pointCount = (int)((end - begin) / spacing);

            double[] xs = DataGen.Consecutive(pointCount, spacing: spacing, offset: begin);
            return xs;
        }

        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(prop));
        }
    }
}
