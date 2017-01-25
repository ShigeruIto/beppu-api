# coding=utf-8
import os
import os.path
import shutil
import json
import glob

# global
head = {}
hkey = []
hname = []
hattr = []

# detailの属性ごとのjson作成
def make(key, attr, value):
	if( attr == "times" or attr == "infos" ):		# times属性と、infos属性だけは、さらにコレクション化
		x = {key:[]}
		for n in value.split('|'):
			p={}
			for m in n.split(','):
				s=m.split("=")
				if(len(s)==2):				# key=value の形になっているときのみ登録
					p.update({s[0]:s[1]});
			x[key].append(p);
		print x
	else:
		x = {key:value}					# text属性などは、そのまま設定
	return x

# データ部
def decode_record(row):
	global head
	global hkey
	global hname
	global hattr
	d = {}
	c = row.split('\t')
	del c[0]
	i = 0
	for name in hname:
		if(name != ""):
			d.update(make(hkey[i], hattr[i], c[i]))
		i=i+1
	return d

# ヘッダ部
def decode_header(row, excel_row):
	global head
	global hname
	global hkey
	global hattr
	c = row.split('\t')
	del c[0]
	if(excel_row==1):			# Excel 1行目 カテゴリ、サブカテ
		head['cate_name'] = c[2-1]
		head['sub_name'] = c[6-1]
	elif(excel_row==2):			# Excel 2行目 カテゴリ、サブカテ(path)
		head['cate_path'] = c[2-1]
		head['sub_path'] = c[6-1]
	elif(excel_row==8):			# Excel 8行目
		hname = c
	elif(excel_row==9):			# Excel 9行目
		hkey = c
	elif(excel_row==10):			# Excel 10行目
		hattr = c

##########################################################
#
# main
#
##########################################################
input = "input"
tsv_files = glob.glob(input + "/*.tsv");	# excelからtsvに変換して保存したファイル取得。(excelではtxtで保存することでtsvになる。でもUTF-8で)
if(len(tsv_files)<=0):
	print "tsv file empty."
	exit(1)

root="data"					# データ作成パス
if(os.path.exists(root)):
	os.rmdir(root)				# 空のデータパスがあった場合削除
os.mkdir(root)

cate=[]
for file in tsv_files:
	# 当該カテゴリのdetail情報クリア
	details = []

	# tsv入力
	f = open(file, 'r')
	count=0
	line=0
	for row in f:
		# 改行削除
		row = row.replace('\r','')
		row = row.replace('\n','')
		# tsv 1行解析
		if( line < 10 ):
			decode_header(row, line+1)		# tsvのヘッダ部(～10行目)
		else:
			detail = decode_record(row)		# tsvのデータ部(11行目以降)
			details.append(detail)
		line=line+1
	# 1tsvファイル終了
	f.close()

	print head["cate_name"], head["sub_name"]
	# cate.json 追記
	key = head["cate_path"]
	i = 0
	for c in cate:
		if( c["path"] == key ):
			break;
		i=i+1
	if( i>=len(cate) ):					# 新規カテゴリ追加
		cate.append(0)
		cate[i] = {"name":head["cate_name"], "path":head["cate_path"], "sub":[]}
	cate[i]["sub"].append({"name" : head["sub_name"], "path" : head["sub_name"]});

	# ホルダ作成
	a = root + "/" + head["cate_path"]
	if(os.path.exists(a)==0):
		os.mkdir(a)
	a = a + "/" + head["sub_path"]
	os.mkdir(a)

	# attribute.json作成
	attribute=[]
	i=0
	for name in hname:
		if(name != ""):
			attribute.append({"key": hkey[i], "name": hname[i], "attribute": hattr[i]});
		i=i+1
	f = open(a + "/attribute.json", "w")
	json.dump(attribute, f, ensure_ascii=False)
	f.close();

	# list.json作成, detail.json出力
	idx = 10000	# detailホルダの開始番号
	lists = []
	for detail in details:
		# ディレクトリ作成
		b = a + "/" + str(idx)
		os.mkdir(b)

		# サムネイル出力
		jpg = detail["thumbnail"]
		inp_jpg = input + "/" + jpg
		if( jpg !="" and os.path.exists(inp_jpg) ):
			shutil.copy(inp_jpg, b + "/")
			detail["thumbnail"]=os.path.basename(jpg)	# thumbnail画像ファイル名だけにする

		# リスト作成
		lst = {
			"name":detail["name"],
			"open":detail["open"],
			"lat":detail["lat"],
			"lng":detail["lng"],
			"thumbnail": str(idx) + "/" + detail["thumbnail"],
			"path":str(idx)}
		lists.append(lst)

		# detailを出力
		f = open(b + "/detail.json", "w")
		json.dump(detail, f, ensure_ascii=False)
		f.close()

		idx = idx + 1

	# list.json出力
	f = open(a + "/list.json", "w")
	json.dump(lists, f, ensure_ascii=False)
	f.close();

# cate.json出力
f = open(root + "/cate.json", "w")
json.dump(cate, f, ensure_ascii=False)
f.close();
