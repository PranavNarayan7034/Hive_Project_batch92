from connection import hiveConnection

def create_table(tablename,columninfo):
    try:
        c = hiveConnection()
        t = f'''
        create table if not exists {tablename}({columninfo}) 
        row format delimited fields terminated by "," 
        tblproperties("skip.header.line.count"="1")'''
        c.execute(t)

        print(f'{tablename} Table Created Successfully..')

    except Exception as e:
        print(f'Error in Table: {tablename} Creation',e)

