import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"     #查询字符串 language:python是指定获取主要语言为python的仓库
    #sort:stars 是指定将项目按星数排序         添加条件: stars:>10000 是查找超过10000颗星的python仓库

headers = {"Accept":"application/vnd.github.v3+json"}  #指定使用这个版本的API,并返回JSON格式 的结果
r = requests.get(url,headers=headers)
print(f"Status code : {r.status_code}")
response_dict = r.json()        #用json()方法将数据转换成字典
print(response_dict.keys())

print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete results:{not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")

for key,value in sorted(repo_dict.items()):
    # print(value)
    print(key)

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

for dict in repo_dicts:
    print(f"\nName: {dict['name']}")
    print(f"Owner: {dict['owner']['login']}")
    print(f"Stars: {dict['stargazers_count']}")
    print(f"Repository: {dict['html_url']}")
    print(f"Description: {dict['description']}")

# https://api.github.com/rate_limit  #可以看到github的限制  
# search里
#limit显示每分钟10个请求
#remaining 指还有 多少次
# reset 对应的值是配额将被重置的 Unix 时间或新纪元时间（从 1970 年 1 月 1 日零点开始经过的秒数）