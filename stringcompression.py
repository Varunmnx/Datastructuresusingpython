from itertools import takewhile, dropwhile


def compress(s):
    if not s:
        return ""
    return str(len(list(takewhile(lambda c: c == s[0], s)))) + s[0] + compress(
        "".join(list(dropwhile(lambda c: c == s[0], s))))

if __name__ == "__main__":
  print("enter your string :")
  s = input().strip()
  print(compress(s))