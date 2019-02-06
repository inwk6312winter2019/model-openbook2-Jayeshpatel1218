t=[]
def transit(filename):
        f=open(filename)
        for line in f:
                f1=tuple()
                line=line.split(",")
                str_name=line[2]
                full_name=line[4]
                from_str=line[6]
                to_str=line[7]
                f1=(str_name,full_name,from_str,to_str)
                t.append(f)
        return t
print(transit("Street_Centrelines.csv"))

