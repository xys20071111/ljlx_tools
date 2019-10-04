import sys,requests
cookie = sys.argv[1]
cookies={'sc1':cookie}
print("Lejiqolexue tools,version 0.0.1")
print("Cookies in using:"+cookie)
print('(1) Pull a blog.\n(2) Get blog list.\n(3) Publish a blog.')
print('(4) Get user info.')
print('Please enter a number,if you want to exit,enter ^C')
choice = int(input())
if choice == 1:
    blogid = input('Please enter a blog id:')
    res = requests.get('http://blog.app.ljlx.com/rest/blog/cont.ashx?talent_id='+blogid,cookies=cookies)
    print(res.text)
    choice = input('Would you like to save it to a JSON file? [y/n]')
    if choice == 'y':
        filename = input('Filename(without ".json"):')
        with open(filename+'.json','w+') as f:
            f.write(res.text)
elif choice == 2:
    typeId = input('Type id:')
    pageSize = input('Page size:')
    res = requests.get('http://blog.app.ljlx.com/rest/blog/gettalent.ashx',cookies=cookies,data={'tag':typeId,'page_index':'1','page_size':pageSize})
    choice = input('Save it into a JSON file? [y/n]')
    if choice == 'y':
        filename = input('Filename(without ".json"):')
        with open(filename+'.json','w+') as f:
            f.write(res.text)
    else:
            print(res.text)
elif choice == 3:
        print('Not reday.')
elif choice == 4:
    uid = input('UID:')
    res = request.post()
