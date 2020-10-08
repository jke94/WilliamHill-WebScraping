'''

    AUTOR: Javier Carracedo
    Date: 08/10/2020 

    Auxiliar class to test methods from WilliamHillURLs.py

'''

import WilliamHillURLs as whUrls

if __name__ == "__main__":

    myVariable = whUrls.WilliamHillURLs()

    # Print all matches played actually.
    for item in myVariable.GetAllMatchsPlayedActually(myVariable.URL_FootballOnDirect):
        print(item)
    
    '''
        OUTPUT EXAMPLE at 08/10/2020 20:19:29:

        Islas Feroe Sub 21 v EspaÃ±a Sub 21: 90/1  | 15/2  | 1/40 
        Dornbirn v St Gallen: 90/1  | 15/2  | 1/40
        Corellano v PeÃ±a Azagresa: 90/1  | 15/2  | 1/40
        Esbjerg v Silkeborg: 90/1  | 15/2  | 1/40
        Koge Nord v Ishoj: 90/1  | 15/2  | 1/40
        Vasco da Gama Sub 20 v Bangu Sub 20: 90/1  | 15/2  | 1/40 
        Rangers de Talca v Dep. Valdivia: 90/1  | 15/2  | 1/40    
        San Marcos v Dep. Santa Cruz: 90/1  | 15/2  | 1/40        
        Melipilla v Puerto Montt: 90/1  | 15/2  | 1/40
        Kray v TuRU Dusseldorf: 90/1  | 15/2  | 1/40
        Siegen v Meinerzhagen: 90/1  | 15/2  | 1/40
        1. FC M'gladbach v Kleve: 90/1  | 15/2  | 1/40
        Waldgirmes v Turkgucu-Friedberg: 90/1  | 15/2  | 1/40     
        Zamalek v Wadi Degla: 90/1  | 15/2  | 1/40
        Elva v Flora B: 90/1  | 15/2  | 1/40
        Fujairah FC v Ajman: 90/1  | 15/2  | 1/40
        Vanersborg v Ahlafors: 90/1  | 15/2  | 1/40
    '''

    # Print all URL mathes played actually.
    for item in myVariable.GetAllUrlMatches(myVariable.URL_FootballOnDirect):
        print(item)

    '''
        OUTPUT EXAMPLE at 08/10/2020 20:19:29:

        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701125/islas-feroe-sub-21-â-espaÃ±a-sub-21
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701988/dornbirn-â-st-gallen
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18702077/corellano-â-peÃ±a-azagresa
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694620/esbjerg-â-silkeborg
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18702062/koge-nord-â-ishoj
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701883/vasco-da-gama-sub-20-â-bangu-sub-20
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694610/rangers-de-talca-â-dep-valdivia
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694611/san-marcos-â-dep-santa-cruz
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694612/melipilla-â-puerto-montt
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694624/kray-â-turu-dusseldorf
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694625/siegen-â-meinerzhagen
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694626/1-fc-mgladbach-â-kleve
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694627/waldgirmes-â-turkgucu-friedberg
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18694162/zamalek-â-wadi-degla
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701762/elva-â-flora-b
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701661/fujairah-fc-â-ajman
        https://sports.williamhill.es/betting/es-es/fÃºtbol/OB_EV18701852/vanersborg-â-ahlafors

    '''
