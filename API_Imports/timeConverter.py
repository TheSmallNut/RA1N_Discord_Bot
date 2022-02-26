from distutils.log import ERROR
from dateutil import parser
from dateutil.tz import gettz
import time

def convertStringToDatetime(string):
    tzinfo = {"CST": gettz("America/Chicago"),
                  "CT": gettz("America/Chicago"),
                  "PT": gettz("America/Los_Angeles"),
                  "PST": gettz("America/Los_Angeles"),
                  "ET": gettz("Canada/Eastern"),
                  "EST": gettz("Canada/Eastern"),
                  "UTC": gettz("ETC/UTC")
                  }
    try:
        date = parser.parse(string, fuzzy=True, tzinfos = tzinfo)
        return date
    except(parser.ParserError):
        return None

def datetimeToUnix(datetimeObject):
    unixtime = int(time.mktime(datetimeObject.timetuple()))
    return unixtime



if __name__ == "__main__":
    datetimeVariable = convertStringToDatetime("Sunday 1pm PT")
    print(datetimeToUnix(datetimeVariable))