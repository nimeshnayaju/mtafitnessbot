### About
I made this simple python script because I didn't want to manually send an email to Mount A Fitness Center everyday to book a gym slot. I use this script with `hickory` to automatically send an email to Fitness Center everyday to book a slot for the following day.

### How to run

If you wish to run this locally, make sure you have `python-dotenv` installed and an `.env` file (on the same directory level as `main.py`). Make sure you've the following fields correctly populated inside your `.env` file.

```sh
SENDER=XXXXXXXXXXXX
PASSWORD=XXXXXXXXXXXX
RECIPIENT=XXXXXXXXXXXX
SUBJECT="<SUBJECT OF THE EMAIL>"
NAME="<NAME>"
SUNDAY="<SLOT TIME (e.g. 1 pm)>"
MONDAY="<SLOT TIME>"
TUESDAY="<SLOT TIME>"
WEDNESDAY="<SLOT TIME>"
THURSDAY="<SLOT TIME>"
FRIDAY="<SLOT TIME>"
SATURDAY="<SLOT TIME>"
```

You can also pair this script with `hickory <https://github.com/maxhumber/hickory>`_, a command line tool to schedule Python scripts. After you've installed `hickory`, you can run the following command to schedule the email everyday.

````sh
hickory schedule main.py --every=day@10am
````

To view all status of all hickory schedules:

```sh
hickory status
```

To cancel the execution of the script, you can run the following command:

```sh
hickory kill main.py
````