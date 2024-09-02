from operator import itemgetter
import requests

url =  "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    #每篇文章都执行一个API请求
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)


# 按照评论数对提交的字典列表进行降序排序
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
# 使用 operator 模块中的函数 itemgetter()
#我们向这个函数传递了键 'comments'，因此它从这个列表的
#每个字典中提取与键 'comments' 对应的值。


# 遍历每个提交的字典对象，打印其中的关键信息
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")