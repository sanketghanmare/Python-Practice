class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f'{self.start_tag}{self.contents}{self.end_tag}'

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN '
                         'http://www.w3.org/TR/html4/loose.dtd', '')
        self.end_tag = ''


class Head(Tag):
    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)
    # def __init__(self, contents="This is a Head Tag"):
    #     super().__init__('head', f'<title>{contents}</title>')


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')  # body contents will be built seperately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):
    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML document')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open('text.html', 'w') as test_doc:
        my_page.display(file=test_doc)

new_body = Body()
new_body.add_tag('h1', 'Aggregation')
new_body.add_tag('p',
                 'unlike <strong>composition</strong>, aggregations uses existing instances of objects to build up another object.')
new_body.add_tag('p', "The composed of object doesn't actually own the objects ...." )
# give our document new content by swithching its body
my_page._body = new_body

with open('test2.html', 'w') as test_doc:
    my_page.display(file=test_doc)
