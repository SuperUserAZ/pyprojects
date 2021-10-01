import speedtest

s = speedtest.Speedtest()
send_d = s.download()
send_up = s.upload()
send_d, send_up = int(send_d), int(send_up)
result_d = send_d /1000_000  #1 мегабайт = 1000 000 байтов поэтому делим 
result_up = send_up /1000_000
print(f"{result_d:.2f} Mb/ps")  #округляем результат загрузки
print(f"{result_up:.2f} Mb/ps") #результат отправки данных
