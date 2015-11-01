"""Generate the TOC in README."""

import os
import os.path as op
import json


_TOC_HEADER = '## Table of contents'
_CHAPTER_HEADERS = {
    1: 'Getting started with IPython',
    2: 'Interactive data analysis with pandas',
    3: 'Numerical computing with NumPy',
    4: 'Interactive plotting and Graphical Interfaces',
    5: 'High-performance and parallel computing',
    6: 'Customizing IPython',
}


def _get_readme_before_toc(file):
    with open(file, 'r') as f:
        readme = f.read()
    index = readme.index(_TOC_HEADER)
    before = readme[:index]
    return before


def _iter_chapters(root):
    for i in range(1, 7):
        yield op.realpath(op.join(root, 'chapter{0:d}'.format(i)))


def _iter_notebooks(chapter_path):
    for file in sorted(os.listdir(chapter_path)):
        if file.endswith('.ipynb'):
            with open(op.join(chapter_path, file), 'r') as f:
                text = f.read()
            yield op.join(chapter_path, file), 'execution_count' in text


def _get_chapter_header(num):
    name = _CHAPTER_HEADERS[num]
    return '### {num}. {name}'.format(num=num, name=name)


def _notebook_title(path):
    with open(path, 'r') as f:
        d = json.load(f)
    cells = d['cells']
    if not cells:
        return
    title = d['cells'][0]['source'].replace('#', '').strip()
    a, b = op.basename(path)[:2]
    return '{0}.{1}. {2}'.format(a, b, title)


def _nbviewer(path):
    dir = op.split(op.dirname(path))[-1]
    file = op.basename(path)
    return "http://nbviewer.ipython.org/github/ipython-books/minibook-2nd-code/blob/master/" + dir + '/' + file


def _iter_all(root):
    for i, chapter in enumerate(_iter_chapters(root)):
        yield '{0}\n\n'.format(_get_chapter_header(i + 1))
        for notebook, display_link in _iter_notebooks(chapter):
            title = _notebook_title(notebook)
            if not title:
                continue
            if display_link:
                yield '* [{0}]({1})\n'.format(title, _nbviewer(notebook))
            else:
                yield '* {0}\n'.format(title)
        yield '\n'


def generate(root):
    readme_file = op.join(root, 'README.md')
    before_toc = _get_readme_before_toc(readme_file)
    with open(readme_file, 'w') as f:
        f.write(before_toc)
        f.write(_TOC_HEADER + '\n\n')
        for item in _iter_all(root):
            f.write(item)


if __name__ == '__main__':
    curdir = os.path.dirname(os.path.realpath(__file__))
    root = op.realpath(op.join(curdir, '../'))
    generate(root)
