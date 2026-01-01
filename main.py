from stats import get_book_text, count_words, count_characters, dict_to_dictList, format_stat
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  filepath = sys.argv[1]
  file_contents = get_book_text(filepath)

  num_words = count_words(file_contents)
  c_dict = count_characters(file_contents)
  dict_list = dict_to_dictList(c_dict)

  format_stat("./books/frankenstein.txt", num_words, dict_list)



main()