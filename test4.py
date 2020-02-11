def renderfile(file, data) :
    html = open(file, "rt", encoding="utf-8").read()
    for v in data :
        html = html.replace("@"+v, data[v])
    return html

html = "hello @v1   test @v2   item @v3 "
data = {"v1":"안녕하세요",  "v2":"이순신", "v3":"^^"}
html = render(html, data)
print(html)