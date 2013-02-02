
import web
import os
import markdown
import codecs
import time


title = "xiaobo blog"
domain = 'xiaobo.info'
url = 'http://xiaobo.info'

src_dir = 'blog_raw'
dst_dir = 'static/html'

render = web.template.render('templates'
        , base='base'
        , globals={'title':title, 'domain':domain, 'url':url})


def get_blogs():
    blogs = []
    for f in os.listdir( src_dir ):
        fpath = os.path.join( src_dir, f )
        bf = open( fpath )
        blogf = os.path.join( 'static/html', os.path.splitext(f)[0]) + '.html'

        blog = dict( title=bf.readline()
                , summary=bf.readline()
                , time=time.strftime("%Y-%m-%d %X", time.gmtime(os.path.getmtime(fpath)))
                , href=blogf )
        blogs.append(blog)

    return sorted(blogs, key=lambda x:x['time'], reverse=True)


def build_index():
    html = render.main( get_blogs() )
    open('index.html','w').write( str(html) )


def build_blogs():
    for f in os.listdir( src_dir ):
        blog_src = os.path.join( src_dir, f )
        blog_dst = os.path.join( dst_dir, os.path.splitext(f)[0] + '.html')

        if os.path.exists(blog_dst) and os.path.getmtime(blog_src) < os.path.getmtime(blog_dst):
            continue

        text = codecs.open( blog_src, mode='r', encoding='utf8' ).read()
        html = render.blog( markdown.markdown(text), f, f
                , "{0}//{1}".format(url, blog_dst)  )
        open( blog_dst, 'w').write( str(html) )



