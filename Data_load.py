from connection import hiveConnection

def Load_data(filename,tablename):
    try:
        c = hiveConnection()
        hql = f'''load data local inpath 
        "/home/pranav/PycharmProjects/Bigdata92/hive_project/data/{filename}" 
        overwrite into table {tablename}'''
        c.execute(hql)
        print(f'{filename} Loaded successfully into {tablename}..')

    except Exception as e:
        print(f"Error in Data loading of table:{tablename}",e)


