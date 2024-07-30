
from openpyxl import Workbook
import requests
data=[]
for x in range(10000001,10000100):
    scraping_url="https://dantri.com.vn/thpt/1/0/99/" +  str(x) + "/2024/0.2/search-gradle.htm"
    payload={}
    headers={}
    response=requests.request("GET",scraping_url,headers=headers,data=payload)
    info = response.json()['student']
    diem = "SBD {} Toan {} Van {} Anh {} Ly {} Hoa {} Sinh {} DiemTBTuNhien {} Lich Su {} Dia Ly {} GDCD {} DiemTBXaHoi {}".format(
        info['sbd'],info['toan'],info['van'],info['ngoaiNgu'],info['vatLy'],info['hoaHoc'],info['sinhHoc'],info['diemTBTuNhien'],info['lichSu'],info['diaLy'],info['gdcd'],info['diemTBXaHoi'],
        )
    diemthi=str(diem)
    print(diem)
    data.append(diemthi)

wb = Workbook()
ws = wb.active
ws.title = "Student Data"



for item in data:
    values = item.split(" ")
    ws.append(values)


wb.save("student_data.xlsx")