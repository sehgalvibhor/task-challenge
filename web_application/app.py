from flask import Flask,Response, request, render_template, redirect, flash, url_for, g, session, jsonify, make_response
#from flask_restful import Resource, Api
from json import dumps
import os
import csv
import json
import urlparse
from flask_restful import Resource, Api
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
api = Api(app)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
	database=url.path[1:],
	user=url.username,
	password=url.password,
	host=url.hostname,
	port=url.port
)

cur = conn.cursor(cursor_factory=RealDictCursor)


'''
@app.route('/ajax')
def ajax() :
	data_d3 = {}
	data_d3["name"] = "Youtube"
	data_d3["img"] = "https://www.youtube.com/yt/brand/media/image/YouTube-logo-full_color.png"
	data_d3["children"] = []
	with open('static/data/graph.csv','rb') as csvfile:
		csvreader = csv.reader(csvfile,dialect='excel')
		for row in csvreader:
			child = {}
			child["name"] = row[2]
			child["img"] = row[3]
			child["size"] = 40000
			child["id"] = row[0]
			data_d3["children"].append(child)
	return Response(json.dumps(data_d3), mimetype='application/json')
'''

class channel_list(Resource):
	def get(self):
		query = cur.execute("select distinct channelId,channelTitle from vis_db;" )
		rec = cur.fetchall()
		return rec

class channel_details(Resource):
	def get(self,client):
		query = cur.execute("select distinct channel_videoCount::integer,channel_subscriberCount::integer,channel_viewCount::integer,channel_commentCount::integer	from vis_db where channelId='"+str(client)+"';" )
		rec = cur.fetchall()
		return rec


@app.route('/')
def index():
	return render_template('home.html')



api.add_resource(channel_list, '/channel_list')
api.add_resource(channel_details, '/channel_details/<string:client>')

if __name__ == '__main__':
	app.run(debug=True)