import matplotlib.dates
import numpy as np

def polyfit(dates, levels, p):
    # Create list of time and list of level
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Shift in date-time axis
    d0 = x[0]

    # Find coefficient of best-fit polynomials
    p_coeff = np.polyfit(x - d0, y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    # Return info
    return poly, d0