using OxyPlot;
using OxyPlot.Series;
using OxyPlot.Axes;
using System;
using System.Collections.Generic;
using System.IO;
using OxyPlot.WindowsForms;

class Program
{
    static void Main(string[] args)
    {
       var model = new PlotModel { Title = "Counted steps and Asymptotic running time" };
        var countedStepsSeries = new LineSeries { Title = "counted steps", Color = OxyColors.Red };
        var asymptoticSeries = new LineSeries { Title = "O(n^2)", Color = OxyColors.Green };

        var scatterSeries = new ScatterSeries { Title = "approximation of c" };

        List<int> B = new List<int> { 5, 2, 4, 6, 1, 3 };
        int points = 13;
        List<double> x = new List<double>(), y = new List<double>(), refValues = new List<double>(), c = new List<double>();

        for (int i = 0; i < points; i++)
        {
            Console.WriteLine($"{i + 1}/{points}");
            int steps = InsertionSort(B.ToArray()); // Implement this method
            B.AddRange(B); // Double the size of the list
            x.Add(B.Count);
            y.Add(steps);
            c.Add(steps / Math.Pow(B.Count, 2));
        }

        double cReference = c[6];
        for (int i = 0; i < x.Count; i++)
        {
            countedStepsSeries.Points.Add(new DataPoint(x[i], y[i]));
            asymptoticSeries.Points.Add(new DataPoint(x[i], cReference * Math.Pow(x[i], 2)));
            scatterSeries.Points.Add(new ScatterPoint(x[i], c[i]));
        }

        model.Series.Add(countedStepsSeries);
        model.Series.Add(asymptoticSeries);
        model.Series.Add(scatterSeries);
        var pngExporter = new PngExporter { Width = 600, Height = 400, Background = OxyColors.White };
        using (var stream = File.Create("plot.png"))
        {
            pngExporter.Export(model, stream);
        }

        Console.WriteLine("Plot exported as 'plot.png'");
    }

    static int InsertionSort(int[] arr)
    {
        // Insertion sort will be implemented here and called in main
        int steps = 0;
        for (int i = 1; i < arr.Length; i++)
        {
            int j = i;
            while (j > 0 && arr[j - 1] > arr[j])
            {
                int temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
                j--;
                steps++;
            }
        }
        return steps;
    }
}
