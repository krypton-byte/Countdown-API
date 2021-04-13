from datetime import datetime
import json
import pytz
from flask import (
    Flask, request
)
from os import environ
from werkzeug.utils import redirect
app = Flask(__name__)


@app.route("/countdown")
def countdown():
    try:
        timenow = datetime.now(
            pytz.timezone(request.args.get("tz", "Asia/Jakarta"))
        )
        year = int(request.args.get("year", timenow.year))
        month = int(request.args.get("month", timenow.month))
        day = int(request.args.get("day", timenow.day))
        total = datetime(year, month, day).replace(
            tzinfo=pytz.timezone(
                request.args.get("tz", "Asia/Jakarta")
                )) - datetime.now(
                pytz.timezone(request.args.get("tz", "Asia/Jakarta"))
            )
        return app.response_class(
            response=json.dumps({
                "day": total.days,
                "minute": int(total.seconds % 3600 // 60),
                "hour": int(total.seconds // 3600),
                "second": int(total.seconds % 60)
            }, indent=4),
            mimetype="json/application",
            status=200
            )
    except pytz.exceptions.UnknownTimeZoneError:
        return {}
    except ValueError:
        return {}


@app.route("/tz")
def redir():
    return redirect(
        "https://raw.githubusercontent.com/dmfilipenko/"
        "timezones.json/master/timezones.json")


app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
