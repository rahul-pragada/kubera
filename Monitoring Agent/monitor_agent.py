public class MonitoringAgent
{
    public void Monitor(string asset)
    {
        while (true)
        {
            double currentPrice = GetCurrentPrice(asset);
            Console.WriteLine($"Current price of {asset}: {currentPrice}");
            Thread.Sleep(60000); // Monitor price every minute
        }
    }

    private double GetCurrentPrice(string asset)
    {
        // Fetch real-time price using Coinbase API
        return new CoinbaseAPI().GetCryptoPrice(asset).Result;
    }
}

public class DecisionAgent
{
    public string MakeDecision(double currentPrice, double buyPrice)
    {
        // Decision logic based on current price vs. buy price
        if (currentPrice > buyPrice * 1.05) return "Sell"; // Sell if 5% gain
        else if (currentPrice < buyPrice * 0.95) return "Hold"; // Hold if losing
        else return "Buy"; // Otherwise, consider adding more
    }
}

public class CoinbaseAPI
{
    private static readonly HttpClient client = new HttpClient();

    public async Task<double> GetCryptoPrice(string asset)
    {
        var response = await client.GetAsync($"https://api.coinbase.com/v2/prices/{asset}-USD/spot");
        var json = await response.Content.ReadAsStringAsync();
        return ParsePrice(json);
    }

    private double ParsePrice(string json)
    {
        // Parse JSON response to extract the price
        var jsonObject = JObject.Parse(json);
        return double.Parse(jsonObject["data"]["amount"].ToString());
    }
}