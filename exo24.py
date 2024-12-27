def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tabby", "batty")) # False