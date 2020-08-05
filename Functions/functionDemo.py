# def center_text(*args, sep='', end='\n', file=None, flush=False):
#     text = ''
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)


# with open("center", mode='w') as center_file:
#     # call function center_text
#     center_text("Spam and eggs", file=center_file)
#     center_text('spam, spam and eggs', file=center_file)
#     center_text(12, file=center_file)
#     center_text('spam, spam and eggs asdfasdfdas adf', file=center_file)


def center_text(*args, sep=''):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


print(center_text("Spam and eggs"))
print(center_text('spam, spam and eggs'))
print(center_text(12))
print(center_text('spam, spam and eggs asdfasdfdas adf'))

s1 = center_text("=" + str(12 * 3))
print(s1)
