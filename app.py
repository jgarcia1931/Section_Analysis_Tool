from flask import Flask, render_template, url_for, request
from flask import jsonify
import section_plot
import ast
from flask_cors import CORS, cross_origin
# from tweepyfunc import word_of_interest, analize_sentiment, clean_tweets, pull_tweets
# import pandas as pd
# import numpy as np




app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
def index2():
    if request.method == 'GET':
        return "\n\n<style>\n\n</style>\n\n<div id=\"fig_el4131446767698889328338567\"></div>\n<script>\nfunction mpld3_load_lib(url, callback){\n  var s = document.createElement('script');\n  s.src = url;\n  s.async = true;\n  s.onreadystatechange = s.onload = callback;\n  s.onerror = function(){console.warn(\"failed to load library \" + url);};\n  document.getElementsByTagName(\"head\")[0].appendChild(s);\n}\n\nif(typeof(mpld3) !== \"undefined\" && mpld3._mpld3IsLoaded){\n   // already loaded: just create the figure\n   !function(mpld3){\n       \n       mpld3.draw_figure(\"fig_el4131446767698889328338567\", {\"height\": 480.0, \"plugins\": [{\"type\": \"reset\"}, {\"type\": \"zoom\", \"enabled\": false, \"button\": true}, {\"type\": \"boxzoom\", \"enabled\": false, \"button\": true}], \"width\": 640.0, \"data\": {\"data03\": [[0.0, 0.0]], \"data01\": [[80.0, 163.6273504273504], [576.0, 163.6273504273504]], \"data02\": [[334.35897435897436, 52.8], [334.35897435897436, 422.4]]}, \"id\": \"el413144676769888\", \"axes\": [{\"lines\": [{\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data01\", \"id\": \"el413144677426872\"}, {\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data02\", \"id\": \"el413144677454256\"}], \"xdomain\": [0.0, 1.9500000000000002], \"texts\": [], \"collections\": [{\"xindex\": 0, \"offsets\": \"data03\", \"edgecolors\": [\"#BF00BF\"], \"zorder\": 1, \"edgewidths\": [1.0], \"alphas\": [null], \"paths\": [[[[0.5, 0.0], [1.5, 0.0], [1.5, 0.3], [0.5, 0.3]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.85, 0.3], [1.15, 0.3], [1.15, 2.0], [0.85, 2.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]]], \"id\": \"el413144677455544\", \"pathcoordinates\": \"data\", \"yindex\": 1, \"offsetcoordinates\": \"display\", \"pathtransforms\": [], \"facecolors\": []}], \"markers\": [], \"images\": [], \"xscale\": \"linear\", \"bbox\": [0.125, 0.10999999999999999, 0.775, 0.77], \"ylim\": [0.0, 2.6], \"sharex\": [], \"sharey\": [], \"paths\": [], \"axesbg\": \"#FFFFFF\", \"axesbgalpha\": null, \"id\": \"el413144677308088\", \"xlim\": [0.0, 1.9500000000000002], \"yscale\": \"linear\", \"ydomain\": [0.0, 2.6], \"zoomable\": true, \"axes\": [{\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"bottom\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 9, \"tickformat\": null}, {\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"left\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 7, \"tickformat\": null}]}]});\n   }(mpld3);\n}else if(typeof define === \"function\" && define.amd){\n   // require.js is available: use it to load d3/mpld3\n   require.config({paths: {d3: \"https://mpld3.github.io/js/d3.v3.min\"}});\n   require([\"d3\"], function(d3){\n      window.d3 = d3;\n      mpld3_load_lib(\"https://mpld3.github.io/js/mpld3.v0.3.js\", function(){\n         \n         mpld3.draw_figure(\"fig_el4131446767698889328338567\", {\"height\": 480.0, \"plugins\": [{\"type\": \"reset\"}, {\"type\": \"zoom\", \"enabled\": false, \"button\": true}, {\"type\": \"boxzoom\", \"enabled\": false, \"button\": true}], \"width\": 640.0, \"data\": {\"data03\": [[0.0, 0.0]], \"data01\": [[80.0, 163.6273504273504], [576.0, 163.6273504273504]], \"data02\": [[334.35897435897436, 52.8], [334.35897435897436, 422.4]]}, \"id\": \"el413144676769888\", \"axes\": [{\"lines\": [{\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data01\", \"id\": \"el413144677426872\"}, {\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data02\", \"id\": \"el413144677454256\"}], \"xdomain\": [0.0, 1.9500000000000002], \"texts\": [], \"collections\": [{\"xindex\": 0, \"offsets\": \"data03\", \"edgecolors\": [\"#BF00BF\"], \"zorder\": 1, \"edgewidths\": [1.0], \"alphas\": [null], \"paths\": [[[[0.5, 0.0], [1.5, 0.0], [1.5, 0.3], [0.5, 0.3]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.85, 0.3], [1.15, 0.3], [1.15, 2.0], [0.85, 2.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]]], \"id\": \"el413144677455544\", \"pathcoordinates\": \"data\", \"yindex\": 1, \"offsetcoordinates\": \"display\", \"pathtransforms\": [], \"facecolors\": []}], \"markers\": [], \"images\": [], \"xscale\": \"linear\", \"bbox\": [0.125, 0.10999999999999999, 0.775, 0.77], \"ylim\": [0.0, 2.6], \"sharex\": [], \"sharey\": [], \"paths\": [], \"axesbg\": \"#FFFFFF\", \"axesbgalpha\": null, \"id\": \"el413144677308088\", \"xlim\": [0.0, 1.9500000000000002], \"yscale\": \"linear\", \"ydomain\": [0.0, 2.6], \"zoomable\": true, \"axes\": [{\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"bottom\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 9, \"tickformat\": null}, {\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"left\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 7, \"tickformat\": null}]}]});\n      });\n    });\n}else{\n    // require.js not available: dynamically load d3 & mpld3\n    mpld3_load_lib(\"https://mpld3.github.io/js/d3.v3.min.js\", function(){\n         mpld3_load_lib(\"https://mpld3.github.io/js/mpld3.v0.3.js\", function(){\n                 \n                 mpld3.draw_figure(\"fig_el4131446767698889328338567\", {\"height\": 480.0, \"plugins\": [{\"type\": \"reset\"}, {\"type\": \"zoom\", \"enabled\": false, \"button\": true}, {\"type\": \"boxzoom\", \"enabled\": false, \"button\": true}], \"width\": 640.0, \"data\": {\"data03\": [[0.0, 0.0]], \"data01\": [[80.0, 163.6273504273504], [576.0, 163.6273504273504]], \"data02\": [[334.35897435897436, 52.8], [334.35897435897436, 422.4]]}, \"id\": \"el413144676769888\", \"axes\": [{\"lines\": [{\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data01\", \"id\": \"el413144677426872\"}, {\"xindex\": 0, \"color\": \"#FF0000\", \"linewidth\": 1.5, \"coordinates\": \"display\", \"drawstyle\": \"default\", \"zorder\": 2, \"dasharray\": \"none\", \"alpha\": 1, \"yindex\": 1, \"data\": \"data02\", \"id\": \"el413144677454256\"}], \"xdomain\": [0.0, 1.9500000000000002], \"texts\": [], \"collections\": [{\"xindex\": 0, \"offsets\": \"data03\", \"edgecolors\": [\"#BF00BF\"], \"zorder\": 1, \"edgewidths\": [1.0], \"alphas\": [null], \"paths\": [[[[0.5, 0.0], [1.5, 0.0], [1.5, 0.3], [0.5, 0.3]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.85, 0.3], [1.15, 0.3], [1.15, 2.0], [0.85, 2.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]], [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [\"M\", \"L\", \"L\", \"L\", \"Z\"]]], \"id\": \"el413144677455544\", \"pathcoordinates\": \"data\", \"yindex\": 1, \"offsetcoordinates\": \"display\", \"pathtransforms\": [], \"facecolors\": []}], \"markers\": [], \"images\": [], \"xscale\": \"linear\", \"bbox\": [0.125, 0.10999999999999999, 0.775, 0.77], \"ylim\": [0.0, 2.6], \"sharex\": [], \"sharey\": [], \"paths\": [], \"axesbg\": \"#FFFFFF\", \"axesbgalpha\": null, \"id\": \"el413144677308088\", \"xlim\": [0.0, 1.9500000000000002], \"yscale\": \"linear\", \"ydomain\": [0.0, 2.6], \"zoomable\": true, \"axes\": [{\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"bottom\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 9, \"tickformat\": null}, {\"visible\": true, \"tickvalues\": null, \"scale\": \"linear\", \"position\": \"left\", \"fontsize\": 10.0, \"grid\": {\"gridOn\": false}, \"nticks\": 7, \"tickformat\": null}]}]});\n            })\n         });\n}\n</script>"

    if request.method == 'POST':
        section1 = request.form['section1']
        section2 = request.form['section2']
        section3 = request.form['section3']
        section4 = request.form['section4']
        section5 = request.form['section5']
        section6 = request.form['section6']
        section7 = request.form['section7']
        section8 = request.form['section8']
        data = [ast.literal_eval(section1), ast.literal_eval(section2), ast.literal_eval(section3),
                ast.literal_eval(section4), ast.literal_eval(section5), ast.literal_eval(section6),
                ast.literal_eval(section7), ast.literal_eval(section8)]
        result = section_plot.initializeAnalysis(data)
        # return json.dumps(result)
        return jsonify(result)

