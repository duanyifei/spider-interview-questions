# coding:utf8
"""
请补全下方代码
"""
import re

with open("weibo_topic.html", encoding="utf8") as f:
    html = f.read()

regex_pattern = re.compile("请补全此处正则表达式")

scripts = re.findall("<script>(.*?)</script>", html)

for script in scripts:
    infos = regex_pattern.search(script)
    if infos:
        print(infos.groupdict())

# 输出
'''
{'ns': 'pl.common.webim', 'domid': 'pl_common_webim'}
{'ns': 'pl.top.index', 'domid': 'pl_common_top'}
{'ns': 'page.pl.content.changeLanguage.index', 'domid': 'pl_common_footer'}
{'ns': 'pl.base.index', 'domid': 'pl_common_base'}
{'ns': 'pl.invoke.forward', 'domid': 'pl_common_forword'}
{'ns': 'pl.header.objectHead.index', 'domid': 'pl_common_topicbase'}
{'ns': 'pl.discover.leftnav.index', 'domid': 'Pl_Discover_LeftNav__2'}
{'ns': 'pl.content.miniTab.index', 'domid': 'Pl_Discover_SingleTextb__5'}
{'ns': 'pl.content.textnewlist.index', 'domid': 'Pl_Discover_TextNewList__3'}
{'ns': 'pl.content.miniTab.index', 'domid': 'Pl_Discover_Pt6Rank__4'}
'''
