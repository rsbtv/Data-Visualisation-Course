from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, hn_links, comments = [], [], []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    # hn_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    # hn_links.append(hn_link)
    # comments.append(submission_dict['comments'])
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")
    hn_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    hn_links.append(hn_link)
    comments.append(submission_dict['comments'])

data = [{
    'type': 'bar',
    'x': hn_links,
    'y': comments,
    #    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most-commented articles on Hacker-news',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Article',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
    'yaxis': {'title': 'Comments',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_articles.html')