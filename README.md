# ce_compute_unit_cost
Python script to get last months compute unit cost from your cost explorer

```python3 main.py```

Unit_cost = spend/usage


In CE https://console.aws.amazon.com/cost-management/home?#/custom?groupBy=None&forecastTimeRangeOption=None&hasBlended=false&excludeTaggedResources=false&chartStyle=Group&timeRangeOption=Last6Months&granularity=Monthly&reportName=Monthly%20costs%20by%20service&isTemplate=true&reportType=CostUsage&hasAmortized=false&excludeDiscounts=true&usageAs=usageQuantity&excludeCategorizedResources=false&excludeForecast=false&startDate=2021-07-01&endDate=2021-12-31&filter=%5B%7B%22dimension%22:%22UsageTypeGroup%22,%22values%22:%5B%7B%22value%22:%22EC2:%20Running%20Hours%22,%22unit%22:%22Hrs%22%7D%5D,%22include%22:true,%22children%22:null%7D,%7B%22dimension%22:%22RecordType%22,%22values%22:%5B%22DiscountedUsage%22,%22SavingsPlanCoveredUsage%22,%22Usage%22%5D,%22include%22:true,%22children%22:null%7D%5D