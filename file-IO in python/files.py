# so i have a file with content this  -- Hello, My Name is Divyanshu and i am a AI Engineer at Google at L6 Level my GID is 1912

# opening in read mode 
r = open("testing.txt", 'r')
print(r)
text = r.read()
print(text)
r.close()

print()


r = open("testing2.txt", "w")
txt = r.write("Hello this file is not existed but i use write method to create and write the content")
print(txt)
r.close()


r = open("testing2.txt", "a")
r.write("\nHello this content is written using append method")
r.close()


# here again and again i need to close the file so here is the shortcut and more effcient method to do this----

with open("testing2.txt", "a") as m:
    m.write("\n heyy i am using ""with"" now so i dont need to close the file again and again")

