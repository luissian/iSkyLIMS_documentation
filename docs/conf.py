from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'iSkyLIMS'
copyright = u'2021, Luis Chapado , Sara Monzón'
author = u'Luis Chapado , Sara Monzón'

github_doc_root = 'https://github.com/luissian/iSkyLIMS_documentation/docs/'
