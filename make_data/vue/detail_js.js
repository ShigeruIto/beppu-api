
var path = decodeURIComponent(location.search.match(/path=(.*?)(&|$)/)[1]);
var detail = file_json(path + "/detail.json");
var attr = file_json(path + "/../attribute.json");

// 属性によって表示方法を使い分ける
function gethtml(value, attr){
  m = "";
  if(attr.attribute=="bool"){
    if(value=="") m="不明";
    else if(value) m="〇";
    else m="×";
  }
  else if(attr.attribute=="infos"){
     bef = "";
     for(k in value){
       v=value[k];
       if('route' in v){	// バス停データか？
         if(m!="") m=m+"<br>";
         if(bef!=v.company){
           if(bef!="") m = m + "<br>";
           m = m + "<b>" + v.company + "</b><br>";
           bef=v.company;
         }
         m = m + "  ・" + v.route;
       }
     }
  }
  else {
    m = value;
  }
  return m;
}

// 
var app_detail = new Vue({
  el: '#detailmenu',
  data: {
    detail: detail
  },
  methods: {
    detail_maker: function() {
      m = "";
      m = m + "<table border=1 style='border-collapse: collapse;'>";
      for(a of attr){
	// detailのkey取得
	k = a.key;
	// detail.value取得
	v = detail[k];
        // skip attr
        if(k=="thumbnail" || k=="lat" || k=="lng" || k=="open" || k=="address" || k=="closingday") continue;
	if(k!=""){
          m = m + "<tr>";
          m = m + "  <td>" + a.name + "</td>";
          m = m + "  <td>" + gethtml(v, a) + "</td>";
          m = m + "</tr>";
	}
      }
      // 画像
      k="thumbnail";v=detail[k];
      if(k!="" && v!=""){
        m = m + "<tr>";
        m = m + "  <td>画像</td>";
        m = m + "  <td><img src=" + path + "/" + v + "></img></td>";
        m = m + "</tr>";
      }
      // 地図
      if(1){
        addr = detail['address'];
        if(addr=="") addr="GoogleMap表示";
        m = m + "<tr>";
        m = m + "  <td>地図表示</td>";
        m = m + "  <td><a href='http://maps.google.com/maps?q=" + detail['lat'] + "," + detail['lng'] + "'>" + addr + "</a></td>";
        m = m + "</tr>";
      }
      // 時間帯
      if(1){
        m = m + "<tr>";
        m = m + "  <td>時間帯</td>";
        //m = m + "  <td>" + opentime(detail['open'], "<br>") + "</td>";
        m = m + "  <td><table>";
        v = detail['open'];
	for(tk in v){
          tv = v[tk];
          m = m + "    <tr>";
          if( tv.stime=="0:00" && tv.etime=="0:00" ){
            m = m + "      <td> 終日（または不明） </td>";
          } else {
            m = m + "      <td>" + tv.stime + "-" + tv.etime + "</td>";
          }
          m = m + "      <td>" + tv.message + "</td>";
          m = m + "    </tr>";
	}
        closingday=detail['closingday']; // 定休日
        if(closingday!=""){
          m = m + "    <tr><td>定休日</td><td><b>" + closingday + "</b></td></tr>";
        }
        m = m + "  </table></td>";
        m = m + "</tr>";
      }
      // finish
      m = m + "</table>";
      return m;
    }
  }
})
