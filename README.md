# pc_remote_android
PC通过USB/WIFI连接Android手机，远程控制手机执行相应的app操作。

## 安装
python3
uiautomator2
adbutils

## 设备类操作
1. 查找控件ID
```
private UiObject2 getRootParent(UiObject2 object2) {
        UiObject2 parent = object2.getParent();
        if (parent != null) {
            return getRootParent(parent);
        } else {
            return object2;
        }
    }

    private void printChildrenInfo(UiObject2 object2, int index) {
        String prefix = String.join("", Collections.nCopies(index, "-"));
        Log.d("ZXD", prefix + "ClassName:" + object2.getClassName() + ", ResourceName:" + object2.getResourceName() + ", Text:" + object2.getText());
        List<UiObject2> children = object2.getChildren();
        if (children != null) {
            index++;
            for (int i = 0; i < children.size(); i++) {
                printChildrenInfo(children.get(i), index);
            }
        }
    }

    @Test
    public void printParent() {
        UiDevice device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
        UiObject2 targetView = device.findObject(By.text("说点什么..."));

        UiObject2 rootView = getRootParent(targetView);
        printChildrenInfo(rootView, 0);
    }
```


### 抖音
* 包名 com.ss.android.ugc.aweme

操作：
1. 启动应用，包括自动点掉一些弹窗 
* launch
2. 搜索 用户/直播
* find_user
* find_live
3. 用户 关注/分享/私信/举报/拉黑
4. 作品 浏览/点赞/评论/收藏/分享
5. 直播 弹幕/礼物/粉丝团/点赞


#### 目前进度
1. 打开关闭抖音 --- 已完成
2. 搜索指定用户/直播间 --- 已完成
3. 直播间发弹幕 --- 已完成
4. 直播间送礼物 --- 未
5. 直播间点赞 --- 未
6. 直播间粉丝 --- 未
7. 退出直播间 --- 已完成

后续 主要是直播间刷礼物  礼物类型/礼物分页/礼物号
直播间点赞 目前没有找到连续点击的方法
直播间人数， 这个有必要么
直播间目前内容主要这么多 看看直播鸭是还有哪些内容

管理后台那一部分还是有很多内容的 这部分考虑自己做还是找人