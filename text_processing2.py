#######################
# Test Processing II  #
#######################

def digits_to_words(input_string:str) -> str:
  nums = ['zero','one','two','three','four','five', 'six','seven','eight','nine','ten']
  dict_ = {}

  for n,j in enumerate(nums):
    dict_[n] = j

  tmp = []
  for i in input_string:
    if i.isdigit():
      tmp.append(dict_[int(i)])

  return ' '.join(tmp)



def to_camel_case(underscore_str:str) -> str:
  list_ = underscore_str.split('_')
  camelcase_str = ''
  for i, s in enumerate(list_):
    if s == '':
      continue
    
    s = s.lower()
    
    if camelcase_str == '':
      camelcase_str += s
      continue

    s = s[0].upper() + s[1:]
    camelcase_str += s 
  
  return camelcase_str