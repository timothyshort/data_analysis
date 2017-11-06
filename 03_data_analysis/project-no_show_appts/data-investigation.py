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