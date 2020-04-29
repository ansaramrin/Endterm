s = {int(i) for i in input().split()}
def n(s: set):
    news = set()
    for i in s:
        news.add(i-1)
        news.add(i+1)
    return news
print(n(s))
