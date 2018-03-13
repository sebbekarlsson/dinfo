import os
import subprocess


def get_authors():
    try:
        gitlog = subprocess.check_output(['git', 'log', '--all'])\
            .decode('utf-8').split('\n')
    except subprocess.CalledProcessError:
        return []

    authors = []

    for entry in gitlog:
        if 'Author' not in entry:
            continue

        author = entry.split('Author: ')[1].lower()

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
    full_path = get_full_dir_path()
    ignored_dirs = ['venv', 'node_modules', 'egg-info', '.git']
    ignored_extensions = ['']

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

            do_continue = False
            for ignored in ignored_dirs:
                if ignored in root.split('/'):
                    do_continue = True

            if do_continue:
                continue

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
