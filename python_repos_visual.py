import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000" 

headers = {"Accept":"application/vnd.github.v3+json"}  
r = requests.get(url,headers=headers)
print(f"Status code : {r.status_code}")
response_dict = r.json()
print(f"Complete_results: {response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
repo_names, stars= [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

fig= px.bar(x=repo_names,y=stars)       #使用 px.bar() 函数创建了一个条形图
title = "Most-Starred Python Projects on GitHub"
labels = {"x":"Repository", "y":"Stars"}


fig= px.bar(x=repo_names,y=stars,title=title,labels=labels)   #设置title和labels
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)  #使用fig.update_layout() 方法修改一些图形元素
#xaxis_title_font_size x坐标轴标题字体大小

fig.show()

#添加定制工具提示
hover_texts = []
for repo_dict in repo_dicts:
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

fig=px.bar(x=repo_names,y=stars,title=title,labels=labels,hover_name=hover_texts)       #hover_name参数使鼠标移动到对应的条形上时，会显示hover_texts中的文本
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()

#添加可单击的链接
# Plotly 允许在文本元素中使用 HTML，这让你能够轻松地在图形中添加链接.
repo_links = []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"     #使用 html
    repo_links.append(repo_link)

fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6) #修改条形颜色和透明度   1表示完全不透明
fig.show()
