import requests,flask
from flask import Flask,jsonify,request
app=Flask(__name__)

headers = {
    'Client-Id': 'kunaiu-android',
    'Client-Secret': 'b7022a16e0c896575g2d82c33a8h2d9d36781g33',
    'Accept': 'application/*+json, application/json',
    'ku_version_code': '6',
    'ku-version-code': '6',
    'Authorization': 'Bearer 6ff1c5300e78ee59cf63625ab7a711074b51f3b2',
    'Host': 'api.kunaiu.com',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.13',
}

@app.route('/anime')
def mm():
    
    date=request.args.get('date')
    Se=request.args.get('ss')
    if Se=='الربيع' or Se=='ربيع':
    	mo='Spring'
    if Se=='الصيف'or Se=='صيف':
    	mo='Summer'
    if Se=='خريف'or Se=='الخريف':
    	mo='Autumn'
    if Se=='شتاء'or Se=='الشتاء':
    	mo='Winter'
    params = {'json': f'{{"_offset":0,"_limit":30,"_order_by":"anime_rating_desc","list_type":"filter","anime_release_years":{date},"anime_season":"{mo}","just_info":"Yes"}}',
}
    response = requests.get('https://api.kunaiu.com/anime/public/animes/get-published-animes', params=params, headers=headers).json()['response']['data']
    data={'data':response}
    return jsonify(data)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
    