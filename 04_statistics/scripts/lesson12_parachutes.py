import numpy as np
import pandas as pd

par_data = pd.read_csv('parachute_dataset.csv')

total_parachutes = par_data.count()[0]
errors = par_data.query('actual != predicted').count()[0] / total_parachutes
errors

#Type 1 error
par_pred_fail_but_open = par_data[par_data['predicted'] == 'fails'][par_data['actual'] == 'open']
par_type2_error = par_pred_fail_but_open.count()[0] / total_parachutes
par_type2_error

#Type 2 Error
par_pred_open_but_fail = par_data[par_data['predicted'] == 'opens'][par_data['actual'] == 'fails']
par_type1_error = par_pred_open_but_fail.count()[0] / total_parachutes
par_type1_error