import bs4
html_str="<html><div></div></html>"

bsObj = bs4.BeautifulSoup(html_str, "html.parser")

if __name__ == "__main__":
	print(type(bsObj))
	print(bsObj)
