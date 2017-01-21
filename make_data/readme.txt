データ仕様                       2017.01.21 create


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
             詳細は、サンプルデータ sample_data/cate.json 参照

list.json … サブカテゴリ内のデータ一覧
             今回の要件は、営業時間内でかつ近隣のデータをモバイル側で
　　　　　　 マッチングを行うため、必要最低限のデータ（緯度経度、営業時間）
             だけでリスト化
             詳細は、サンプルデータ sample_data/onsen/ashiyu/list.json を参照

attribute.json … detail.json の属性を規定。
             詳細は、サンプルデータ sample_data/onsen/ashiyu/attribute.json
             
detail.json … 1物件の詳細情報を格納
             attribute.jsonに対応したカラムで作成
             詳細は、サンプルデータ sample_data/onsen/ashiyu/00001/detail.json
 

■３．手入力用excel仕様＊＊＊＊＊＊＊＊＊＊現在検討中
(1) サブカテゴリごとにexcelシートを作成
      1行目にフィールドkeyを並べる。name tel time　・・・。a-z列に必須項目。aa列からは、専用項目を並べる。
      2行名にkeyに対するnameを並べる。名称 電話 営業時間・・・
      3行目にkeyに対するattributeを並べる。text text text ・・・
タイトル, それ以降データ
      4行目移行を、データ部とする

  ＊営業時間は、検索条件になるので解析しやすくするように配列化が必要。例えば以下のような文字列をexcelにどう分けて、入力するか検討。
      8:30-22:30、砂湯8:00-受付21:30

＊＊＊
仕様がまとまり次第、excelで数行の簡単なサンプルを作成します。
実際のデータはどなたかに作成していただきたく思います。




■４．excelデータの変換プログラム仕様＊＊＊＊＊＊＊＊＊＊現在検討中

excelデータを1の階層的なURLと2のjsonに変換するプログラム。

excelデータをutf-8でcsvに落としたものを入力とし、
パイソンかシェルスクリプトで開発予定です。



