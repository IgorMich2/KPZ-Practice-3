import platform

a = []

def find_palindromes_in_sub_string(input, j, k):
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    a.append(input[j: k + 1])

    j -= 1
    k += 1


def palindrom(text):
  for i in range(0, len(text)):
    find_palindromes_in_sub_string(text, i - 1, i + 1)
    find_palindromes_in_sub_string(text, i, i + 1)
  return a;

def validate_ip(ip_address):
    a = ip_address.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def get_os():
    return platform.system()


s = "aabbbaa";
print(palindrom(s))

print(validate_ip('192.168.2.10'))
print(validate_ip('266.168.2.10'))
print(get_os())