
import datetime

import json
import os

def geef_zon_tijden():
    maanden =['jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec']
    with open(r'applicatie/bronnen/zon_tijden.json') as json_data:
        d = json.load(json_data)
        vandaag = datetime.datetime.today()
        dagnr_vandaag = vandaag.strftime("%d")
        maandnr_vandaag = vandaag.strftime("%m")
        vandaag_string = str(dagnr_vandaag) + '-' + maanden[int(maandnr_vandaag)-1]
        nr = 0
        unieke_jaren = []
        for rec in d['zon_tijden']:
            if rec['datum'] == vandaag_string:
                zonop = rec['zon_op']
                zononder = rec['zon_onder']
    return(zonop,zononder)

