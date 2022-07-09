from fastapi import FastAPI
import webbrowser
import functions

# Home page URL
home_url = "https://inc-news.ru/"
functions.url_response(home_url)


app = FastAPI()


@app.get('/')
async def sp():
    return {'summer_practice'}


@app.get("/hp_news", description='Home page listing')
async def listing():

    functions.certain_page_parsing(home_url)
    _list = functions.get_articles_list()
    return _list


@app.post("/cn_page", description='Open a page with a certain news')
async def insert_string(title: str):

    title = title.replace("\\", "")

    _list = functions.get_titles_list()
    _refs = functions.get_refs_list()

    _flag = False
    for i in range(len(_list)):
        if title == _list[i]:
            _flag = True
            return webbrowser.open_new_tab(_refs[i])
    if not _flag:
        return {'There`s no such page'}


@app.post('/cn_section', description='Open certain news section')
async def listing(section: str):

    functions.clear()

    sections_list_refs, sections_list_titles = functions.sections_parsing(home_url)

    _list = functions.sections_parsing(home_url)

    _flag = False
    for i in range(len(sections_list_titles)):
        if section == sections_list_titles[i]:
            _flag = True
            functions.certain_page_parsing(sections_list_refs[i])
            _list = functions.get_articles_list()
            return _list[:-5]
    if not _flag:
        return {'There`s no such section'}
