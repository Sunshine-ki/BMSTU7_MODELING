using MathNet.Numerics;
using System;
using System.Collections.Generic;
using System.Text;

namespace lab_01
{
    public static class Distribution
    {
        public static double UniformDistribution(double a, double b, double x)
        {
            return a <= x && x <= b ? 1 / (b - a) : 0;
        }

        public static double UniformDistributionFunc(double a, double b, double x)
        {
            if (x < a)
            {
                return 0;
            }
            if (x > b)
            {
                return 1;
            }
            return (x - a) / (b - a);
        }

        public static double NormalDistribution(double m, double sig, double x)
        {
            return 1 / sig * Math.Sqrt(2 * Math.PI) * Math.Pow(Math.E, - Math.Pow(x - m, 2) / (2 * sig * sig));
        }

        public static double NormalDistributionFunc(double m, double sig, double x)
        {
            return (1 + SpecialFunctions.Erf((x - m) / sig / Math.Sqrt(2))) / 2;
        }

        public static double[] Apply(double[] xs, double a, double b, Func<double, double, double, double> f)
        {
            double[] ys = new double[xs.Length];

            for (int i = 0; i < xs.Length; i++)
            {
                ys[i] = f(a, b, xs[i]);
            }

            return ys;
        }
    }
}
