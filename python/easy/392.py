# s = "google"

s = "aaaaaa"


t = "bbaaaa"


def isSubsequence(s: str, t: str) -> bool:
    find_scope = 0
    for i, v in enumerate(s):
        if v in t[find_scope:]:
            find_scope = t.index(v)
            continue
        return False

    return True


a = isSubsequence(s, t)
