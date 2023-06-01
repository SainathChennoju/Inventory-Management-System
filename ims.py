import pyodbc
from flask import Flask,jsonify,request,render_template
app=Flask(__name__)

server='SAINATH\SQLEXPRESS'
database='IMS2'
driver='{SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

connect = pyodbc.connect(connection_string)

cn=connect.cursor()

# customer_name='rtf'
# customer_addr='hyd'
# customer_email='rtf@gmail.com'

# cn.execute('select * from customer')
# print(cn.fetchall())
# cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customer_name}','{customer_addr}','{customer_email}')")
# connect.commit()
# #f is used to combine string and variable, used before string name


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/show-customers")
def customer_show():
    cn=connect.cursor()
    cn.execute('select * from customer')
    data=[]
    for i in cn.fetchall():
        customer={}
        customer['customer_id']=i[0]
        customer['customer_name']=i[1]
        customer['customer_addr']=i[2]
        customer['customer_email']=i[3]
        data.append(customer)
    print(data)
    return render_template('showcustomers.html',data=data)

@app.route("/show-product")
def product_show():
    cn=connect.cursor()
    cn.execute('select * from product')
    data=[]
    for i in cn.fetchall():
        product={}
        product['product_id']=i[0]
        product['product_name']=i[1]
        product['product_stock']=i[2]
        product['product_price']=i[3]
        product['product_supplier']=i[4]

        data.append(product)
    print(data)
    return render_template('showproduct.html',data=data)

@app.route("/show-orders")
def order_show():
    cn=connect.cursor()
    cn.execute('select * from orders')
    data=[]
    for i in cn.fetchall():
        orders={}
        orders['order_id']=i[0]
        orders['product_ID']=i[1]
        orders['customer_id']=i[2]
        orders['quantity']=i[3]

        data.append(orders)
    print(data)
    return render_template('showorders.html',data=data)

@app.route("/show-suppliers")
def supplier_show():
    cn=connect.cursor()
    cn.execute('select * from supplier')
    data=[]
    for i in cn.fetchall():
        suppliers={}
        suppliers['supplier_id']=i[0]
        suppliers['supplier_name']=i[1]
        suppliers['supplier_addr']=i[2]
        suppliers['supplier_email']=i[3]

        data.append(suppliers)
    print(data)
    return render_template('showsuppliers.html',data=data)


@app.route("/add-customer",methods=['GET','POST'])
def addcustomer():
    if request.method=='POST':
        cn=connect.cursor()
        customername=request.form.get('name')
        customeraddr=request.form.get('addr')
        customeremail=request.form.get('email')
        cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customername}','{customeraddr}','{customeremail}')")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addcustomer.html')
    
@app.route("/update-customer",methods=['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        cn=connect.cursor()
        customerid=request.form.get('customer_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatecustomer.html')

@app.route("/add-product",methods=['GET','POST'])
def addproduct():
    if request.method=='POST':
        cn=connect.cursor()
        productname=request.form.get('productname')
        productstock=request.form.get('stock')
        productprice=request.form.get('price')
        productsupplierid=request.form.get('supplierid')
        cn.execute(f"insert into product(product_name,stock,price,supplier_id) values('{productname}','{productstock}','{productprice}','{productsupplierid}')")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addproduct.html')
    
@app.route("/add-orders",methods=['GET','POST'])
def addorder():
    if request.method=='POST':
        cn=connect.cursor()
        productid=request.form.get('productid')
        customerid=request.form.get('customerid')
        quantity=request.form.get('quantity')
        cn.execute(f"insert into orders(product_id,customer_id,quantity) values('{productid}','{customerid}','{quantity}')")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addorder.html')
    
@app.route("/add-supplier",methods=['GET','POST'])
def addsupplier():
    if request.method=='POST':
        cn=connect.cursor()
        suppliername=request.form.get('suppliername')
        supplieraddr=request.form.get('supplieraddr')
        supplieremail=request.form.get('supplieremail')
        cn.execute(f"insert into supplier(supplier_name,supplier_addr,supplier_email) values('{suppliername}','{supplieraddr}','{supplieremail}')")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addsupplier.html')
    
@app.route("/update-product",methods=['GET','POST'])
def updateproduct():
    if request.method=='POST':
        cn=connect.cursor()
        productid=request.form.get('product_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  product set {change} = '{newvalue}' where product_id = '{productid}'")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateproduct.html')
    
@app.route("/update-orders",methods=['GET','POST'])
def updateorder():
    if request.method=='POST':
        cn=connect.cursor()
        orderid=request.form.get('order_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id = '{orderid}'")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateorder.html')
    
@app.route("/update-supplier",methods=['GET','POST'])
def updatesupplier():
    if request.method=='POST':
        cn=connect.cursor()
        supplierid=request.form.get('supplier_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  supplier set {change} = '{newvalue}' where supplier_id = '{supplierid}'")
        connect.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatesupplier.html')
    
@app.route("/delete-product", methods=['GET', 'POST'])
def deleteproduct():
    if request.method == 'POST':
        cn = connect.cursor()
        productid = request.form.get('product_id')
        
        # Check if the product exists in the database
        cn.execute(f"SELECT * FROM product WHERE product_id = '{productid}'")
        product = cn.fetchone()
        
        if product:
            # Delete the product from the database
            cn.execute(f"DELETE FROM product WHERE product_id = '{productid}'")
            connect.commit()
            print('Product has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Product does not exist'})
    else:
        return render_template('deleteproduct.html')
    
@app.route("/delete-order", methods=['GET', 'POST'])
def deleteorder():
    if request.method == 'POST':
        cn = connect.cursor()
        orderid = request.form.get('order_id')
        
        # Check if the order exists in the database
        cn.execute(f"SELECT * FROM orders WHERE order_id = '{orderid}'")
        order = cn.fetchone()
        
        if order:
            # Delete the order from the database
            cn.execute(f"DELETE FROM orders WHERE order_id = '{orderid}'")
            connect.commit()
            print('Order has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Order does not exist'})
    else:
        return render_template('deleteorder.html')
    
@app.route("/delete-supplier", methods=['GET', 'POST'])
def deletesupplier():
    if request.method == 'POST':
        cn = connect.cursor()
        supplierid = request.form.get('supplier_id')
        
        # Check if the supplier exists in the database
        cn.execute(f"SELECT * FROM supplier WHERE supplier_id = '{supplierid}'")
        supplier = cn.fetchone()
        
        if supplier:
            # Delete the supplier from the database
            cn.execute(f"DELETE FROM supplier WHERE supplier_id = '{supplierid}'")
            connect.commit()
            print('Supplier has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Supplier does not exist'})
    else:
        return render_template('deletesupplier.html')

@app.route("/delete-customer", methods=['GET', 'POST'])
def deletecustomer():
    if request.method == 'POST':
        cn = connect.cursor()
        customerid = request.form.get('customer_id')
        
        # Check if the customer exists in the database
        cn.execute(f"SELECT * FROM customer WHERE customer_id = '{customerid}'")
        customer = cn.fetchone()
        
        if customer:
            # Delete the customer from the database
            cn.execute(f"DELETE FROM customer WHERE customer_id = '{customerid}'")
            connect.commit()
            print('Customer has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Customer does not exist'})
    else:
        return render_template('deletecustomer.html')


    



if __name__=='__main__':
    app.run()





