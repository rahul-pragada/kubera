# class Program
# {
#     static async Task Main(string[] args)
#     {
#         var marketAgent = new MarketSelectionAgent();
#         var selectedMarket = marketAgent.SelectMarket();

#         if (selectedMarket == "Out")
#         {
#             Console.WriteLine("Staying out of all markets.");
#             return;
#         }

#         var assetAgent = new AssetPredictionAgent();
#         var selectedAsset = assetAgent.PredictAsset(selectedMarket);

#         var entryAgent = new EntryTimingAgent();
#         if (entryAgent.ShouldEnterAsset(selectedAsset))
#         {
#             var monitoringAgent = new MonitoringAgent();
#             monitoringAgent.Monitor(selectedAsset);

#             var decisionAgent = new DecisionAgent();
#             var currentPrice = await new CoinbaseAPI().GetCryptoPrice(selectedAsset);
#             var decision = decisionAgent.MakeDecision(currentPrice, 100); // Assuming 100 as buy price

#             Console.WriteLine($"Decision for {selectedAsset}: {decision}");
#         }
#         else
#         {
#             Console.WriteLine("Not a good time to enter the market.");
#         }
#     }
# }