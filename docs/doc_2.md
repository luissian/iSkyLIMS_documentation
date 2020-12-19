Configuring AutoStructify
-------------------------

The behavior of AutoStructify can be configured via a dict in document setting.
In sphinx, you can configure it by `conf.py`. The following snippet
is what is actually used to generate this document, see full code at [conf.py](conf.py).

```python
github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

```

All the features are by default enabled

***List of options***

* __enable_auto_toc_tree__: whether enable [Auto Toc Tree](#auto-toc-tree) feature.
* __auto_toc_tree_section__: when enabled,  [Auto Toc Tree](#auto-toc-tree) will only be enabled on section that matches the title.
* __enable_auto_doc_ref__: whether enable [Auto Doc Ref](#auto-doc-ref) feature.  **Deprecated**
* __enable_math__: whether enable [Math Formula](#math-formula)
* __enable_inline_math__: whether enable [Inline Math](#inline-math)
* __enable_eval_rst__: whether [Embed reStructuredText](#embed-restructuredtext) is enabled.
* __url_resolver__: a function that maps a existing relative position in the document to a http link

Auto Toc Tree
-------------

One of important command in tools like sphinx is `toctree`. This is a command to generate table of contents and
tell sphinx about the structure of the documents. In markdown, usually we manually list of contents by a bullet list
of url reference to the other documents.

AutoStructify transforms bullet list of document URLs like this

```
* [Title1](doc1.md)
* [Title2](doc2.md)
```

to the AST of this following reStructuredText code

```rst
.. toctree::
   :maxdepth: 1

   doc1
   doc2
```

You can also find the usage of this feature in `index.md` of this document.
