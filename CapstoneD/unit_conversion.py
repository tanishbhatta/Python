"""
Capstone 7: UNIT CONVERSION LIBRARY
A module containing many small, reusable functions.

"""

#DISTANCE
def kilometer_to_meter(km:float) -> float:
    """
    Converts Kilometer into Meter

    Argument:
        km: Distance measure in kilometers.
    
    Returns:
        Equivalent distance in meters.
    """
    m = km * 1000

    return m

def meter_to_kilometer(m:float) -> float:
    """
    Converts Meter into Kilometer

    Argument:
        m: Distance measure in meters.
    
    Returns:
        Equivalent distance in kilometers.
    """
    km = m / 1000

    return km

def kilometer_to_mile(km:float) -> float:
    """
    Converts Kilometer into Mile

    Argument:
        km: Distance measure in kilometers.
    
    Returns:
        Equivalent distance in Miles.
    """
    mil = km / 1.609

    return mil

def mile_to_kilometer(mil:float) -> float:
    """
    Converts Mile into Kilometers

    Argument:
        mil: Distance measure in miles.
    
    Returns:
        Equivalent distance in kilometers.
    """
    km = mil * 1.609

    return km

def meter_to_foot(m:float) -> float:
    """
    Converts Meter into Foot

    Argument:
        m: Distance measure in meters.
    
    Returns:
        Equivalent distance in feet.
    """
    ft = m * 3.281

    return ft

def foot_to_meter(ft:float) -> float:
    """
    Converts Foot into Meter

    Argument:
        ft: Distance measure in feet.
    
    Returns:
        Equivalent distance in meters.
    """
    m = ft / 3.281

    return m

def centimeter_to_inch(cm:float) -> float:
    """
    Converts Centimeter into Inch

    Argument:
        cm: Distance measure in centimeters.
    
    Returns:
        Equivalent distance in inches.
    """
    inc = cm / 2.54

    return inc

def inch_to_centimeter(inc:float) -> float:
    """
    Converts Meter into Centimeter

    Argument:
        inc: Distance measure in inches.
    
    Returns:
        Equivalent distance in centimeters.
    """
    cm = inc * 2.54

    return cm


#WEIGHT
def kilogram_to_gram(kg:float) -> float:
    """
    Converts Kilogram into Gram

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in grams.
    """
    g = kg * 1000

    return g

def gram_to_kilogram(g:float) -> float:
    """
    Converts Gram into Kilogram

    Argument:
        g: Mass measure in grams.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = g / 1000

    return kg

def kilogram_to_pound(kg:float) -> float:
    """
    Converts Kilogram into Pound

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in pounds.
    """
    lb = kg * 2.205

    return lb

def pound_to_kilogram(lb:float) -> float:
    """
    Converts Pound into Kilogram

    Argument:
        lb: Mass measure in pounds.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = lb / 2.205

    return kg

def gram_to_ounce(g:float) -> float:
    """
    Converts Gram into Ounce

    Argument:
        g: Mass measure in grams.
    
    Returns:
        Equivalent mass in ounces.
    """
    oz = g / 28.35

    return oz

def ounce_to_gram(oz:float) -> float:
    """
    Converts Ounce into Gram

    Argument:
        oz: Mass measure in ounces.
    
    Returns:
        Equivalent mass in grams.
    """
    g = oz * 28.35

    return g

def ton_to_kilogram(ton:float) -> float:
    """
    Converts Ton into Kilogram

    Argument:
        ton: Mass measure in tons.
    
    Returns:
        Equivalent mass in kilograms.
    """
    kg = ton * 907.2

    return kg

def kilogram_to_ton(kg:float) -> float:
    """
    Converts Kilogram into Ton

    Argument:
        kg: Mass measure in kilograms.
    
    Returns:
        Equivalent mass in tons.
    """
    ton = kg / 907.2

    return ton


#TEMPERATURE
def celsius_to_fahrenheit(c:float) -> float:
    """
    Converts Celsius into Fahrenheit

    Argument:
        c: Temperature measure in celsius.
    
    Returns:
        Equivalent temperature in fahrenheit.
    """
    f = (c * 1.8) + 32

    return f

def fahrenheit_to_celsius(f:float) -> float:
    """
    Converts Fahrenheit into Celsius

    Argument:
        f: Temperature measure in fahrenheit.
    
    Returns:
        Equivalent temperature in celsius.
    """
    c = (f - 32) / 1.8

    return c

def celsius_to_kelvin(c:float) -> float:
    """
    Converts Celsius into Kelvin

    Argument:
        c: Temperature measure in celsius.
    
    Returns:
        Equivalent temperature in kelvin.
    """
    k = c + 273.15

    return k

def kelvin_to_celsius(k:float) -> float:
    """
    Converts Kelvin into Celsius

    Argument:
        k: Temperature measure in kelvin.
    
    Returns:
        Equivalent temperature in celsius.

    Constraint:
        Input must be greater or equal to zero.
    """
    if k < 0:
        raise ValueError("Invalid token")
    else:
        c = k - 273.15

        return c

def kelvin_to_fahrenheit(k:float) -> float:
    """
    Converts Kelvin into Fahrenheit

    Argument:
        k: Temperature measure in kelvin.
    
    Returns:
        Equivalent temperature in fahrenheit.
    
    Constraint:
        Input must be greater or equal to zero.
    """
    if k < 0:
        raise ValueError("Invalid token")
    else:
        f = (k - 273.15) * 1.8 + 32

        return f

def fahrenheit_to_kelvin(f:float) -> float:
    """
    Converts Fahrenheit into Kelvin

    Argument:
        f: Temperature measure in fahrenheit.
    
    Returns:
        Equivalent temperature in kelvin.
    """
    k = (f - 32) / 1.8 + 273.15

    return k