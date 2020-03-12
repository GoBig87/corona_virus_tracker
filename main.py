from web_scraping.world_meters_parser import WorldMetersParser
from data_analysis.data_analysis import DataAnalysis

if __name__ == "__main__":
    wmp = WorldMetersParser()
    da = DataAnalysis(wmp.country_dict)
    da.store_exp_curve_fit()
    da.plot_exp_curve_fit()
    pass
