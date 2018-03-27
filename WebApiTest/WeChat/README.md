# WeChat MenuAPi

文档说明：

1.后台菜单管理添加一、二级菜单未做限制

2./menu?type=1 接口按照微信菜单最大数限制处理

3.数据库限制字符长度为100，程序前后端未限制



字段说明：

1.button 一级菜单 必须 1-3个

2.sub_button 二级菜单 非必须 1-5个

3.type 类型 必须 常用可选类型click,view,media_id,view_limited

4.name 必须 菜单标题 不超过16个字节

5.key 非必须 click类型必须 不超过128个字节

6.url 非必须 view类型必须 不超过1024字节

7.media_id 非必须 media_id与view_limited类型必须 调用新增永久素材接口返回的合法media_id
