
import datetime
import logging
import azure.functions as func



def main(myTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()


    print(f"Hello, World! function ran at {utc_timestamp}")