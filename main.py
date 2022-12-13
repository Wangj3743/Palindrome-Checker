def palindrome(x):
  txt = list(x)
  # print(txt[:int(len(txt)/2)]) # i tried to find a way to make two lists that divide in the middle and remove the middle value if it is present
  # print(txt[(int(len(txt)/2)):]) 
  if len(txt) % 2 == 1: txt.pop(int(len(txt)/2)) # checks if there is a character in the middle and removes it
  list1, list2 = txt[0:int(len(txt)/2)], txt[int(len(txt)/2):] #split the list into two and reverse the order of the second list
  if list1 == list2[::-1]: return f"\n\"{x}\" is a palindrome."
  else: return f"\n\"{x}\" is not a palindrome."

txt = print(palindrome(input("Enter your plaindrome here: (based on characters; spaces and other special characters count)\n"))) # racecar, hannah, lol, 02022020 
