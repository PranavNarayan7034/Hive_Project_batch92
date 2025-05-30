# Top 10 products which most sales in quantity wise
# >>> select sales.productid,productname,quantity from products join sales on
#     products.productid = sales.productid limit 10;
# >>> select productname,sum(quantity)as Total_sales_qty from
#     products join sales on products.productid = sales.productid
#     group by productname limit 10;
# >>> select productname,sum(quantity)as Total_sales_qty from
#     products join sales on products.productid = sales.productid
#     group by productname order by Total_sales_qty desc limit 10;

from hive_project.connection import hiveConnection
def Most_sales():
    try:
        c = hiveConnection()
        hql = f'''select productname,sum(quantity)as Total_sales_qty from
            products join sales on products.productid = sales.productid
            group by productname order by Total_sales_qty desc limit 10'''
        c.execute(hql)
        Result_table = c.fetchall()
        return Result_table
    except Exception as e:
        print('Errro in Most Sales query (Analytics1) : ',e)