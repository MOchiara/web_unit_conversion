from pyudunits2 import UnitSystem, Converter
import numpy as np

# Coversion
def run_conversion(input_unit, output_unit, val):
    ut_system = UnitSystem.from_udunits2_xml()
    in_u= ut_system.unit(input_unit)
    out_u = ut_system.unit(output_unit)
    converter = Converter(in_u, out_u)
    expression = converter.expression
    
    output_val = converter.convert(float(val))
    return output_val, expression

