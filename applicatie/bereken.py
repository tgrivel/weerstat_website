import json
from datetime import datetime
from collections import namedtuple
from calendar import monthrange

dagen_per_maand = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def geef_data_per_maand(huidige_maand, data_def):
    with open(r'bronnen/weer_alle_dagen.json') as json_data:
        d = json.load(json_data)
        nr = 0
        unieke_jaren = []
        for rec in d['alle_dagen']:
            nr += 1
            maand = str(rec['datum'][5:7])
            jaar = str(rec['datum'][0:4])
            if jaar not in unieke_jaren:
                unieke_jaren.append(jaar)
            # print(nr, rec['datum'], maand, jaar, rec['maximale_temp'])

        dagen  = []
        data = {}
        for dag in range(1, dagen_per_maand[huidige_maand-1] + 1):
            dagen.append(str(dag))
        data = {'Dag': dagen}
        # print(data)
        for jr in unieke_jaren:
            temps = []
            for i in range(1, dagen_per_maand[huidige_maand-1] + 1):
                temps.append(0.01)
            for rec in d['alle_dagen']:
                maand = int(rec['datum'][5:7])
                jaar = str(rec['datum'][0:4])
                # dagnr = int(rec['datum'][8:10])
                # print(rec['datum'], jaar, maand, dagnr)
                if maand == huidige_maand and jr == jaar:
                    dagnr = int(rec['datum'][8:10])
                    # print(jaar, maand, dagnr, rec[data_def])
                    temps[dagnr-1] = float(rec[data_def])
            # for recordje in range(len(temps)):
            #     if recordje > 1:
            #         if temps[recordje] == 0.001:
            #             temps[recordje] = temps[recordje-1]
            data[jr] = temps
    # print(data)
    return data
