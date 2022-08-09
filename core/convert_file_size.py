import os

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{num} {x}"
            # return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)

        fsize = file_info.st_size

        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if fsize < 1024.0:
                return f"{fsize} {x}"
                # return "%3.1f %s" % (fsize, x)
            fsize /= 1024.0
        return fsize

