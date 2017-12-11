import numpy as np
import pandas as pd

jud_data = pd.read_csv('judicial_dataset_predictions.csv')
jud_data.head()

#Data Setup
wrong_verdicts = jud_data.query('actual != predicted').count()[0]
total_verdicts = jud_data.count()[0]
wrong_verdicts/total_verdicts

#Type 1 Errors
jud_pred_guilty = jud_data[jud_data['predicted'] == 'guilty']
jud_pred_guilty_but_innocent = jud_pred_guilty[jud_pred_guilty['actual'] == 'innocent']
jud_type1_error = jud_pred_guilty_innocent.count()[0] / total_verdicts
jud_type1_error

#Type 2 Errors
jud_pred_innocent = jud_data[jud_data['predicted'] == 'innocent']
jud_pred_innocent_but_guilty = jud_pred_innocent[jud_pred_innocent['actual'] == 'guilty']
jud_type2_error = jud_pred_innocent_but_guilty.count()[0] / total_verdicts
jud_type2_error

jud_data[jud_data['actual'] == 'innocent'].count()[0] / total_verdicts
