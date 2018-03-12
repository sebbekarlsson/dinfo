import os


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
    lines = 0
    extensions = []

    for root, dirs, files in os.walk(full_path):
        count += len(files)

        for _file in files:
            filename, file_extension = os.path.splitext(_file)

            if file_extension in ignored_extensions:
                continue

            if file_extension not in extensions:
                extensions.append(file_extension)

            with open(os.path.join(root, _file)) as __file:
                lines += __file.read().count('\n')
            __file.close()

    return [count, lines, extensions]
