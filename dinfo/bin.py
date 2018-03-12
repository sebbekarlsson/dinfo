from dinfo.utils import get_dirname, get_all_files


def run():
    files = get_all_files()

    info = ''
    info += 'name: ' + get_dirname() + '\n'
    info += 'files: ' + str(files[0]) + '\n'
    info += 'lines: ' + str(files[1]) + '\n'
    info += 'extensions: [{}]'.format(', '.join(files[2]))

    print(info)
