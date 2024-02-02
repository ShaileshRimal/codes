word=["a",3,"b",5,7]
# word
def concat(list):
    num=len(list)
    result=""
    for i in list:
        result+=str(i)

    return result

print(concat(word))



