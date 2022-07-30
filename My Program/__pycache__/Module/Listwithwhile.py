'''subject_marks=[45,50,67,89,66]
for marks in subject_marks:
    print (marks)
print(f"maximum marks={max(subject_marks)}")
print(f"minumum marks={min(subject_marks)}")
print(f"Total marks={sum(subject_marks)}")
print(f"lenght of Marks={len(subject_marks)}")
subject_marks.sort()
print(subject_marks)
subject_marks.sort(reverse=True)
print(subject_marks)'''
#If we have store element in existing list we have subject marks...
shoppin_cart=[]
for i in range(1,6):
    item=input("Enter item")
    shoppin_cart.append(item)
print(shoppin_cart)


