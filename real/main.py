import requests
import json

def get_data():

    cookies = {
        'lang': 'ru',
        'rrpvid': '499671429539068',
        '_gid': 'GA1.2.22867773.1689937975',
        '_gcl_au': '1.1.955200086.1689937975',
        'cartUserCookieIdent_v3': 'a3fafc95d3ba0d02bbcf60158ddb7030c4b348ef518688665d2667f73dd27366a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a74abd62-276f-3694-9231-7545091ed224%22%3B%7D',
        'phonesIdent': '989a351d452b2e385092122dfd49ce92c7cd9fed85d4b880e7826bd8fe1b3c54a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%228a146f3b-05e8-4c60-92c4-b934ca34ee3a%22%3B%7D',
        'rcuid': '64b3ef50c4192110b654d0de',
        'tmr_lvid': '2247ade18b1a284402f3b0528aef0e5e',
        'tmr_lvidTS': '1689937975244',
        '_ym_uid': '1689937975940574031',
        '_ym_d': '1689937975',
        'PHPSESSID': 'ba3e88c2d4732aebd03dcb5839c76768',
        '_csrf': 'aef0e6acaa229bce77e466f0d999fe6278b0fbaee6ca8e7c80eaab0c7c92db81a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EReGDUaikNY9OAUJnRHtWnP4tvsHK3kW%22%3B%7D',
        'city_path': 'sibai',
        'current_path': 'dbf135a2b72bf4e890ee3d09f8917ef5019e720850ec051d0be7683cd40a0798a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A109%3A%22%7B%22city%22%3A%229fddc42f-c5c1-11e2-beca-00155d030b1f%22%2C%22cityName%22%3A%22%5Cu0421%5Cu0438%5Cu0431%5Cu0430%5Cu0439%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'qrator_jsid': '1690027157.456.OJ5iRjMU9EJBtXgX-o0fdh640mb8suik1klo9i3mt8vfmh4sg',
        '_gat': '1',
        '_gat_%5Bobject%20Object%5D': '1',
        'tmr_detect': '0%7C1690029039040',
        '_ga': 'GA1.2.980157781.1689937975',
        '_gat_UA-8349380-2': '1',
        '_ga_FLS4JETDHW': 'GS1.1.1690025699.5.1.1690029070.60.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'lang=ru; rrpvid=499671429539068; _gid=GA1.2.22867773.1689937975; _gcl_au=1.1.955200086.1689937975; cartUserCookieIdent_v3=a3fafc95d3ba0d02bbcf60158ddb7030c4b348ef518688665d2667f73dd27366a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a74abd62-276f-3694-9231-7545091ed224%22%3B%7D; phonesIdent=989a351d452b2e385092122dfd49ce92c7cd9fed85d4b880e7826bd8fe1b3c54a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%228a146f3b-05e8-4c60-92c4-b934ca34ee3a%22%3B%7D; rcuid=64b3ef50c4192110b654d0de; tmr_lvid=2247ade18b1a284402f3b0528aef0e5e; tmr_lvidTS=1689937975244; _ym_uid=1689937975940574031; _ym_d=1689937975; PHPSESSID=ba3e88c2d4732aebd03dcb5839c76768; _csrf=aef0e6acaa229bce77e466f0d999fe6278b0fbaee6ca8e7c80eaab0c7c92db81a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EReGDUaikNY9OAUJnRHtWnP4tvsHK3kW%22%3B%7D; city_path=sibai; current_path=dbf135a2b72bf4e890ee3d09f8917ef5019e720850ec051d0be7683cd40a0798a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A109%3A%22%7B%22city%22%3A%229fddc42f-c5c1-11e2-beca-00155d030b1f%22%2C%22cityName%22%3A%22%5Cu0421%5Cu0438%5Cu0431%5Cu0430%5Cu0439%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; _ym_isad=2; _ym_visorc=b; qrator_jsid=1690027157.456.OJ5iRjMU9EJBtXgX-o0fdh640mb8suik1klo9i3mt8vfmh4sg; _gat=1; _gat_%5Bobject%20Object%5D=1; tmr_detect=0%7C1690029039040; _ga=GA1.2.980157781.1689937975; _gat_UA-8349380-2=1; _ga_FLS4JETDHW=GS1.1.1690025699.5.1.1690029070.60.0.0',
        'Origin': 'https://www.dns-shop.ru',
        'Referer': 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/no-referrer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
        'X-CSRF-Token': 'wwQrRtOx9OoPRO9qANUMjS7YkXv9g7pDjZCsrmXoGseGVk4Bl-SVg2QKtlNPlFnHQIrZD6rt6nf55t_mLttxkA==',
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = 'data={"type":"product-buy","containers":[{"id":"as-Ez7xph","data":{"id":"5404475"}},{"id":"as-Wihj3v","data":{"id":"5407513"}},{"id":"as-o_x0aN","data":{"id":"5090600"}},{"id":"as-MgmuvG","data":{"id":"5002613"}},{"id":"as-nZjyfz","data":{"id":"5004473"}},{"id":"as-glb64W","data":{"id":"1620709"}},{"id":"as-Hy8W7g","data":{"id":"5014414"}},{"id":"as-yBKnFM","data":{"id":"5099730"}},{"id":"as-RYCmIC","data":{"id":"5012303"}},{"id":"as-Xrb5LO","data":{"id":"1383865"}},{"id":"as-iI5IJ9","data":{"id":"5405585"}},{"id":"as-JLKfQq","data":{"id":"5082769"}},{"id":"as-im6Zz8","data":{"id":"4757252"}},{"id":"as-5yNGjm","data":{"id":"5098353"}},{"id":"as-jbOwO2","data":{"id":"5014412"}},{"id":"as-7guaiD","data":{"id":"5083016"}},{"id":"as--ithhq","data":{"id":"5076427"}},{"id":"as-1ltLE4","data":{"id":"5080942"}}]}'

    response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', cookies=cookies, headers=headers, data=data).json()

    products_body = response.get('data').get("states")
    result = []

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(products_body, file, indent=4, ensure_ascii=False)

    for i in products_body:
        data = i.get('data')
        product_name = data.get("name")
        product_link_id = data.get("id")
        
        if data.get('avail') is None:
            price = data.get('price')
            product_CurPrice = price.get("current")
            product_MinPrice = price.get("min")
        
            if product_MinPrice is not None:
                product_discount = product_CurPrice - product_MinPrice

                result.append(
                    {
                        "Name": product_name,
                        'id': product_link_id,
                        "Default_price": product_CurPrice,
                        "Price_with_discount": product_MinPrice,
                        "Discount": product_discount
                    }
                )
                
            else:
                result.append(
                    {
                        "Name": product_name,
                        'id': product_link_id,
                        "Default_price": product_CurPrice,
                    }
                )


    with open('result1.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))

def main():
    get_data()

if __name__ == '__main__':
    main()