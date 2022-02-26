# This is to test random stuff
from dateutil import parser
from dateutil.tz import gettz
import time

tzinfo = {"CST": gettz("America/Chicago"),
                  "CT": gettz("America/Chicago"),
                  "PT": gettz("America/Los_Angeles"),
                  "PST": gettz("America/Los_Angeles"),
                  "ET": gettz("Canada/Eastern"),
                  "EST": gettz("Canada/Eastern"),
                  "UTC": gettz("ETC/UTC")
                  }


date = parser.parse("nyjhwrtbnhjkgbnrhjkegbnhjkfd", fuzzy=True, tzinfos = tzinfo)


unixtime = time.mktime(date.timetuple())



print(unixtime)