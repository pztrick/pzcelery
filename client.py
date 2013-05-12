from tasks import make_pi
import time
import datetime

number_of_digits = 20


print "Client requesting pi digits calculated for significance of 1 to %i digits..." % number_of_digits

results = list(make_pi.delay(x) for x in range(1, number_of_digits))

while not all(result.ready() for result in results):
    time.sleep(2)
    finishers = filter(lambda x: x.ready(), results)
    #print "STATUS: %i/%i complete." % (len(finishers), len(results))
    for finisher in finishers:
        response = finisher.get()
        print "[%s] [Worker @ %s] pi: %s" % (datetime.datetime.now().strftime('%I:%M:%S%p'),
                                               response['hostname'],
                                               response['result'])
        results.remove(finisher)
