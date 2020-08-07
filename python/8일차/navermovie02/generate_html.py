import webbrowser
from adp_casting import GetCastingByMovie

def GetHtmlTemplate(template_path):
    f = open(template_path, 'r', encoding='utf8')
    html = f.read()
    f.close()
    return html

def GenMovieHtml(movies, save_path):
    html = GetHtmlTemplate('C:/07.27-12.1_CLOUD/python/8일차/navermovie02/html/main.html')

    li_list_text = ''
    for item in movies:
        title_text = '<div class="movie-title">{0}</div>'.format(item.m_title)
        img_text = '<img class="movie-poster" src="{0}"></img>'.format(item.img_src)
        li_list_text += '<a href="moviedetail/{0}.html">{1}{2}</a>'.format(item.m_code, img_text, title_text)

    html = html.replace('@RENDER_MOVIES', li_list_text)

    f = open(save_path, 'w', encoding='utf8')
    f.write(html)
    f.close()
    webbrowser.open(save_path)


def GenMovieDetailHtml(movies, save_path):
    
    for item in movies:
        html = GetHtmlTemplate('C:/07.27-12.1_CLOUD/python/8일차/navermovie02/html/detail.html')
        li_list_text = ''
        castings = GetCastingByMovie(item.m_code)

        for c in castings:  
            li_list_text += '<li>{0}</li>'.format(c.c_name)
        
        html = html.replace('@RENDER_IMG_SRC', item.img_src)
        html = html.replace('@RENDER_TITLE', item.m_title)
        html = html.replace('@RENDER_CASTING', li_list_text)

        f = open('{0}/{1}.html'.format(save_path, item.m_code), 'w', encoding='utf8')
        f.write(html)
        f.close()
    
    webbrowser.open('C:/07.27-12.1_CLOUD/python/8일차/navermovie02/html/movielist.html')
    
    
