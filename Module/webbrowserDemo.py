import webbrowser

webbrowser.open("http://sk101.netlify.com")
webbrowser.open("http://www.python.org/")

for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=', ')

chrome = webbrowser.get("chrome")
chrome.open_new("https://www.udemy.com/")

safari = webbrowser.get("safari")
safari.open_new("https://www.udemy.com/")
