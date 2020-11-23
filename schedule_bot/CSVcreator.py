import pandas as pd


df = pd.DataFrame(data=[['Data analysis', 'Monday', '18:15', '21:30'],
                        ['AI', 'Tuesday', '18:15', '21:30'],
                        ['Unity', 'Wednesday', '9:00', '12:15'],
                        ['English', 'Wednesday', '18:15', '21:30'],
                        ['Software engineering', 'Thursday', '18:15', '21:30'],
                        ['Project Monitoring', 'Friday', '16:00', '18:00'],
                        ['Agile', 'Saturday', '9:00', '12:15'],
                        ['Python', 'Saturday', '12:30', '15:30']],
                  columns=['Subject', 'Weekday', 'TimeStart', 'TimeEnd'])
df.to_csv('schedule.csv', index=False)
