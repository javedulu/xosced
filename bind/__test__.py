import sys
sys.path.append('.')
import pyxosc
from pyxosc import xosc
osc = xosc()
osc.load("/Users/javedshaik/ws/pyosc_p/build/pybind/ACC_1_speed_regulation.xosc")
osc.parse()

def get_children(osc_o):
    if str(type(osc_o)).find("e_")!=-1 : return
    if (str(type(osc_o)).find('pyxosc.UnsignedInt')!=-1):
        print ("\t --",osc_o,type(osc_o),osc_o.m_unsignedInt);return
    elif (str(type(osc_o)).find('pyxosc.Int')!=-1):
        print ("\t --",osc_o,type(osc_o),osc_o.UnsignedInt);return
    elif (str(type(osc_o)).find('pyxosc.String')!=-1):
        print ("\t --",osc_o,type(osc_o),osc_o.m_string);return
    elif (str(type(osc_o)).find('pyxosc.Double')!=-1):
        print ("\t --",osc_o,type(osc_o),osc_o.m_double);return
    elif (str(type(osc_o)).find('pyxosc.Boolean')!=-1):
        print ("\t --",osc_o,type(osc_o),osc_o.m_boolean);return
    else:
        print (osc_o)
    for o in dir(osc_o):
        if (str(o).find('__')!=-1):continue
        val = getattr(osc_o,o)
        if type(val) in [type(1),type(0.0),type('')]: continue
        if type(val) in [type([])]: 
            for val_c in val: get_children(val_c)
        elif (val) : get_children(val)

get_children(osc.OpenSCENARIO)