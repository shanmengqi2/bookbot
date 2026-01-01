def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def count_words(text):
  num_words = 0
  words_list = text.split()
  num_words = len(words_list)
  return num_words

def count_characters(text):
  character_dict = {}
  for c in text.lower():
    if c in character_dict:
      character_dict[c] += 1
    else:
      character_dict[c] = 1
  return character_dict

def format_stat(filepath,count,dict_list):
  print("============ BOOKBOT ============")
  print("Analyzing book found at "+filepath[2:]+"...")
  print("----------- Word Count ----------")
  print(f"Found {count} total words")
  print("--------- Character Count -------")

  for item in dict_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")

  print("============= END ===============")

def dict_to_dictList(c_dict):
  dict_list = []
  for item in c_dict:
    char_num_dict = {}
    char_num_dict["char"] = item
    char_num_dict["num"] = c_dict[item]

    # append to list
    dict_list.append(char_num_dict)
  
  # sort list
  dict_list.sort(reverse=True, key=sort_on)
  return dict_list
  
  

def sort_on(items):
    return items["num"]