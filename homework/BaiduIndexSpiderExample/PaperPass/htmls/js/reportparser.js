function sentenceContent(e,r){var t=parseSentence(e[r%200]);var i=template("similar-template",t);$(".sentence-illustrate").hide();$(".logo_right").hide();$(".sentence-detail").html(i).show();if(typeof is_online_view==="undefined"||is_online_view==false){$(".xm-smart-rewrite").attr("href","https://www.xiaomo.com/reWrite")}$("body").scrollTop(0)}function parseSentence(e){var t=localCount=periodicalCount=degreeCount=conferenceCount=bookCount=netCount=otherCount=sbCount=0;var i=[];e.result.forEach(e=>{t++;var r={score:Math.round(e.score*100),similaritySegGreyList:e.similaritySegGreyList,originalSegGreyList:e.originalSegGreyList,similaritySentence:filterCharacter(e.similaritySentence),subSimilaritySentenceSection:filterCharacter(e.subSimilaritySentenceSection),simpleDetailJson:e.duplicateSourceMD5,articleType:e.articleType!="net"?e.articleType:"互联网",classification:e.classification,paperPassId:e.duplicateSourceMD5};if(r.articleType=="OpenSearch")r.articleType="自建库";if(e.classification=="local"||e.classification=="OpenSearch"){localCount++;switch(e.articleType){case"学术期刊":periodicalCount++;r.title=JSON.parse(simSource[e.duplicateSourceMD5]).title;r.simpleDetailJson=SentenceDetailParser.parsePeriodical(simSource[e.duplicateSourceMD5]);break;case"书籍数据":bookCount++;r.simpleDetailJson=SentenceDetailParser.parseBook(simSource[e.duplicateSourceMD5]);break;case"学位论文":degreeCount++;r.simpleDetailJson=SentenceDetailParser.parseThesis(simSource[e.duplicateSourceMD5]);break;case"学术会议":conferenceCount++;r.simpleDetailJson=SentenceDetailParser.parseConference(simSource[e.duplicateSourceMD5]);break;case"自建库":sbCount++;r.simpleDetailJson=SentenceDetailParser.parseSelfBuild(simSource[e.duplicateSourceMD5]);break;case"OpenSearch":sbCount++;r.simpleDetailJson=SentenceDetailParser.parseOpenSearch(simSource[e.duplicateSourceMD5]);break;case"大学生联合比对库":otherCount++;r.simpleDetailJson=SentenceDetailParser.parseUniversity();break}}else if(e.classification=="net"){netCount++;r.chuChu=JSON.parse(simSource[e.duplicateSourceMD5]).chuchu;r.title=JSON.parse(simSource[e.duplicateSourceMD5]).title}i.push(r)});if(t>0){var r={total:t,local:localCount,periodical:periodicalCount,degree:degreeCount,conference:conferenceCount,book:bookCount,net:netCount,sb:sbCount,other:otherCount,data:i,checkType:typeof check_type=="undefined"?"ultimate":check_type,isSelfBuild:typeof isSelfBuild=="undefined"?false:isSelfBuild,pid:Report.report_id}}r.content=filterCharacter(e.content);r.score=Math.round(e.result[0].score*100);if(e.result[0].score>=.4){r.synonymsContent=e.synonymsContent;r.segRedList=e.segRedList;r.newSegRedList=e.result[0].originalSegGreyList}return r}function wordsColor(e,c,r){var t="";var u=0;var l=false;var f=[];e.forEach(e=>{for(const o in e){if(Object.hasOwnProperty.call(e,o)){var r=e[o];var t=o;var i=t.length;var n=c.indexOf(t,u);if(n!==false&&n>=u){var s=n-u;if(s!=0){var a=c.substr(u,s);if(r=="1"&&l){f.push({s:a,c:true})}else{f.push({s:a,c:false})}u+=s}if(r=="1"){f.push({s:t,c:true});l=true}else{f.push({s:t,c:false});l=false}u+=i}}}});var i="";f.forEach(e=>{if(e["c"]){i=i+e["s"]}else{if(i!=""){t=t+r.replace("{%s}",i);i=""}t+=e["s"]}});if(i!=""){t=t+r.replace("{%s}",i)}return t}function subSimilaritySection(e,r){return e.replace(r,'<span class="g-font-color green">'+r+"</span>")}function filterCharacter(e){return e.replace(/[<>\&]/g,function(e){return"&#"+e.charCodeAt(0)+";"})}function scoreColor(e){if(e<40){return"green"}else if(e>=70){return"red"}else{return"orange"}}function synonymsContent(e){var e=e.split("\r\n");e.pop();var r="";e.filter(function(e){var e=e.split(":");r+='<li class="g-font-color green"><span class="g-font-color red">'+e[0]+" ： </span>"+e[1]+"</li>"});return r}function formatTitle(e){if(e.articleType=="大学生联合比对库"){return""}var r=e.paperPassId;var t="";var i="《"+e.title+"》";if(!r)return e.simpleDetailJson;if(e.articleType=="学术期刊"){t=getDocLink(e.articleType,r)}if(t){var n='<a href="'+t+'" target="_blank">'+i+'</a><a href="'+t+'" target="_blank" class="icon iconfont icon-tiaozhuan"></a>';e.simpleDetailJson=e.simpleDetailJson.replace(i,n)}return e.simpleDetailJson}function getDocLink(e,r){var t="";if(!r||r.length>=32){return t}if(e=="学术期刊"){t="https://doc.paperpass.com/journal/"+r+".html?utm_source=ppreport"}return t}function issetString(e){if(typeof e!=="undefined"&&e!=""){return true}else{return false}}function issetArray(e){if(typeof e!=="undefined"&&e.length!=0){return true}else{return false}}var SentenceDetailParser={parsePeriodical:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.title)){r+='<div class="source-detail-title"><b>篇名：</b><span>《'+e.title+"》</span></div>"}if(issetArray(e.author)){r+="<b>作者：</b>"+e.author.toString()+"<br>"}if(issetString(e.chuchu)){r+="<b>期刊名称：</b>"+e.chuchu+"<br>"}if(issetString(e.year)){r+="<b>出版日期：</b>"+e.year+"年";if(issetString(e.issue)){r+=e.issue+"期"}r+="<br>"}if(issetString(e.column)){r+="<b>期刊栏目：</b>"+e.column+"<br>"}if(issetString(e.page)){r+="<b>页码：</b>"+e.page+"<br>"}if(issetString(e.pageNum)){r+="<b>页数：</b>"+e.pageNum+"页<br>"}if(issetString(e.cLCNumber)){r+="<b>分类号：</b>"+e.cLCNumber+"<br>"}if(issetArray(e.fundInfo)){r+="<b>基金项目：</b>"+e.fundInfo.toString()+"<br>"}if(issetString(e.publicationDate)){r+="<b>出版时间：</b>"+e.publicationDate+"<br>"}var t=[];if(!(typeof e.isCoreISTIC=="undefined")&&e.isCoreISTIC==1){t.push("ISTIC")}if(!(typeof e.isCoreNJU=="undefined")&&e.isCoreNJU==1){t.push("CSSCI")}if(!(typeof e.isCorePKU=="undefined")&&e.isCorePKU==1){t.push("PKU")}if(!(typeof e.isCoreSCI=="undefined")&&e.isCoreSCI==1){t.push("SCI")}if(!(typeof e.isCoreEI=="undefined")&&e.isCoreEI==1){t.push("EI")}if(t.length!=0){r+="<b>期刊级别：</b>"+t.toString()+"<br>"}if(issetString(e.iSSN)){r+="<b>ISSN：</b>"+e.iSSN+"<br>"}return r}},parseThesis:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.title)){r+="<b>篇名：</b>《"+e.title+"》"+"<br>"}if(issetArray(e.author)){r+="<b>作者：</b>"+e.author.toString()+"<br>"}if(issetString(e.chuchu)){r+="<b>授予单位：</b>"+e.chuchu+"<br>"}if(issetString(e.year)){r+="<b>学位年度：</b>"+e.year+"<br>"}if(issetString(e.degree)){r+="<b>授予学位：</b>"+e.degree+"<br>"}if(issetString(e.cLCNumber)){r+="<b>分类号：</b>"+e.cLCNumber+"<br>"}if(issetArray(e.authorSubject)){r+="<b>学科专业：</b>"+e.authorSubject+"<br>"}if(issetArray(e.teacherName)){r+="<b>导师姓名：</b>"+e.teacherName.toString()+"<br>"}return r}},parseConference:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.title)){r+="<b>篇名：</b>《"+e.title+"》"+"<br>"}if(issetArray(e.author)){r+="<b>作者：</b>"+e.author.toString()+"<br>"}if(issetString(e.conference)){r+="<b>会议名称：</b>"+e.conference+"<br>"}if(issetArray(e.convener)){r+="<b>主办单位：</b>"+e.convener.toString()+"<br>"}if(issetString(e.conferenceDate)){r+="<b>会议时间：</b>"+e.conferenceDate+"<br>"}if(issetString(e.conferenceLocus)){r+="<b>会议地点：</b>"+e.conferenceLocus+"<br>"}return r}},parseBook:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.category)){r+="<b>章节：</b>"+e.category+"<br>"}if(issetString(e.title)){r+="<b>书名：</b>《"+e.title+"》<br>"}if(issetArray(e.author)){r+="<b>作者：</b>"+e.author.toString()+"<br>"}if(issetString(e.publisher)){r+="<b>出版社：</b>"+e.publisher+"<br>"}if(issetString(e.publicationDate)){r+="<b>出版时间：</b>"+e.publicationDate+"<br>"}if(issetString(e.iSBN)){r+="<b>ISBN：</b>"+e.iSBN+"<br>"}return r}},parseSelfBuild:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.title)){r+="<b>篇名：</b>《"+e.title+"》<br>"}if(issetArray(e.author)){r+="<b>作者：</b>"+e.author.toString()+"<br>"}if(issetString(e.publicationDate)){r+="<b>发表时间：</b>"+e.publicationDate+"<br>"}if(issetArray(e.chuchu)){r+="<b>出处：</b>"+e.chuchu+"<br>"}return r}},parseOpenSearch:function(e){if(issetString(e)){var r="";e=JSON.parse(e);if(issetString(e.title)){r+="<b>篇名：</b>《"+e.title+"》<br>"}if(issetString(e.contentLengthString)){r+="<b>长度：</b>"+e.contentLengthString+"<br>"}if(issetString(e.publicationDate)){r+="<b>上传时间：</b>"+e.publicationDate+"<br>"}if(issetArray(e.chuchu)){r+="<b>出处：</b>自建库["+e.chuchu+"]<br>"}return r}},parseUniversity:function(){res="<b>来源：</b>大学生联合比对库<br>";return res}};