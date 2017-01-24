データ仕様                       2017.01.21 create
                                 2017.01.24 update


■１．URL仕様

url_root/
   cate.json
   <カテゴリ1>/
     <サブカテ1>/
       list.json
       <データ1>/
         detail.json
       <データ2>/
         detail.json
          :
     <サブカテ2>/
       list.json
     <サブカテ3>/
       list.json
           :
   <カテゴリ2>/
            :




■２．json仕様
cate.json … カテゴリ･サブカテゴリ一覧
             x 手打ちサンプルデータは、 sample_data/cate.json 参照
             o 自動作成データは、data/cate.json 参照

list.json … サブカテゴリ内のデータ一覧
             今回の要件は、営業時間内でかつ近隣のデータをモバイル側で
　　　　　　 マッチングを行うため、必要最低限のデータ（緯度経度、営業時間）
             だけでリスト化
             x 手打ちサンプルデータは、sample_data/onsen/ashiyu/list.json を参照
             o 自動作成データは、data/spa/beppuall/list.json を参照

attribute.json … detail.json の属性を規定。
             x 手打ちサンプルデータは sample_data/onsen/ashiyu/attribute.json
             o 自動作成サンプルデータは data/spa/beppuall/attribute.json
             
detail.json … 1物件の詳細情報を格納
             attribute.jsonに対応したカラムで作成
             x 手打ちサンプルデータ sample_data/onsen/ashiyu/00001/detail.json
             o 自動作成サンプルデータは data/spa/beppuall/10000/detail.json

* 各jsonの"path"を連結することで、目的のデータのパスを生成。
   例）detail.jsonは、cate.jsonの"path" + cate.jsonの"sub/path" + list.jsonの"path"
 

■３．手入力用excel仕様
(1) サブカテゴリごとにexcelシートを作成

  詳細は、input/beppu_apiデータ入力用.xlsx の「表紙」シート参照



■４．excelデータの変換プログラム仕様

excelデータを1の階層的なURLと2のjsonに変換するプログラム。

excelデータをutf-8でcsvに落としたものを入力とし、パイソンで開発です。


実行手順：
　・excelデータをサブカテゴリシートごとに、tsvに落とす(utf-8)。
  ./make_data.py を実行すると、inputの下にある全てのtsvを変換して、dataの下に作成される


