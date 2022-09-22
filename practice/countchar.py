# test_dict="alkaisdeveloper"
# dict={}
# for i in test_dict:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# print(dict)

# test='alka is developer'
# dict={}
# for i in test:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict) 

def word_count(str):
  counts = dict()
  words = str.split()
  for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
  return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))