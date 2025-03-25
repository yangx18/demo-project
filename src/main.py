import datetime
from dateutil.relativedelta import relativedelta

def get_future_date(months_ahead=1):
    """Calculate a date in the future."""
    current_date = datetime.datetime.now()
    future_date = current_date + relativedelta(months=months_ahead)
    return future_date

def main():
    print("Welcome to the Demo Project!")
    print(f"Current time: {datetime.datetime.now()}")
    print(f"One month from now: {get_future_date(1)}")

if __name__ == "__main__":
    main()