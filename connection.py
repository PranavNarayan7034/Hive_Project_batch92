from pyhive import hive

def hiveConnection():
    try:
        cursor = hive.connect(host="localhost",
                              database="groceries").cursor()
        # print("Connected to Hive Successfully...")
        return cursor

    except Exception:
        print("Error in Hive Connection")