# https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150


'''
My soln

Neetcode's soln is prolly more elegant (TODO: Look at it!)
'''

def encode(strs):
    out = ""
    for string in strs:
        if not string:
            out += "."
            continue
        for ch in string:
            out += str(ord(ch))
            out += ","
        out += "."
    return out

def decode(s):
    words = s.split(".")
    out = []
    for word in words:
        if not word:
            out.append("")
            continue
        chars = word.split(",")
        for i in range(len(chars)):
            if not chars[i]:
                chars.pop(i)  # Removing "" when there is ',.' combination (occurs at end of every word in the of list)

        chars = [chr(int(char)) for char in chars]
        out_word = ""
        for char in chars:
            out_word += char
        out.append(out_word)
    out.pop()  # removing the last "" (occurs automatically due to last fullstop)
    return out


a = ["Hello", "World!"]
print(encode(a))
print(decode(encode(a)))
