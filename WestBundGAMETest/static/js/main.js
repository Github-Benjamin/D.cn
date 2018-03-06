/**
 * Created by admin on 2017/12/20.
 */
// ifame框架打开页面
var openpage = function (href) {
    $(".addpage").empty();
    var html = '<iframe id="iframe-page-content" src="'+href+'" width="100%"  frameborder="no" border="0" marginwidth="0" marginheight=" 0" scrolling="no" allowtransparency="yes"></iframe>'
    $(".addpage").append(html);
    var ifm= document.getElementById("iframe-page-content");
    ifm.height=document.documentElement.clientHeight;
}

//加载ifame框架
$(".addmeu").click(function(){
    var href= $(this).attr("data-href");
    openpage(href);
});