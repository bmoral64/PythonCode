# Script that takes an amazon .csv file and prints different statistics
# about purchase history. Amazon purchase history can be retrieved from https://www.amazon.com/b2b/reports
# or use the sample file included in the repository
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

ROOT = tk.Tk()
ROOT.withdraw()
fileToAnalyze = askopenfilename()

data = pd.read_csv(fileToAnalyze)
data = data.fillna(0)
print(data['Item Total'])
data['Item Total'] = data['Item Total'].str.replace('$','', regex = True).astype(float)
print('Total: ' + str(data['Item Total'].sum()))
print('Average: ' + str(data['Item Total'].mean()))
print('Median: ' + str(data['Item Total'].median()))
print('Max: ' + str(data['Item Total'].max()))
print('Min: ' + str(data['Item Total'].min()))