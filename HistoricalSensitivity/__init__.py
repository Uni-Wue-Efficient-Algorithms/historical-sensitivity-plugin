# -*- coding: utf-8 -*-
# ---------------------------------------------------------
#    __init__ - HistoricalSensitivity init file
#
#    author               : Benedikt Budig
#    email                : benedikt.budig@uni-wuerzburg.de
# ---------------------------------------------------------

def classFactory(iface): 
    from HistoricalSensitivity import HistoricalSensitivity 
    return HistoricalSensitivity(iface)

