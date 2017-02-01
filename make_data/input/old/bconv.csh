#!/bin/csh
# なかやまさんのデータを、バス停ごとに、バス会社＋路線で集計

cat busstop_route.utf-8.tsv | awk '{if(NR>10){print $0;}}' | sort -t'	' -k2 -k27 -k30 -k31 | awk -F'\t' '{key=$27; if($z!="" && b!=key) {print z "\t" e; e="";} if(e!="") e=e "|"; e=e "company=" $30 ",route=" $31; z="";for(i=1;i<NF;i++) {z = z $(i) "\t";} b=key} END{print z "\t" e;}'
