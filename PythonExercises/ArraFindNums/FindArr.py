def main():
    pass

arr=[1,2,4,6,10]
diff_hash={}
expected_sum=3
for i in arr:
    if i in diff_hash:
        print (i,diff_hash[i])
    key=expected_sum-i
    diff_hash[key]=i        