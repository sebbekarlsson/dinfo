from dinfo.utils import get_dirname, get_all_files, get_authors


def run():
    files = get_all_files()

    info = ''
    info += 'name: ' + get_dirname() + '\n'

    info_buffer = ''
    for k, v in files.items():
        if k in ['count_total', 'count_lines', 'count_size']:
            continue

        info += 'lines of {} = {} | ({} bytes)\n'\
            .format(k, v['lines'], v['size'])
        info_buffer += 'number of {} files = {}\n'.format(k, v['count'])

    info += info_buffer

    info += 'total number of files = {}\n'.format(files['count_total'])
    info += 'total number of lines = {}\n'.format(files['count_lines'])
    info += 'total size = {} MB\n'.format(files['count_size'])
    info += 'Authors: [{}]'.format(', '.join(get_authors()))

    print(info)
