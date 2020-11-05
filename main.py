import sys
import requests
import json


def user(commandList):
    if(commandList[0]) == 'get':
        uid = commandList[1]
        res = requests.get(
            'https://api.ljlx.com/platform/userinfo/getuserextinfo?user_id='+uid, cookies=cookies)
        print(res.text)

def blog(commandList):
    command = commandList[0]
    if command == 'get':
        blogid = commandList[1]
        res = requests.get(
            'http://blog.app.ljlx.com/rest/blog/cont.ashx?talent_id='+blogid, cookies=cookies)
        print(res.text)
    elif command == 'list':
        typeId = commandList[1]
        pageSize = commandList[2]
        res = requests.get('http://blog.app.ljlx.com/rest/blog/gettalent.ashx', cookies=cookies, data={
            'tag': typeId,
            'page_index': '1',
            'page_size': pageSize
        })
        print(res.text)
    elif command == 'publish':
        uid = commandList[1]
        btype = commandList[2]
        tag = commandList[3]
        title = commandList[4]
        summary = commandList[5]
        text = commandList[6]
        data = {
            'title': json.dumps({'title': title, 'summary': summary}),
            'user_id': uid,
            'proxy_user_id': uid,
            'content': '{"list":[{"type":10,"content":"<type=\"text\",size=6,fontsize=45.00,textcolor=\"33,33,33\">' + text + '"}]}', 'tag': tag, 'type': btype}
        print(requests.post('http://blog.app.ljlx.com/rest/blog/addtalent.ashx',
                            cookies=cookies, data=data).text)
    elif command == 'modify':
        uid = commandList[1]
        blogid = commandList[2]
        title = commandList[3]
        summary = commandList[4]
        text = commandList[5]
        data = {'title': json.dumps({'title': title, 'summary': summary}), 'user_id': uid, 'proxy_user_id': uid,
                'content': '{"list":[{"type":10,"content":"<type=\"text\",size=6,fontsize=45.00,textcolor=\"33,33,33\">' + text + '"}]}', 'tag': '1', 'type': '0', 'talent_id': blogid}
    print(requests.post('http://blog.app.ljlx.com/rest/blog/modifyblog.ashx',
                        cookies=cookies, data=data).text)

def help(commandList):
    if len(commandList) == 0:
        print('help <command> [subcommand]')
        return
    if len(commandList) == 1:
        command = commandList[0]
        if command == 'blog':
            print('subcommand: get list publish modify')
            return
        elif command == 'user':
            print('subcommand: get')
            return
    command = commandList[0]
    subcommand = commandList[1]
    if command == 'blog':
        if subcommand == 'get':
            print('blog get <BlogId>')
            return
        elif subcommand == 'list':
            print('blog list <TypeId> <PageSize>')
            return
        elif subcommand == 'publish':
            print('blog publish <uid> <TypeId> <Tag> <Title> <Summary> <Text>')
        elif subcommand == 'modify':
            print('blog modify <uid> <BlogId> <Title> <summary> <Text>')
    elif command == 'user':
        if subcommand == 'get':
            print('user get <uid>')

def run():
    command = input('>')
    commandList = command.split(' ')
    if commandList[0] == 'blog':
        blog(commandList[1:])
    elif commandList[0] == 'user':
        user(commandList[1:])
    elif commandList[0] == 'help':
        help(commandList[1:])
    elif commandList[0] == 'exit' or commandList[0] == 'quit':
        sys.exit(0)

if __name__ == '__main__':
    print("Lejiqolexue tools,version 0.0.1")
    token = '4CE2959613CAEE0AE15240B5979612FED5656A11aU1%2fMgHtBdWR2DBcaQw%2bsRV7NBWwYAj%2ft1mUi4aPu0Y0QRXPnGlmNjO%2b8Q6QrRvxGOjimokBxGbI0CZfr3tUYbV3zL24juyFpgVWf1MMn2CBIqgG6iRLEGukmTm%2fTGLPU5scgYjg4Qrkn8sZL1vjn9LV63flzsj%2byR2tx6Ql'
    if len(sys.argv) > 2:
        token = sys.argv[1]
    cookies = {'sc1': token}
    print("Token in using:"+token)
    while True:
        run()
