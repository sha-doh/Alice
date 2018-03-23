from utils import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from financial_functions import *
from agent import *
from genetics import *
from time import time


def main():
	candle_period = "1H"
	ma_maximum_period = 100
	population_amt = 50 #Change cross over, 2 steps
	generations = 10
	survival_rate = 0.3
	mutation_factor = 0.09 #Mutation factor should be unique to the individual, 
	#offspring inherit mutation factor either randomly or a convolved version of daddy and mommy

	traders, average_fitness, best_fitness = train(candle_period, ma_maximum_period, population_amt, generations, survival_rate, mutation_factor)

	
	show_metrics(traders, average_fitness, best_fitness)


	#Validate results
	validate(traders, candle_period, ma_maximum_period)
	show_metrics_valid(traders)
main()