import os
import subprocess


def get_authors():
    gitlog = subprocess.check_output(['git', 'log', '--all'])\
        .decode('utf-8').split('\n')

    authors = []

    for entry in gitlog:
        if 'Author' not in entry:
            continue

        author = entry.split('Author: ')[1]

        if author not in authors:
            authors.append(author)

    return authors


def get_full_dir_path():
    return os.getcwd()


def get_dirname():
    cwd = get_full_dir_path()
    cwd = cwd.split('/')[len(cwd.split('/'))-1]

    return cwd


def get_all_files():
    ignored_extensions = [
        '.exe',
        '.out',
        '.egg',
        '.swp',
        '.swl',
        '.swj',
        '.jpg',
        '.png',
        '.gif',
        '.jpeg',
        '.bmp',
        '.db',
        '',
        '.pyc',
        '.ttf',
        '.csh',
        '.fish',
        '.egg',
        '.egg-link',
        '.rst',
        '.pot',
        '.mo',
        '.po',
        '.pem',
        '.tmpl',
        '.7',
        '.so',
        '.o',
        '.a'
    ]

    full_path = get_full_dir_path()

    count = 0
    total_lines = 0
    total_size = 0
    extensions = {}

    for root, dirs, files in os.walk(full_path):
        count += len(files)

        for _file in files:
            filename, ext = os.path.splitext(_file)

            if ext in ignored_extensions:
                continue

            file_path = os.path.join(root, _file)

            lines = 0
            with open(file_path) as __file:
                lines = __file.read().count('\n')
            __file.close()

            total_lines += lines

            if ext not in extensions:
                extensions[ext] = {}
                extensions[ext]['lines'] = lines
                extensions[ext]['count'] = 1
                extensions[ext]['size'] = os.path.getsize(file_path)
            else:
                extensions[ext]['lines'] += lines
                extensions[ext]['count'] += 1
                extensions[ext]['size'] += os.path.getsize(file_path)

            total_size += (os.path.getsize(file_path) * 0.001) * 0.001

        extensions['count_total'] = count
        extensions['count_lines'] = total_lines
        extensions['count_size'] = total_size

    return extensions
