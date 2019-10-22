import xlsxwriter
import mysql.connector
from pandas import DataFrame



def recordAudio():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="P@ssword_001",
          database="test"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM auth_permission")

        myresult = mycursor.fetchall()
        #newre	=	[]
        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet("Chart Data")
        #bar_chart = workbook.add_chart({'type': 'column'})

        """bar_chart.add_series({
            'name': 'Max Speed',
            'values': '=Chart Data!${0}${1}:${0}${2}'
            .format(chr(ord('A') + 0 + 1), 1, 1),
            'categories': '=Chart Data!${0}${1}:${0}${2}'
            .format(chr(ord('A') + 10), 1, 10),
            'data_labels': {'value': True, 'num_format': u'#0 "km/h"'}
        })"""

        #worksheet = workbook.add_worksheet('sec')
        title = workbook.add_format({
            'bold': True,
            'font_size': 14,
            'align': 'center',
            'valign': 'vcenter'
        })
        header = workbook.add_format({
            'bg_color': '#F7F7F7',
            'color': 'black',
            'align': 'center',
            'valign': 'top',
            'border': 1
        })

        worksheet.merge_range('B2:H2', "Test Data")
        
        col = 3
        row = 3
        
        for item in myresult:
        	#print(item[0:4])
        	worksheet.write("B"+str(row)+"B:"+str(row), item[0])
        	worksheet.write("C"+str(row)+"C:"+str(row), item[1])
        	worksheet.write("D"+str(row)+"D:"+str(row), item[2])
        	worksheet.write("E"+str(row)+"E:"+str(row), item[3])
        	row += 1

        workbook.close()



        """Cars  = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],'Price': [32000,35000,37000,45000]}
        df = DataFrame(Cars, columns= ['Brand', 'Price'])
        export_excel = df.to_excel (r'D:\voicepython\hello.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

        print (df)  """

if __name__ == '__main__':
    recordAudio()