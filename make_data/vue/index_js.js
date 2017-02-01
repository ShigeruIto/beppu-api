
var root_path = "/../data";
var cates = file_json(root_path + "/cate.json");

// 
var app_catemenu = new Vue({
  el: '#catemenu',
  data: {
    cates: cates,
    subs: [],
    lists: [],
    detail: {},
    cate: {},
    sub: {},
    list: {}
  },
  methods: {
    cateclick: function (cate) {	// カテゴリボタンが押された
      this.cate=cate;
      this.subs=cate.sub;
      this.lists=[];
      this.detail={};
    },
    subclick: function (sub) {	         // サブカテゴリボタンが押された
      this.sub=sub;
      this.lists=file_json( root_path + "/" + this.cate.path + "/" + this.sub.path + "/" + "list.json");
      this.detail={};
    },
    listclick: function (list) {	         // リスト中の１つのボタンが押された
      this.list=list;
      this.detail=file_json( root_path + "/" + this.cate.path + "/" + this.sub.path + "/" + this.list.path + "/" + "detail.json");
      window.open("./detail.html?path=" + root_path + "/" + this.cate.path + "/" + this.sub.path + "/" + this.list.path , "new1", "width=800,height=800,resizable=no,scrollbars=no");
    },
    thumburl: function (list) {		// サムネイルURL取得
      return root_path + "/" + this.cate.path + "/" + this.sub.path + "/" + list.thumbnail;
    },
    getopen: function (list) {		// オープン時間を文字列にする
      m="";
      for(o of list.open){
         if(m!="") m=m+"|";
         if(o.message!="") m = m + o.message + "=";
         if(o.stime=="0:00" && o.etime=="0:00") m = m + "終日";
         else m = m + o.stime + "-" + o.etime;
      }
      return m;
    }
  }
})
