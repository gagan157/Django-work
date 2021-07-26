msg="""hi 
how a
re 
you"""
remove_newline="on"
name="gagan"
email="gagan@"
if remove_newline=="on":
    ntext=""
    for char in msg:        
        if char!="\n":
            ntext=ntext+char                    
    param={"name":name,"email":email,"message":ntext} 
    print(param["message"])
