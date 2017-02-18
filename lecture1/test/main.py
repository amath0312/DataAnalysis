# -*- coding:utf8 -*-

"""
    作者:     amath321
    版本:     1.0
    日期:     2017/02/18
    项目名称：科技工作者心理健康数据分析 (Mental Health in Tech Survey)
"""

import csv
import numpy as np


def process(datafile, resultfile):
	"""
		main function: 
			read data from csv file, 
			calculate the result, 
			and write the result to a file in csv format
	"""
	result = process_data(datafile)
	save_result(result,resultfile)


def process_data(datafile):
	result = {}
	with open(datafile,mode='r', newline='') as csvfile:
		rows = csv.reader(csvfile)
		for i,row in enumerate(rows):
			if i == 0:
				continue

			country = row[3]
			age = row[1]
			if not country in result:
				result[country] = [] 

			if age.isnumeric():
				age = int(age)
				if age > 0:
					result[country].append(int(age))
			else:
				print(i, "country:",country,"age:",age)

	return result

def save_result(result, resultfile):
	with open(resultfile, mode='w',newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerow(['国家','年龄'])
		for country, ages in result.items():
			avgage = np.average(ages)
			csvwriter.writerow([country, avgage])

if __name__ == '__main__':
	datafile = './survey.csv'
	resultfile = './age_country.csv'
	process(datafile,resultfile)
