import requests
import json

resp = requests.get('https://csv.webfleet.com/extern?lang=en&account=electric-T52&username=ndomx&password=243221Hugo'
                    '&apikey=ef23d721-3c65-4713-b3f9-f51d60ac8048&'
                    'action=geocodeAddress&outputformat=json&use=UTF8=true&freetext=Rancagua')
resp2 = requests.get('https://csv.webfleet.com/extern?account=electric-T52&username=ndomx&password=243221Hugo&'
                     'apikey=ef23d721-3c65-4713-b3f9-f51d60ac8048&&lang=de'
                     '&action=showObjectReportExtern&filterstring=003')

resp3 = requests.get('https://csv.webfleet.com/extern?lang=en&account=electric-T52&username=ndomx&password=243221Hugo'
                     '&apikey=ef23d721-3c65-4713-b3f9-f51d60ac8048&&lang=de&action=getObjectCanSignals&objectno=001')


if resp:
    print(resp3.text)
    print("............")

    # print(resp.json())
    # print('headers')
    # print(resp.headers)
    # print('text')
    # print(resp.text)

else:
    print("Error")
