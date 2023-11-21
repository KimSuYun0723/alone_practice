from bs4 import BeautifulSoup

html_doc = """
<!doctype html>
<html>
    <head>
        <title>
            기초 웹 크롤링
        </title>
    </head>
    <body>
        <table border="1">
            <caption> 과일 가격 </caption>
            <tr>
                <th> 상품 </th>
                <th> 가격 </th>
            </tr>
            <tr>
                <td> 오렌지 </td>
                <td> 100 </td>
            </tr>
            <tr>
                <td> 사과 </td>
                <td> 150 </td>
            </tr>
        </table>

        <table border="2">
            <caption> 의류 가격 </caption>
            <tr>
                <th> 상품 </th>
                <th> 가격 </th>
            </tr>
            <tr>
                <td> 셔츠 </td>
                <td> 30000 </td>
            </tr>
            <tr>
                <td> 바지 </td>
                <td> 50000 </td>
            </tr>
        </table>
    </body>
</html>
"""
bs_obj = BeautifulSoup(html_doc, "html.parser")
clothes = bs_obj.find_all("table", {"border":"2"})
print(clothes)