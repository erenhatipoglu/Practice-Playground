# How many seconds have you been wandering the Earth?

from datetime import datetime as dt

try:
    birth_date = input("Your date of birth (YYYY-MM-DD): ")
    if not birth_date:
        raise ValueError("Error: Empty input. Enter a date.")
    else:
        birth_date = dt.strptime(birth_date, "%Y-%m-%d")

except ValueError:
    print("Invalid date format.\nCorrect it and don't forget the dashes between.")

else:
    now = dt.now()
    timespan = now - birth_date

    secs_alive = timespan.total_seconds()
    secs_alive_round = round(secs_alive)

    print(f"You have been alive approximately {secs_alive_round} seconds.")