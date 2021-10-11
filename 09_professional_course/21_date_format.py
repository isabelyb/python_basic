from datetime import datetime

my_local_time = datetime.now()

print('Local time: ', my_local_time)


latam = my_local_time.strftime('%d/%m/%Y')
print('Formato LATAM:', latam)

usa = my_local_time.strftime('%m/%d/%Y')
print('Formato USA:', usa)

random_format = my_local_time.strftime('año %Y mes %m día %d')
print('Formato random:', random_format)

formato_utc = my_local_time.utcnow()
print('Formato UTC:',formato_utc)