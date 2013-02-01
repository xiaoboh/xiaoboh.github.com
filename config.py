
import web
import os
import markdown
import codecs
import time


title = "xiaobo's blog"
src_dir = 'blog_raw'
dst_dir = 'static/html'

render = web.template.render('templates'
        , base='base'
        , globals={'title':title})


def get_blogs():
    blogs = []
    odd = True
    for f in os.listdir( src_dir ):
        fpath = os.path.join( src_dir, f )
        bf = open( fpath )
        blogf = os.path.join( 'static/html', os.path.splitext(f)[0]) + '.html'

        blog = dict( title=bf.readline()
                , summary=bf.readline()
                , odd=odd 
                , time=time.strftime("%Y-%m-%d %X", time.gmtime(os.path.getmtime(fpath)))
                , href=blogf )
        odd = not odd
        blogs.append(blog)

    return sorted(blogs, key=lambda x:x['time'], reverse=True)


def build_index():
    html = render.main( title, get_blogs() )
    open('index.html','w').write( str(html) )


def build_blogs():
    for f in os.listdir( src_dir ):
        blog_src = os.path.join( src_dir, f )
        blog_dst = os.path.join( dst_dir, os.path.splitext(f)[0] + '.html')

        if os.path.exists(blog_dst) and os.path.getmtime(blog_src) < os.path.getmtime(blog_dst):
            continue

        text = codecs.open( blog_src, mode='r', encoding='utf8' ).read()
        html = render.blog( markdown.markdown(text) )
        open( blog_dst, 'w').write( str(html) )



