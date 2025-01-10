public class EntryTimingAgent
{
    public bool ShouldEnterAsset(string asset)
    {
        var priceData = GetPriceData(asset);
        bool isRSIInBuyZone = CalculateRSI(priceData) < 30;
        bool isNearSupport = priceData.Last().Price < GetSupportLevel(asset) * 1.05;

        return isRSIInBuyZone && isNearSupport;
    }

    private List<PricePoint> GetPriceData(string asset)
    {
        // Fetch historical price data for analysis
        return new List<PricePoint>
        {
            new PricePoint { Time = DateTime.Now.AddMinutes(-10), Price = 100 },
            new PricePoint { Time = DateTime.Now, Price = 95 }
        };
    }

    private double CalculateRSI(List<PricePoint> priceData)
    {
        // Placeholder for RSI calculation based on price changes
        return 25; // Example RSI value indicating oversold
    }

    private double GetSupportLevel(string asset)
    {
        // Example: Fetch support level based on historical price lows
        return 94;
    }
}

public class PricePoint
{
    public DateTime Time { get; set; }
    public double Price { get; set; }
}