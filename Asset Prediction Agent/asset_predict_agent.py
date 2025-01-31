public class AssetPredictionAgent
{
    public string PredictAsset(string market)
    {
        var assets = GetAssets(market);
        var bestAsset = assets.OrderByDescending(a => a.ShortTermGainProbability * a.NewsImpactScore / a.Volatility).FirstOrDefault();
        return bestAsset?.Name ?? "None";
    }

    private List<Asset> GetAssets(string market)
    {
        // Example assets fetched based on market type
        return market switch
        {
            "Crypto" => new List<Asset>
            {
                new Asset { Name = "BTC", ShortTermGainProbability = 0.7, Volatility = 0.05, NewsImpactScore = 0.8 },
                new Asset { Name = "ETH", ShortTermGainProbability = 0.65, Volatility = 0.07, NewsImpactScore = 0.6 }
            },
            "Stock" => new List<Asset>
            {
                new Asset { Name = "AAPL", ShortTermGainProbability = 0.6, Volatility = 0.04, NewsImpactScore = 0.75 },
                new Asset { Name = "TSLA", ShortTermGainProbability = 0.55, Volatility = 0.09, NewsImpactScore = 0.5 }
            },
            _ => new List<Asset>()
        };
    }
}

public class Asset
{
    public string Name { get; set; }
    public double ShortTermGainProbability { get; set; }
    public double Volatility { get; set; }
    public double NewsImpactScore { get; set; }
}