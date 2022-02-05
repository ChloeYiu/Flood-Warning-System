import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from .analysis import *

def plot_water_levels(station, dates, levels):
	'''Plots the provided data using matplotlib, alongside lines indicating the typical range for the station'''
	# Plot
	plt.plot(dates, levels)
	low_line = [station.typical_range[0]]*len(levels)
	high_line = [station.typical_range[1]]*len(levels)
	plt.plot(dates, low_line)
	plt.plot(dates, high_line)
	# Add axis labels, rotate date labels and add plot title
	plt.xlabel('date')
	plt.ylabel('water level (m)')
	plt.xticks(rotation=45)
	plt.title(station.name)

	# Display plot
	plt.tight_layout()  # This makes sure plot does not cut off date labels

	plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
	'''Plots the provided data using matplotlib, alongside lines indicating the best-fit polynomial details for the station'''
	# Create list of time and list of level
	x = matplotlib.dates.date2num(dates)
	y = levels

	# Retrieve best-fit polynomial details
	poly, d0 = polyfit(dates, levels, p) 

	# Plot
	plt.plot(dates, y, '.')
	plt.plot(dates, poly(x - d0))
	plt.xlabel('date')
	plt.ylabel('water level')
	plt.xticks(rotation=45)
	plt.title(station.name)

	# Display plot
	plt.tight_layout()  # This makes sure plot does not cut off date labels
	plt.show()