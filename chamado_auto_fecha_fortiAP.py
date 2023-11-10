
import pyodbc  
conn = pyodbc.connect('Driver={SQL Server};'  
                         'Server=CosmosDW;'  
                         'Database=ICD760P;'  
                         'UID=maximo;'  
                          'PWD=payless1520;'  
                          'MARS_Connection=Yes;')  
#filial = "%1"
filial = 'EMP503_FortiAP'
filial = filial.translate({ord(i):None for i in '[]""(),'})
filial = filial.split('_',1)[0]
#sensor = %2
sensor = 'TESTE'
sensor = sensor.translate({ord(i):None for i in '[]""(),'})  
ticked = ''  
procedure1 = "exec proc_cheque_result_fortiAP "  
procedure2 = "exec proc_fecha_chamado "
querycheque = procedure1 + "'" +filial + "' " + ", " + "'" + sensor + "'"  
cursor = conn.cursor()  
cursor.execute(querycheque)
for row in cursor:  
    ticked = row  
ticked2 = str(ticked)  
ticked3 = ticked2.translate({ord(i):None for i in "[]''(),"})  
update = procedure2 + ticked3
if len(ticked) == 0:  
    1+1  
else:  
    cursor.execute(update)  
    conn.commit()
    


