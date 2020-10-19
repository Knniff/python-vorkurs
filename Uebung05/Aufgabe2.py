import argparse
import time
import datetime
import dateutil
import calendar

parser = argparse.ArgumentParser(description="Calculate the time since your birth")
parser.add_argument("birth_date", help="The date of your birth in ISO-format")
parser.add_argument(
    "-f",
    "--format",
    default="Tagen",
    help="Wollen sie die vergangene Zeit in Sekunden, Stunden, Tagen oder Wochen zurückhaben?",
)
args = parser.parse_args()


now = datetime.datetime.today()
birth = datetime.datetime.fromisoformat(args.birth_date)
delta = now - birth
switcher = {
    "Sekunden": delta.days * 24 * 60 * 60,
    "Stunden": delta.days * 24,
    "Tagen": delta.days * 1,
    "Wochen": delta.days / 7,
}
print(round(switcher[args.format]))
