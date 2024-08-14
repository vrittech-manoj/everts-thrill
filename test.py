data  = [{'name':"ram","class":7},{'name':"shyam","class":8}]

modify_data = [{"roll":1,**d} for d in data]
print(modify_data)