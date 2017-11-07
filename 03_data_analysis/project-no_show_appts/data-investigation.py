# Initial investigations
df.info()
df.describe()
df['No-show'].value_counts()
df.query('AppointmentDay - ScheduledDay < 1')
sum(df.duplicated())

scheduled_date = datetime.strptime(df['ScheduledDay'][1], "%Y-%m-%dT%H:%M:%SZ")
scheduled_date = datetime.strptime(df['ScheduledDay'][10][:10], "%Y-%m-%d")
appointment_date = datetime.strptime(df['AppointmentDay'][10][:10], "%Y-%m-%d")
date_difference = appointment_date - scheduled_date
print("Scheduled Date: {}".format(scheduled_date))
print("Appointment Date: {}".format(appointment_date))
print("Time Between Dates: {}".format(date_difference))


#Research Question 1 Investigations
df.groupby('ApptResult').mean()

df1 = df.groupby('Neighbourhood')['ApptResult']
df1.describe().query('mean > .75')

#Research Question 3 Investigations
df.query('Hipertension == 1 or Handcap == 1')['ApptResult'].value_counts()
df.query('Hipertension == 1 and Handcap == 1')['ApptResult'].mean()
df.query('(Hipertension == 1) or (Diabetes == 1) or (Alcoholism == 1) or (Handcap == 1)')['ApptResult'].mean()
df.query('(Alcoholism == 1) and ((Hipertension == 1) or (Diabetes == 1) or (Handcap == 1))')['ApptResult'].mean()
df.query('(Hipertension == 1) and ((Alcoholism == 1) or (Diabetes == 1) or (Handcap == 1))')['ApptResult'].mean()
df.query('(Handcap == 1) and ~((Alcoholism == 1) or (Diabetes == 1) or (Hipertension == 1))')['ApptResult'].mean()
df.query('(Hipertension == 1) or (Diabetes == 1) (Alcoholism == 1) or (Handcap == 1)')['ApptResult'].mean()
df.query('ApptResult == 1').loc[:,'Hipertension':'Handcap'].mean()
df.loc[:,'Hipertension':'Handcap'].mean()

labels = ['Hipertension','Diabetes','Handcap']
x = range(1, len(labels)+1)
y = [hipertension_rate, diabetes_rate, hipertension_rate]
plt.figure(figsize=(12,4))
plt.bar(x,y);
plt.axhline(mean*100, label='Overall Mean Attendance (No Factors): {}%'.format(round(mean*100,1)), color='r', alpha=.5);
plt.xticks(x,labels);
plt.ylim(60,80);
plt.title('Attendance Rate by Health Condition')
plt.ylabel('Attendance Rate');
plt.legend();