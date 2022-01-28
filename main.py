import logging
from datetime import datetime, timedelta
import boto3

log = logging.getLogger()
log.setLevel(logging.INFO)


def lambda_handler(Event, Context):
    time_period = get_timeperiod()

    query = {
            "And": [
                {
                        "Dimensions": {
                            "Key": "RECORD_TYPE",
                            "Values": [
                                "Reservation applied usage",
                                "Savings Plan Covered Usage",
                                "Usage"
                            ]
                        }
                },
                {
                        "Dimensions": {
                            "Key": "USAGE_TYPE_GROUP",
                            "Values": [
                                "EC2: Running Hours"
                            ]
                        }
                }
            ]
        }

    ce_total_spend = get_cost_explorer(time_period, query, "UnblendedCost")
    ce_total_usage = get_cost_explorer(time_period, query, "UsageQuantity")
    Unit_cost = ce_total_spend/ce_total_usage
    print(Unit_cost)
    

def get_timeperiod():
    """
    Calculates timeperiod for cost explorer API call

    Returns:

    time_period : dict
        A dictionary containing the start and end for CE API call - yyyy-mm-dd
    """
    end_date = datetime.today().replace(day=1)  # 1st day of current month
    start_date = (end_date - timedelta(days=1)
                  ).replace(day=1)  # 1st day of last month
    time_period = {
        "Start": start_date.strftime("%Y-%m-%d"),
        "End": end_date.strftime("%Y-%m-%d"),
    }
    log.info(f"Checking validity of {start_date.strftime('%B %Y')}")
    return time_period


def get_cost_explorer(time_period, boto3_filter, metric):
    client = boto3.client("ce")

    response = client.get_cost_and_usage(
        TimePeriod=time_period,
        Granularity="MONTHLY",
        Filter=boto3_filter,
        Metrics=[f"{metric}", ],
    )
    expenditure = float(
        response.get("ResultsByTime")[0].get(
            "Total").get(f"{metric}").get("Amount")
    )
    return expenditure


lambda_handler(None, None)