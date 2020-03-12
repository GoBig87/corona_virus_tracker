from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

import numpy


class DataAnalysis(object):
    '''
    Data Analysis Tool for Analyzer Data from WorldoMeter
    '''
    def __init__(self, world_meters_dict):
        self.world_meters_dict = world_meters_dict

    # Use this if you need to update your data
    def update_data(self, world_meters_dict):
        self.world_meters_dict = world_meters_dict

    def store_exp_curve_fit(self, p0_tupple=(0, 0.1)):
        for country in self.world_meters_dict:
            print(country)
            dict = self.world_meters_dict[country]
            x_range = range(len(dict['coronavirus-cases-linear']))
            y_range = dict['coronavirus-cases-linear']
            exp_curve = curve_fit(lambda t, a, b: a * numpy.exp(b * t), x_range, y_range, p0=p0_tupple)
            self.world_meters_dict[country]['exp_curve_fit'] = exp_curve[0]
        pass

    def plot_exp_curve_fit(self):
        for country in self.world_meters_dict:
            dict = self.world_meters_dict[country]
            x_range = range(45)
            a = dict['exp_curve_fit'][0]
            b = dict['exp_curve_fit'][1]
            y = a * numpy.exp(b * x_range)
            plt.plot(x_range, y)
            plt.title(country)
            plt.ylabel('coronavirus-cases-linear')
            plt.show()
            pass
