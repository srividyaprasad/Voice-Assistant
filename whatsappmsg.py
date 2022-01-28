import pywhatkit
import datetime
now = datetime.datetime.now()
hr=now.hour
mi=now.minute
def main(msg):

    pywhatkit.sendwhatmsg('+8951951105', msg, hr, mi)