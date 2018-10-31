# coding=utf-8
# 使用终端登陆，登陆过一次后会保存token，之后直接假造token登陆
from __future__ import unicode_literals, print_function
import os
from zhihu_oauth import ZhihuClient

TOKEN_FILE = r'Data\login\token.pkl'

client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
    print('login success!')
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)

# # 回答信息
# answer = client.answer(94150403)
#
# print(answer.question.title)
# print(answer.author.name)
# print(answer.voteup_count)
# print(answer.thanks_count)
# print(answer.created_time)
# print(answer.updated_time)
#
# for voter in answer.voters:
#     print(voter.name, voter.headline)

question = client.question(35166763)

print(question.title)

count = 0
for answer in question.answers:
    answer.save(r'Data\Answers\\' + question.title)
    count += 1
    if count == 10:
        break