# @app.route('/tweepyapp', methods=['POST'])
# def index2():
#
#     if request.method == 'POST':
#
#         if 'twitter_handle' in request.form:
#             handle = request.form['twitter_handle']
#             num_results = request.form['num_results']
#             twitter_method = request.form.getlist("twitter_method")
#
#             data = pull_tweets(handle)
#             if type(data) == str:
#                 table_true = 2
#                 return render_template('index2.html', table_op=str(table_true), handle=handle, data_str=data)
#             else:
#                 data.reset_index(drop=True, inplace=True)
#                 rows = len(data)
#                 tokened = []
#                 for row in range(rows):
#                     word_list = clean_tweets(data.loc[row, 'Tweets'])
#                     tokened.append(word_list)
#                 data['Tweets_clean'] = pd.Series(tokened)
#
#                 if twitter_method[0] == 'option1':
#                     data_final = data[['Tweets', 'ID', 'Date', 'Tweets_clean']][:int(num_results)]
#
#                 if twitter_method[0] == 'option2':
#                     data['Tweet_str'] = data['Tweets_clean'].apply(lambda x: ' '.join(x))
#                     data['SA'] = np.array([analize_sentiment(tweet) for tweet in data['Tweet_str']])
#
#                     tweets_pos = []
#                     data.reset_index(drop=True,inplace=True)
#                     for row in range(len(data)):
#                         if data.loc[row, 'SA'] < -.5:
#                             tweets_pos.append(row)
#                     data_final = data.iloc[tweets_pos, :][['Tweets', 'ID', 'Date', 'Tweets_clean']]
#                     data_final.reset_index(drop=True,inplace=True)
#                 word_search = "none"
#
#         if 'twitter_hand' in request.form:
#             handle = request.form['twitter_hand']
#             word_search = request.form['word_search']
#
#             data = pull_tweets(handle)
#
#             if type(data) == str:
#                 table_true = 2
#                 return render_template('index2.html', table_op=str(table_true), handle=handle, data_str=data)
#             else:
#                 data.reset_index(drop=True, inplace=True)
#                 rows = len(data)
#                 tokened = []
#                 for row in range(rows):
#                     word_list = clean_tweets(data.loc[row, 'Tweets'])
#                     tokened.append(word_list)
#                 data['Tweets_clean'] = pd.Series(tokened)
#
#                 data_final = word_of_interest(data, word_search)
#
#         if len(data_final) > 0:
#             table_true = 1
#         else:
#             table_true = 0
#
#
#         return render_template('index2.html', table_op=str(table_true),
#                                data=data_final.to_html(classes="table table-striped"), handle=handle,
#                                word_search=word_search)



if __name__ == '__main__':
    app.run()
