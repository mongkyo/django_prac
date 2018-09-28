import os

current_file = os.path.abspath(__file__)
blog_forder = os.path.dirname(current_file)
app_forder = os.path.dirname(blog_forder)
#templates_forder = os.path.join(app_forder, post_list.html)


print(current_file)
print(blog_forder)
print(app_forder)
#print(templates_forder)
