window.__require = function e(t, n, a) {
    function r(i, s) {
        if (!n[i]) {
            if (!t[i]) {
                var u = i.split("/");
                if (u = u[u.length - 1],
                !t[u]) {
                    var c = "function" == typeof __require && __require;
                    if (!s && c)
                        return c(u, !0);
                    if (o)
                        return o(u, !0);
                    throw new Error("Cannot find module '" + i + "'")
                }
                i = u
            }
            var l = n[i] = {
                exports: {}
            };
            t[i][0].call(l.exports, function(e) {
                return r(t[i][1][e] || e)
            }, l, l.exports, e, t, n, a)
        }
        return n[i].exports
    }
    for (var o = "function" == typeof __require && __require, i = 0; i < a.length; i++)
        r(a[i]);
    return r
}({
    App: [function(e, t, n) {
        "use strict";
        cc._RF.push(t, "59f26fFmM9GM7MJT2W+FLRV", "App");
        var a = this && this.__awaiter || function(e, t, n, a) {
            return new (n || (n = Promise))(function(r, o) {
                function i(e) {
                    try {
                        u(a.next(e))
                    } catch (t) {
                        o(t)
                    }
                }
                function s(e) {
                    try {
                        u(a.throw(e))
                    } catch (t) {
                        o(t)
                    }
                }
                function u(e) {
                    var t;
                    e.done ? r(e.value) : (t = e.value,
                    t instanceof n ? t : new n(function(e) {
                        e(t)
                    }
                    )).then(i, s)
                }
                u((a = a.apply(e, t || [])).next())
            }
            )
        }
          , r = this && this.__generator || function(e, t) {
            var n, a, r, o, i = {
                label: 0,
                sent: function() {
                    if (1 & r[0])
                        throw r[1];
                    return r[1]
                },
                trys: [],
                ops: []
            };
            return o = {
                next: s(0),
                throw: s(1),
                return: s(2)
            },
            "function" == typeof Symbol && (o[Symbol.iterator] = function() {
                return this
            }
            ),
            o;
            function s(e) {
                return function(t) {
                    return u([e, t])
                }
            }
            function u(o) {
                if (n)
                    throw new TypeError("Generator is already executing.");
                for (; i; )
                    try {
                        if (n = 1,
                        a && (r = 2 & o[0] ? a.return : o[0] ? a.throw || ((r = a.return) && r.call(a),
                        0) : a.next) && !(r = r.call(a, o[1])).done)
                            return r;
                        switch (a = 0,
                        r && (o = [2 & o[0], r.value]),
                        o[0]) {
                        case 0:
                        case 1:
                            r = o;
                            break;
                        case 4:
                            return i.label++,
                            {
                                value: o[1],
                                done: !1
                            };
                        case 5:
                            i.label++,
                            a = o[1],
                            o = [0];
                            continue;
                        case 7:
                            o = i.ops.pop(),
                            i.trys.pop();
                            continue;
                        default:
                            if (!(r = (r = i.trys).length > 0 && r[r.length - 1]) && (6 === o[0] || 2 === o[0])) {
                                i = 0;
                                continue
                            }
                            if (3 === o[0] && (!r || o[1] > r[0] && o[1] < r[3])) {
                                i.label = o[1];
                                break
                            }
                            if (6 === o[0] && i.label < r[1]) {
                                i.label = r[1],
                                r = o;
                                break
                            }
                            if (r && i.label < r[2]) {
                                i.label = r[2],
                                i.ops.push(o);
                                break
                            }
                            r[2] && i.ops.pop(),
                            i.trys.pop();
                            continue
                        }
                        o = t.call(e, i)
                    } catch (s) {
                        o = [6, s],
                        a = 0
                    } finally {
                        n = r = 0
                    }
                if (5 & o[0])
                    throw o[1];
                return {
                    value: o[0] ? o[1] : void 0,
                    done: !0
                }
            }
        }
        ;
        Object.defineProperty(n, "__esModule", {
            value: !0
        });
        var o = e("./ConstantGlobal")
          , i = e("./Data")
          , s = e("./Net");
        n.default = new (function() {
            function e() {}
            return e.prototype.initServerInfo = function() {
                var e = this;
                xysz.http.defaults.headers["content-type"] = "application/json",
                xysz.http.defaults.timeout = 1,
                "qiehuangdev.ioutu.cn" === location.hostname ? (xysz.http.defaults.baseURL = "https://devapi.xiaoyisz.com/qiehuang/",
                i.default.wxInfo.pagePathShare = "/packages/wm-cloud-h5-game/middlePage/index",
                i.default.wxInfo.pagePathAuth = "/packages/wm-cloud-h5-game/authorize/index",
                i.default.wxInfo.pageUrl = "https://qiehuangdev.ioutu.cn",
                i.default.shareImages = {
                    share_friend: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_friend.jpg",
                    share_help: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_help.jpg",
                    share_adventure: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_adventure.jpg"
                }) : (xysz.http.defaults.baseURL = "https://api.xiaoyisz.com/qiehuang/",
                i.default.wxInfo.pagePathShare = "/packages/wm-cloud-h5-game/middlePage/index",
                i.default.wxInfo.pagePathAuth = "/packages/wm-cloud-h5-game/authorize/index",
                i.default.wxInfo.pageUrl = "https://thekingoftomato.ioutu.cn",
                i.default.shareImages = {
                    share_friend: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_friend.jpg",
                    share_help: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_help.jpg",
                    share_adventure: "https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/share/share_adventure.jpg"
                }),
                xysz.http.setRequestInterceptor(function(e) {
                    return e.data || (e.data = {}),
                    e
                }),
                xysz.http.setResponseInterceptor(function(t) {
                    var n = t.data;
                    return 0 === n.code ? (console.log(t.path, n),
                    n) : 903 == n.code || 904 == n.code || 802 == n.code ? (e.reload(),
                    xysz.ui.showToast("\u7f51\u7edc\u5f02\u5e38\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5!"),
                    new Error("\u7f51\u7edc\u5f02\u5e38\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5!")) : 429 == n.code ? (xysz.ui.showToast("\u7f51\u7edc\u5f02\u5e38\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5"),
                    new Error("\u7f51\u7edc\u5f02\u5e38\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5")) : 504 == n.code || 499 == n.code ? new Error(n.code) : "timeout" == n.code ? (xysz.ui.showToast("\u7f51\u7edc\u8d85\u65f6\u5f02\u5e38"),
                    new Error("\u7f51\u7edc\u8d85\u65f6\u5f02\u5e38")) : (e.doWmErrCode(n),
                    xysz.ui.showToast("" + n.message),
                    new Error(n.message))
                })
            }
            ,
            e.prototype.reload = function() {
                return a(this, void 0, void 0, function() {
                    return r(this, function(e) {
                        switch (e.label) {
                        case 0:
                            return i.default.ServerTimestamp = null,
                            [3, 2];
                        case 1:
                            return e.sent(),
                            [3, 4];
                        case 2:
                            return i.default.wmInfo ? [4, s.default.common.thirdLogin({
                                appId: i.default.wmInfo.thirdAppId,
                                openId: i.default.wmInfo.openId,
                                wid: i.default.wmInfo.wid,
                                unionid: i.default.wmInfo.unionid
                            })] : [3, 4];
                        case 3:
                            e.sent(),
                            e.label = 4;
                        case 4:
                            return i.default.nextScene = "Plant",
                            cc.director.loadScene("Loading"),
                            [2]
                        }
                    })
                })
            }
            ,
            e.prototype.doWmErrCode = function(e) {
                switch (e.code) {
                case "1051000100001":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801100001";
                    break;
                case "1051010100004":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801100004";
                    break;
                case "1051010200003":
                case "1051020200003":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801200003";
                    break;
                case "1051120400001":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801400001";
                    break;
                case "1051220400007":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801400007";
                    break;
                case "900010010006001":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006001";
                    break;
                case "900010010006002":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006002";
                    break;
                case "900010010006003":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006003";
                    break;
                case "900010010006004":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006004";
                    break;
                case "900010010006005":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006005";
                    break;
                case "900010010006006":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006006";
                    break;
                case "900010010006007":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006007";
                    break;
                case "900010010006008":
                    e.message = "\u670d\u52a1\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5 \n \u9519\u8bef\u7801006008"
                }
            }
            ,
            e.prototype.initDebugView = function() {
                return a(this, void 0, void 0, function() {
                    var e;
                    return r(this, function(t) {
                        switch (t.label) {
                        case 0:
                            return [4, xysz.res.loadAsset("abGame", "prefab/UIDebug")];
                        case 1:
                            return e = t.sent(),
                            cc.game.addPersistRootNode(cc.instantiate(e)),
                            [2]
                        }
                    })
                })
            }
            ,
            e.prototype.initOnlineOperation = function() {
                return a(this, void 0, void 0, function() {
                    var e;
                    return r(this, function(t) {
                        switch (t.label) {
                        case 0:
                            return [4, s.default.common.getOperate("gameOperation")];
                        case 1:
                            return e = t.sent(),
                            i.default.gameOperation = JSON.parse(e.data || "{}"),
                            void 0 === i.default.gameOperation.sound && (i.default.gameOperation.sound = !0),
                            xysz.sound.setOnlineStatus(i.default.gameOperation.sound),
                            this.updateOnlineOperation(),
                            [2]
                        }
                    })
                })
            }
            ,
            e.prototype.updateOnlineOperation = function() {
                var e = JSON.stringify(i.default.gameOperation);
                s.default.common.setOperate("gameOperation", e)
            }
            ,
            e.prototype.initGuideSteps = function() {
                return a(this, void 0, void 0, function() {
                    var e, t, n;
                    return r(this, function(a) {
                        switch (a.label) {
                        case 0:
                            return e = i.default,
                            n = (t = JSON).parse,
                            [4, s.default.common.getOperate("guideSteps")];
                        case 1:
                            return e.guideSteps = n.apply(t, [a.sent().data]),
                            i.default.guideSteps || (i.default.guideSteps = []),
                            [2]
                        }
                    })
                })
            }
            ,
            e.prototype.checkIfGuideNewUser = function(e) {
                return a(this, void 0, void 0, function() {
                    return r(this, function(t) {
                        switch (t.label) {
                        case 0:
                            return i.default.guideSteps ? [3, 2] : [4, this.initGuideSteps()];
                        case 1:
                            t.sent(),
                            t.label = 2;
                        case 2:
                            return i.default.guideSteps.includes(e) ? (console.log("guideSteps false"),
                            [2, !1]) : (cc.log("refresGuidesteps"),
                            i.default.guideSteps.push(e),
                            [4, s.default.common.setOperate("guideSteps", JSON.stringify(i.default.guideSteps))]);
                        case 3:
                            return t.sent(),
                            console.log("guideSteps true"),
                            [2, !0]
                        }
                    })
                })
            }
            ,
            e.prototype.switchSound = function() {
                i.default.gameOperation.sound = !i.default.gameOperation.sound,
                xysz.sound.setOnlineStatus(i.default.gameOperation.sound),
                this.updateOnlineOperation()
            }
            ,
            e.prototype.initShareInfo = function() {
                return a(this, void 0, void 0, function() {
                    var e;
                    return r(this, function() {
                        return xysz.runtime === xysz.C_Runtime.program_wx && (e = {
                            data: {
                                type: "share",
                                data: {
                                    title: "\u5feb\u6765\u79cd\u756a\u8304\uff0c\u62a2\u5148\u8d62\u597d\u793c!",
                                    imageUrl: i.default.shareImages.share_friend,
                                    path: i.default.wxInfo.pageUrl
                                }
                            }
                        },
                        xysz.wx.web.postMessage(e)),
                        [2]
                    })
                })
            }
            ,
            e.prototype.gotoNextScene = function(e) {
                return a(this, void 0, void 0, function() {
                    var t, n;
                    return r(this, function(a) {
                        switch (a.label) {
                        case 0:
                            return cc.log("fromscene:", cc.director.getScene().name),
                            t = cc.director.getScene().name,
                            i.default.nextScene = e,
                            "Road" === i.default.nextScene || "Adventure" === i.default.nextScene || "Plant" === i.default.nextScene && !i.default.isFirstLogin ? "Road" !== i.default.nextScene ? [3, 3] : [4, xysz.res.loadAsset("abGame", "res/tp/road", cc.SpriteAtlas)] : [3, 4];
                        case 1:
                            return n = a.sent(),
                            [4, xysz.ui.addAtlas(n)];
                        case 2:
                            a.sent(),
                            a.label = 3;
                        case 3:
                            return cc.director.loadScene(i.default.nextScene, function() {
                                "Road" != t && "Adventure" != t || setTimeout(function() {
                                    cc.game.emit(o.E_Global.SwitchScene, t)
                                }, 1e3)
                            }),
                            [3, 5];
                        case 4:
                            cc.director.loadScene("Loading"),
                            a.label = 5;
                        case 5:
                            return [2]
                        }
                    })
                })
            }
            ,
            e.prototype.updateShareInfo = function(e) {
                void 0 === e && (e = {});
                var t = e.invitorId
                  , n = e.taskId
                  , a = e.buildingId
                  , r = {
                    activityTpId: xysz.saas.info.activityTpId,
                    activityId: xysz.query.activityId,
                    terminalType: xysz.query.terminalType,
                    edition: xysz.query.edition,
                    utm_campaign: "\u5206\u4eab\u9080\u8bf7",
                    utm_source: 5,
                    invitorId: t,
                    taskId: n,
                    buildingId: a,
                    random: Date.now()
                };
                if (xysz.runtime === xysz.C_Runtime.browser_wx)
                    r.shareType = "app_message",
                    wx.updateAppMessageShareData({
                        title: xysz.saas.game.otherPage.wechatSharing.defaultConfig.title,
                        desc: xysz.saas.game.otherPage.wechatSharing.defaultConfig.description.replace("[\u6635\u79f0]", i.default.userInfo.nickName),
                        link: "" + location.origin + location.pathname + "?" + xysz.tool.getSortedQuery(r),
                        imgUrl: xysz.saas.game.otherPage.wechatSharing.defaultConfig.imgAddr,
                        success: function() {
                            console.log("wx.updateAppMessageShareData-\u8bbe\u7f6e\u5206\u4eab\u6210\u529f"),
                            console.log("" + location.origin + location.pathname + "?" + xysz.tool.getSortedQuery(r))
                        }
                    }),
                    r.shareType = "timeline",
                    wx.updateTimelineShareData({
                        title: xysz.saas.game.otherPage.wechatSharing.defaultConfig.title,
                        link: "" + location.origin + location.pathname + "?" + xysz.tool.getSortedQuery(r),
                        imgUrl: xysz.saas.game.otherPage.wechatSharing.defaultConfig.imgAddr,
                        success: function() {
                            console.log("wx.updateTimelineShareData-\u8bbe\u7f6e\u5206\u4eab\u6210\u529f")
                        }
                    });
                else if (xysz.runtime === xysz.C_Runtime.program_wx) {
                    var o = {
                        data: {
                            type: "share",
                            data: {
                                title: "\u5feb\u6765\u79cd\u756a\u8304\uff0c\u62a2\u5148\u8d62\u597d\u793c!",
                                imageUrl: i.default.shareImages.share_friend,
                                path: i.default.wxInfo.pageUrl
                            }
                        }
                    };
                    xysz.wx.web.postMessage(o)
                }
            }
            ,
            e.prototype.refreshUnpackBg = function(e, t, n) {
                return a(this, void 0, void 0, function() {
                    return r(this, function(a) {
                        switch (a.label) {
                        case 0:
                            return xysz.ui.getSpriteFrame(n) ? [3, 2] : [4, xysz.ui.addInnerImage("abGame", t)];
                        case 1:
                            a.sent(),
                            a.label = 2;
                        case 2:
                            return e.getComponent(cc.Sprite) && (e.getComponent(cc.Sprite).spriteFrame = xysz.ui.getSpriteFrame(n)),
                            [2]
                        }
                    })
                })
            }
            ,
            e.prototype.miniProgramOpt = function(e, t, n) {
                "navigate" === e ? (n = n || {},
                console.log("opt:", xysz.tool.getSortedQuery(n)),
                xysz.wx.web.navigateTo({
                    url: t + "?" + xysz.tool.getSortedQuery(n)
                })) : "switch" === e && xysz.wx.web.switchTab({
                    url: t
                })
            }
            ,
            e.prototype.gotoMiniProgramPage = function(e) {
                cc.log("path:", i.default.wxInfo.pageUrl + "?" + xysz.tool.getSortedQuery(e.urlParams));
                var t = i.default.wxInfo.pagePathShare;
                "auth" == e.shareType && (t = i.default.wxInfo.pagePathAuth),
                this.miniProgramOpt("navigate", t, {
                    title: e.title,
                    imageUrl: e.imageUrl,
                    path: encodeURIComponent(i.default.wxInfo.pageUrl + "?" + xysz.tool.getSortedQuery(e.urlParams)),
                    type: e.shareType,
                    user: e.user,
                    phone: e.phone,
                    share_task_name: e.share_task_name,
                    url: encodeURIComponent(e.url),
                    utm_campaign: e.utm_campaign || null,
                    utm_source: e.utm_source || null,
                    utm_medium: e.utm_medium || null,
                    utm_term: e.utm_term || null,
                    utm_content: e.utm_content || null
                })
            }
            ,
            e.prototype.gotoMainPage = function() {
                xysz.wx.web.reLaunch({
                    url: "/pages/index/index"
                })
            }
            ,
            e.prototype.getTaskIdByType = function(e) {
                return a(this, void 0, void 0, function() {
                    return r(this, function(t) {
                        switch (t.label) {
                        case 0:
                            return i.default.taskList && i.default.taskList.length ? [3, 2] : [4, s.default.common.getTaskList()];
                        case 1:
                            t.sent(),
                            t.label = 2;
                        case 2:
                            return [2, i.default.taskList.find(function(t) {
                                return t.taskType == e
                            }) ? i.default.taskList.find(function(t) {
                                return t.taskType == e
                            }).taskId : ""]
                        }
                    })
                })
            }
            ,
            e.prototype.refreshRewardIcon = function(e, t) {
                return a(this, void 0, void 0, function() {
                    return r(this, function() {
                        switch (t) {
                        case 1:
                            e.spriteFrame = xysz.ui.getSpriteFrame("icon_tomato");
                            break;
                        case 2:
                            e.spriteFrame = xysz.ui.getSpriteFrame("icon_sunshine");
                            break;
                        case 3:
                            e.spriteFrame = xysz.ui.getSpriteFrame("icon_chance");
                            break;
                        case 5:
                            e.spriteFrame = xysz.ui.getSpriteFrame("icon_exp")
                        }
                        return [2]
                    })
                })
            }
            ,
            e.prototype.randomString = function(e) {
                void 0 === e && (e = 16);
                for (var t = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", n = t.length, a = "", r = 0; r < e; r++)
                    a += t.charAt(Math.floor(Math.random() * n));
                return a
            }
            ,
            e.prototype.createSignatureData = function() {
                return a(this, void 0, void 0, function() {
                    var e, t, n, a, o;
                    return r(this, function(r) {
                        switch (r.label) {
                        case 0:
                            return e = {
                                dev: {
                                    clientKey: "IfWu0xwXlWgqkIC7DWn20qpo6a30hXX6",
                                    clientSecret: "A4rHhUJfMjw2I5CODh5g40Ja1d3Yk1CH"
                                },
                                prod: {
                                    clientKey: "IfWu0xwXlWgqkIC7DWn20qpo6a30hXX6",
                                    clientSecret: "A4rHhUJfMjw2I5CODh5g40Ja1d3Yk1CH"
                                }
                            },
                            t = xysz.saas.getEnvByHostname(),
                            i.default.ServerTimestamp ? [3, 2] : [4, s.default.common.getTimestamp()];
                        case 1:
                            r.sent(),
                            setTimeout(function() {
                                i.default.ServerTimestamp = null
                            }, 19e3),
                            r.label = 2;
                        case 2:
                            return n = this.randomString(),
                            a = {
                                clientKey: e[t].clientKey,
                                clientSecret: e[t].clientSecret,
                                timestamp: i.default.ServerTimestamp,
                                nonce: n
                            },
                            o = xysz.tool.getSortedQuery(a),
                            [2, {
                                signature: xysz.encrypt.Md5.encode(o).toUpperCase(),
                                timestamp: i.default.ServerTimestamp,
                                clientKey: e[t].clientKey,
                                clientSecret: e[t].clientSecret,
                                nonce: n
                            }]
                        }
                    })
                })
            }
            ,
            e.prototype.assemblySignatureData = function(e) {
                return a(this, void 0, Promise, function() {
                    var t, n;
                    return r(this, function(a) {
                        switch (a.label) {
                        case 0:
                            return -1 === e.indexOf("?") ? e += "?" : -1 === e.indexOf("&") && (e += "&"),
                            [4, this.createSignatureData()];
                        case 1:
                            return t = a.sent(),
                            n = e.indexOf("?"),
                            [2, {
                                url: (e + (-1 !== n ? n === e.length - 1 ? "" : e.endsWith("&") ? "" : "&" : "?") + "timestamp=" + t.timestamp + "&nonce=" + t.nonce + "&signature=" + t.signature).replace(/&&/g, "&"),
                                config: {
                                    signature: t.signature,
                                    timestamp: t.timestamp,
                                    nonce: t.nonce
                                }
                            }]
                        }
                    })
                })
            }
            ,
            e.prototype.get = function(e, t) {
                return a(this, void 0, Promise, function() {
                    var n;
                    return r(this, function(a) {
                        switch (a.label) {
                        case 0:
                            return [4, this.assemblySignatureData(e)];
                        case 1:
                            return n = a.sent(),
                            cc.log("get:", e),
                            [2, xysz.http.get(n.url, t)]
                        }
                    })
                })
            }
            ,
            e.prototype.post = function(e, t, n) {
                return a(this, void 0, Promise, function() {
                    var a;
                    return r(this, function(r) {
                        switch (r.label) {
                        case 0:
                            return cc.log("post", e),
                            [4, this.assemblySignatureData(e)];
                        case 1:
                            return a = r.sent(),
                            [2, xysz.http.post(a.url, t, n)]
                        }
                    })
                })
            }
            ,
            e
        }()),
        cc._RF.pop()
    }
    , {
        "./ConstantGlobal": "ConstantGlobal",
        "./Data": "Data",
        "./Net": "Net"
    }],
    ConstantGlobal: [function(e, t, n) {
        "use strict";
        cc._RF.push(t, "dc653BveehMzLvGKbELE8r9", "ConstantGlobal"),
        Object.defineProperty(n, "__esModule", {
            value: !0
        }),
        n.E_Global = void 0,
        function(e) {
            e.RefreshUserInfo = "RefreshUserInfo",
            e.RefreshExchanges = "RefreshExchanges",
            e.RefreshTasks = "RefreshTasks",
            e.RefreshDepot = "RefreshDepot",
            e.RefreshSelectReward = "RefreshSelectReward",
            e.RefreshTitleList = "RefreshTitleList",
            e.RefreshSunInfo = "RefreshSunInfo",
            e.RefreshLotteryInfo = "RefreshLotteryInfo",
            e.RefreshPlantInfo = "RefreshPlantInfo",
            e.RefreshAdventure = "RefreshAdventure",
            e.SwitchScene = "SwitchScene",
            e.RefreshFriendList = "RefreshFriendList"
        }(n.E_Global || (n.E_Global = {})),
        cc._RF.pop()
    }
    , {}],
    Data: [function(e, t, n) {
        (function(a) {
            "use strict";
            cc._RF.push(t, "34b1aNbr6dPM5LnLmaHa889", "Data");
            var r = this && this.__awaiter || function(e, t, n, a) {
                return new (n || (n = Promise))(function(r, o) {
                    function i(e) {
                        try {
                            u(a.next(e))
                        } catch (t) {
                            o(t)
                        }
                    }
                    function s(e) {
                        try {
                            u(a.throw(e))
                        } catch (t) {
                            o(t)
                        }
                    }
                    function u(e) {
                        var t;
                        e.done ? r(e.value) : (t = e.value,
                        t instanceof n ? t : new n(function(e) {
                            e(t)
                        }
                        )).then(i, s)
                    }
                    u((a = a.apply(e, t || [])).next())
                }
                )
            }
              , o = this && this.__generator || function(e, t) {
                var n, a, r, o, i = {
                    label: 0,
                    sent: function() {
                        if (1 & r[0])
                            throw r[1];
                        return r[1]
                    },
                    trys: [],
                    ops: []
                };
                return o = {
                    next: s(0),
                    throw: s(1),
                    return: s(2)
                },
                "function" == typeof Symbol && (o[Symbol.iterator] = function() {
                    return this
                }
                ),
                o;
                function s(e) {
                    return function(t) {
                        return u([e, t])
                    }
                }
                function u(o) {
                    if (n)
                        throw new TypeError("Generator is already executing.");
                    for (; i; )
                        try {
                            if (n = 1,
                            a && (r = 2 & o[0] ? a.return : o[0] ? a.throw || ((r = a.return) && r.call(a),
                            0) : a.next) && !(r = r.call(a, o[1])).done)
                                return r;
                            switch (a = 0,
                            r && (o = [2 & o[0], r.value]),
                            o[0]) {
                            case 0:
                            case 1:
                                r = o;
                                break;
                            case 4:
                                return i.label++,
                                {
                                    value: o[1],
                                    done: !1
                                };
                            case 5:
                                i.label++,
                                a = o[1],
                                o = [0];
                                continue;
                            case 7:
                                o = i.ops.pop(),
                                i.trys.pop();
                                continue;
                            default:
                                if (!(r = (r = i.trys).length > 0 && r[r.length - 1]) && (6 === o[0] || 2 === o[0])) {
                                    i = 0;
                                    continue
                                }
                                if (3 === o[0] && (!r || o[1] > r[0] && o[1] < r[3])) {
                                    i.label = o[1];
                                    break
                                }
                                if (6 === o[0] && i.label < r[1]) {
                                    i.label = r[1],
                                    r = o;
                                    break
                                }
                                if (r && i.label < r[2]) {
                                    i.label = r[2],
                                    i.ops.push(o);
                                    break
                                }
                                r[2] && i.ops.pop(),
                                i.trys.pop();
                                continue
                            }
                            o = t.call(e, i)
                        } catch (s) {
                            o = [6, s],
                            a = 0
                        } finally {
                            n = r = 0
                        }
                    if (5 & o[0])
                        throw o[1];
                    return {
                        value: o[0] ? o[1] : void 0,
                        done: !0
                    }
                }
            }
            ;
            Object.defineProperty(n, "__esModule", {
                value: !0
            });
            var i = e("./ConstantGlobal")
              , s = e("./Net");
            n.default = new (function() {
                function e() {
                    this.isToggleOnToday = null,
                    this.gameOperation = {},
                    this.wxInfo = {},
                    this.userInfo = null,
                    this.wmInfo = null,
                    this.shareImages = {},
                    this.ipDialog = {},
                    this.sunInfo = {},
                    this.lotteryInfo = {},
                    this.localInfo = {},
                    this.adventureInfo = {},
                    this.titleList = {},
                    this.friendList = {},
                    this.recommendFriendList = [],
                    this.plantInfo = {},
                    this.depot = {},
                    this.guideSteps = null,
                    this.taskList = {},
                    this.autoToast = null,
                    this.helpFriendNum = 0,
                    this.viewTaskAutoClose = !1,
                    this.utmData = {};
                    var e = [{
                        key: "userInfo",
                        boardcast: i.E_Global.RefreshUserInfo
                    }, {
                        key: "exchanges",
                        boardcast: i.E_Global.RefreshExchanges
                    }, {
                        key: "titleList",
                        boardcast: i.E_Global.RefreshTitleList
                    }, {
                        key: "sunInfo",
                        boardcast: i.E_Global.RefreshSunInfo
                    }, {
                        key: "plantInfo",
                        boardcast: i.E_Global.RefreshPlantInfo
                    }, {
                        key: "depot",
                        boardcast: i.E_Global.RefreshDepot
                    }, {
                        key: "taskList",
                        boardcast: i.E_Global.RefreshTasks
                    }, {
                        key: "lotteryInfo",
                        boardcast: i.E_Global.RefreshLotteryInfo
                    }, {
                        key: "adventureInfo",
                        boardcast: i.E_Global.RefreshAdventure
                    }, {
                        key: "friendList",
                        boardcast: i.E_Global.RefreshFriendList
                    }];
                    xysz.tool.listenDataChange(this, e)
                }
                return e.prototype.initSensors = function() {
                    xysz.sensors = sensorsDataAnalytic201505;
                    var e, t = xysz.saas.getEnvByHostname();
                    console.log("currEnv\uff1a", t),
                    e = ["test", "stage", "dev"].includes(t) ? "https://tongyi-sink.sensorsdata.cn/sa?project=qiehuang_test" : "https://tongyi-sink.sensorsdata.cn/sa?project=qiehuang",
                    xysz.sensors.init({
                        server_url: e,
                        show_log: ["test", "stage", "dev"].includes(t),
                        name: "sensors",
                        app_flush_interval: 2e4,
                        app_flush_bulkSize: 70,
                        app_flush_network_policy: 20,
                        app_session_interval_time: 2e4,
                        heatmap: {
                            clickmap: "not_collect",
                            scroll_notice_map: "not_collect"
                        }
                    })
                }
                ,
                e.prototype.loginSensors = function() {
                    return r(this, void 0, void 0, function() {
                        var e, t, n;
                        return o(this, function(r) {
                            switch (r.label) {
                            case 0:
                                return e = {
                                    app_name: "\u8304\u7687"
                                },
                                xysz.sensors.registerPage(e),
                                [4, s.default.common.getUserTrackInfo()];
                            case 1:
                                return (t = r.sent().data) || (t = {
                                    user_nickname: this.userInfo.nickName,
                                    user_title: this.userInfo.title,
                                    user_level: this.userInfo.level
                                }),
                                t.userMobile && (t.userMobile = a.Base64.toBase64(encodeURIComponent(t.userMobile))),
                                n = {
                                    user_mobile: t.userMobile,
                                    user_nickname: t.userNickname,
                                    user_level: t.userLevel,
                                    user_title: t.userTitle,
                                    user_planting_stage: t.userPlantingStage,
                                    tomato_amount_sum: t.tomatoAmountSum,
                                    sunlight_point_sum: t.sunlightPointSum,
                                    exp_amount_sum: t.expAmountSum,
                                    sunlight_cost_sum: t.sunlightCostSum,
                                    tomato_cost_sum: t.tomatoCostSum,
                                    remaining_sunlight_point: t.remainingSunlightPoint,
                                    remaining_tomato_amount: t.remainingTomatoAmount,
                                    first_time_to_visit_qh: t.firstTimeToVisitQh,
                                    first_time_to_authorize_qh: t.firstTimeToAuthorizeQh,
                                    lottery_times_sum: t.lotteryTimesSum,
                                    challenge_weekly_ranking: t.challengeWeeklyRanking,
                                    coupon_amount_sum: t.couponAmountSum,
                                    last_time_for_get_coupon: t.lastTimeForGetCoupon
                                },
                                xysz.sensors.setProfile(n),
                                xysz.sensors.login(this.wmInfo && this.wmInfo.wid ? this.wmInfo.wid : this.userInfo.id),
                                xysz.sensors.identify(this.wmInfo && this.wmInfo.unionid ? this.wmInfo.unionid : this.userInfo.id, !0),
                                [2]
                            }
                        })
                    })
                }
                ,
                e
            }()),
            cc._RF.pop()
        }
        ).call(this, "undefined" != typeof global ? global : "undefined" != typeof self ? self : "undefined" != typeof window ? window : {})
    }
    , {
        "./ConstantGlobal": "ConstantGlobal",
        "./Net": "Net"
    }],
    Net: [function(e, t, n) {
        "use strict";
        cc._RF.push(t, "2e0c6/UzxZEQa0hrRvHbdBt", "Net");
        var a = this && this.__assign || function() {
            return (a = Object.assign || function(e) {
                for (var t, n = 1, a = arguments.length; n < a; n++)
                    for (var r in t = arguments[n])
                        Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                return e
            }
            ).apply(this, arguments)
        }
        ;
        Object.defineProperty(n, "__esModule", {
            value: !0
        });
        var r = e("./App")
          , o = e("./Data")
          , i = {
            getTimestamp: function() {
                return xysz.http.post("/common/public/api/getServerTimestamp", {}).then(function(e) {
                    return o.default.ServerTimestamp = e.data
                })
            },
            previewLogin: function(e) {
                return xysz.http.post("ga/public/api/testLogin", {
                    formData: e
                }).then(function(e) {
                    return xysz.http.defaults.headers.Authorization = e.data
                })
            },
            thirdLogin: function(e, t) {
                var n = e.wid
                  , a = e.openId
                  , r = e.appId;
                t && t.string && (t.string = "\u52a0\u8f7d\u4e2d....--");
                var o = {
                    md5Secret: "111111111112222222233333333333",
                    appId: r,
                    openId: a,
                    wid: n
                }
                  , i = xysz.tool.getSortedQuery(o)
                  , s = xysz.encrypt.Md5.encode(i).toUpperCase();
                return e.signature = s,
                t && t.string && (t.string = "\u52a0\u8f7d\u4e2d....---"),
                xysz.http.post("/ga/public/api/login", e).then(function(e) {
                    return xysz.http.defaults.headers.Authorization = e.data
                })
            }
        }
          , s = {
            getSunInfo: function(e) {
                return r.default.get("/ga/user/daily/info", {
                    params: {
                        userId: e
                    }
                }).then(function(e) {
                    return o.default.sunInfo = e.data
                })
            },
            stealSun: function(e) {
                return r.default.get("/ga/user/daily/steal", {
                    params: {
                        friendUserId: e
                    }
                })
            },
            pickupSun: function() {
                return r.default.get("/ga/user/daily/pickup")
            }
        }
          , u = {
            getPlantInfo: function(e) {
                return r.default.get("/ga/plant/info", {
                    params: {
                        userId: e
                    }
                }).then(function(e) {
                    return o.default.plantInfo = e.data
                })
            },
            upgradePlant: function(e) {
                return r.default.get("/ga/plant/upgrade", {
                    params: {
                        plantId: e
                    }
                }).then(function(e) {
                    return o.default.plantInfo = e.data
                })
            },
            startPlant: function() {
                return r.default.get("/ga/plant/start")
            },
            startSunning: function(e) {
                return r.default.get("/ga/plant/giveSunshine", {
                    params: {
                        plantId: e
                    }
                })
            },
            startSunningOnce: function(e) {
                return r.default.get("/ga/plant/batchgiveSunshine", {
                    params: {
                        plantId: e
                    }
                })
            },
            harvestTomato: function(e) {
                return r.default.get("/ga/plant/harvest", {
                    params: {
                        plantId: e
                    }
                })
            }
        }
          , c = {
            getFriendList: function(e, t) {
                return void 0 === e && (e = 1),
                void 0 === t && (t = 50),
                r.default.get("/ga/user/friend/list", {
                    params: {
                        page: e,
                        size: t
                    }
                }).then(function(e) {
                    return o.default.friendList = e.data.content
                })
            },
            addFriend: function(e, t, n) {
                return void 0 === n && (n = 1),
                r.default.get("/ga/user/friend/add", {
                    params: {
                        friendUserId: e,
                        type: t,
                        addType: n
                    }
                })
            },
            deletFriend: function(e) {
                return r.default.get("/ga/user/friend/del", {
                    params: {
                        friendUserId: e
                    }
                })
            },
            recommendFriends: function() {
                return r.default.get("/ga/user/friend/recommend").then(function(e) {
                    return o.default.recommendFriendList = e.data
                })
            }
        }
          , l = {
            getAdventureInfo: function(e, t) {
                return void 0 === e && (e = -1),
                void 0 === t && (t = 1),
                r.default.get("/ga/user/adventure/info", {
                    params: {
                        userId: e,
                        type: t
                    }
                }).then(function(e) {
                    return o.default.adventureInfo = e.data
                })
            },
            startAdventure: function() {
                return r.default.get("/ga/user/adventure/start")
            },
            rewardAdventure: function(e) {
                return r.default.get("/ga/user/adventure/drawPrize", {
                    params: {
                        adventureId: e
                    }
                })
            },
            helpAdventure: function(e) {
                return r.default.get("/ga/user/adventure/help", {
                    params: {
                        adventureId: e
                    }
                })
            },
            getPostcardInfo: function() {
                return r.default.get("/ga/user/postcard/list")
            }
        }
          , f = {
            getLotteryInfo: function() {
                return r.default.get("/ga/user/gift/box/info").then(function(e) {
                    return o.default.lotteryInfo = e.data
                })
            },
            startLottery: function(e) {
                return r.default.get("/ga/user/gift/box/drawPrize", {
                    params: {
                        activityId: e
                    }
                })
            },
            getLotteryPool: function() {
                return r.default.get("/ga/user/gift/box/prize")
            },
            getLotteryRecord: function() {
                return r.default.get("/ga/user/gift/box/prizeRecord")
            }
        }
          , d = {
            getTaskList: function() {
                return r.default.get("/ga/user/task/list").then(function(e) {
                    return o.default.taskList = e.data
                })
            },
            reportTask: function(e, t, n) {
                return r.default.get("/ga/user/task/report", {
                    params: {
                        taskType: e,
                        attachId: t,
                        taskId: n
                    }
                })
            },
            taskPrize: function(e) {
                return r.default.get("/ga/user/task/drawPrize", {
                    params: {
                        taskId: e
                    }
                })
            }
        }
          , p = {
            getExchangeList: function() {
                return r.default.get("/ga/user/gift/list").then(function(e) {
                    return o.default.exchanges = e.data
                })
            },
            exchangeExec: function(e) {
                return r.default.get("/ga/user/gift/center/exchange", {
                    params: {
                        giftId: e
                    }
                })
            },
            setSelectedExchange: function(e) {
                return r.default.get("/ga/user/gift/index/choose", {
                    params: {
                        giftId: e
                    }
                })
            },
            getSelectedExchange: function() {
                return r.default.get("/ga/user/gift/index/choose/query")
            },
            reportSelectedExchange: function() {
                return r.default.get("/ga/user/gift/index/choose/report")
            }
        }
          , h = {
            getDepotList: function() {
                return r.default.get("/ga/user/warehouse/list").then(function(e) {
                    return o.default.depot = e.data
                })
            }
        }
          , g = {
            challengeStart: function() {
                return r.default.get("/ga/challenge/start")
            },
            challengeEnd: function(e, t, n) {
                return r.default.post("/ga/challenge/report", {
                    battleId: e,
                    result: t,
                    costMillisecond: n
                })
            },
            challengeRank: function() {
                return r.default.get("/ga/challenge/rank")
            }
        }
          , m = {
            setOperate: function(e, t) {
                return r.default.post("/ga/user/cache/put", {
                    k: e,
                    v: t
                })
            },
            getOperate: function(e) {
                return r.default.get("/ga/user/cache/get", {
                    params: {
                        k: e
                    }
                })
            },
            deletOperate: function(e) {
                return r.default.get("/ga/user/cache/del", {
                    params: {
                        k: e
                    }
                })
            },
            getAllOperate: function() {
                return r.default.get("/ga/user/cache/getAll")
            }
        }
          , y = {
            common: a(a(a(a(a(a(a(a(a(a(a(a({}, {
                getUserInfo: function(e) {
                    return r.default.get("/ga/user/info", {
                        params: {
                            userId: e
                        }
                    }).then(function(e) {
                        return o.default.userInfo = e.data
                    })
                },
                updateUserInfo: function(e, t) {
                    return r.default.post("/ga/user/updateUserInfo", {
                        nickName: e,
                        avatarUrl: t
                    })
                },
                getIpTitleList: function() {
                    return r.default.get("/ga/user/title/list").then(function(e) {
                        return o.default.titleList = e.data
                    })
                },
                getIpDialogList: function() {
                    return r.default.get("/ga/misc/ip/data").then(function(e) {
                        return o.default.ipDialog = e.data
                    })
                },
                updateIpTitle: function(e) {
                    return r.default.get("/ga/user/title/update", {
                        params: {
                            titleId: e
                        }
                    })
                },
                getAbout: function() {
                    return r.default.get("/ga/misc/about")
                },
                getLive: function() {
                    return r.default.get("/ga/live/info")
                },
                getNews: function() {
                    return r.default.get("/ga/notice/list")
                },
                getUserTrackInfo: function() {
                    return r.default.get("/ga/user/query/report")
                }
            }), i), c), l), s), d), u), p), h), f), g), m)
        };
        n.default = y,
        cc._RF.pop()
    }
    , {
        "./App": "App",
        "./Data": "Data"
    }],
    RoundRectMask: [function(e, t, n) {
        "use strict";
        cc._RF.push(t, "0bdbadkFIhGqaZtHgG+w3wb", "RoundRectMask");
        var a, r = this && this.__extends || (a = function(e, t) {
            return (a = Object.setPrototypeOf || {
                __proto__: []
            }instanceof Array && function(e, t) {
                e.__proto__ = t
            }
            || function(e, t) {
                for (var n in t)
                    Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n])
            }
            )(e, t)
        }
        ,
        function(e, t) {
            function n() {
                this.constructor = e
            }
            a(e, t),
            e.prototype = null === t ? Object.create(t) : (n.prototype = t.prototype,
            new n)
        }
        ), o = this && this.__decorate || function(e, t, n, a) {
            var r, o = arguments.length, i = o < 3 ? t : null === a ? a = Object.getOwnPropertyDescriptor(t, n) : a;
            if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                i = Reflect.decorate(e, t, n, a);
            else
                for (var s = e.length - 1; s >= 0; s--)
                    (r = e[s]) && (i = (o < 3 ? r(i) : o > 3 ? r(t, n, i) : r(t, n)) || i);
            return o > 3 && i && Object.defineProperty(t, n, i),
            i
        }
        ;
        Object.defineProperty(n, "__esModule", {
            value: !0
        }),
        n.RoundRectMask = void 0;
        var i = cc._decorator.property
          , s = cc._decorator.ccclass
          , u = cc._decorator.executeInEditMode
          , c = cc._decorator.disallowMultiple
          , l = cc._decorator.requireComponent
          , f = cc._decorator.menu;
        cc.macro.ENABLE_WEBGL_ANTIALIAS = !0;
        var d = function(e) {
            function t() {
                var t = null !== e && e.apply(this, arguments) || this;
                return t._radius = 50,
                t.mask = null,
                t
            }
            return r(t, e),
            Object.defineProperty(t.prototype, "radius", {
                get: function() {
                    return this._radius
                },
                set: function(e) {
                    this._radius = e,
                    this.updateMask(e)
                },
                enumerable: !1,
                configurable: !0
            }),
            t.prototype.onEnable = function() {
                this.mask = this.getComponent(cc.Mask),
                this.updateMask(this.radius)
            }
            ,
            t.prototype.updateMask = function(e) {
                var t = e >= 0 ? e : 0;
                t < 1 && (t = Math.min(this.node.width, this.node.height) * t),
                this.mask.radius = t,
                this.mask.onDraw = this.onDraw.bind(this.mask),
                this.mask._updateGraphics = this._updateGraphics.bind(this.mask),
                this.mask.type = cc.Mask.Type.RECT
            }
            ,
            t.prototype._updateGraphics = function() {
                var e = this._graphics;
                e && this.onDraw(e)
            }
            ,
            t.prototype.onDraw = function(e) {
                e.clear(!1);
                var t = this.node
                  , n = t.width
                  , a = t.height
                  , r = -n * t.anchorX
                  , o = -a * t.anchorY;
                e.roundRect(r, o, n, a, this.radius || 0),
                cc.game.renderType === cc.game.RENDER_TYPE_CANVAS ? e.stroke() : e.fill()
            }
            ,
            o([i()], t.prototype, "_radius", void 0),
            o([i({
                tooltip: "\u5706\u89d2\u534a\u5f84:\n0-1\u4e4b\u95f4\u4e3a\u6700\u5c0f\u8fb9\u957f\u6bd4\u4f8b\u503c, \n>1\u4e3a\u5177\u4f53\u50cf\u7d20\u503c"
            })], t.prototype, "radius", null),
            o([s(), u(!0), c(!0), l(cc.Mask), f("\u6e32\u67d3\u7ec4\u4ef6/\u5706\u89d2\u906e\u7f69")], t)
        }(cc.Component);
        n.RoundRectMask = d,
        cc._RF.pop()
    }
    , {}],
    SceneReady: [function(e, t, n) {
        (function(a) {
            "use strict";
            cc._RF.push(t, "0bd71S+AfhLlYskbvklThEv", "SceneReady");
            var r, o = this && this.__extends || (r = function(e, t) {
                return (r = Object.setPrototypeOf || {
                    __proto__: []
                }instanceof Array && function(e, t) {
                    e.__proto__ = t
                }
                || function(e, t) {
                    for (var n in t)
                        Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n])
                }
                )(e, t)
            }
            ,
            function(e, t) {
                function n() {
                    this.constructor = e
                }
                r(e, t),
                e.prototype = null === t ? Object.create(t) : (n.prototype = t.prototype,
                new n)
            }
            ), i = this && this.__decorate || function(e, t, n, a) {
                var r, o = arguments.length, i = o < 3 ? t : null === a ? a = Object.getOwnPropertyDescriptor(t, n) : a;
                if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                    i = Reflect.decorate(e, t, n, a);
                else
                    for (var s = e.length - 1; s >= 0; s--)
                        (r = e[s]) && (i = (o < 3 ? r(i) : o > 3 ? r(t, n, i) : r(t, n)) || i);
                return o > 3 && i && Object.defineProperty(t, n, i),
                i
            }
            , s = this && this.__awaiter || function(e, t, n, a) {
                return new (n || (n = Promise))(function(r, o) {
                    function i(e) {
                        try {
                            u(a.next(e))
                        } catch (t) {
                            o(t)
                        }
                    }
                    function s(e) {
                        try {
                            u(a.throw(e))
                        } catch (t) {
                            o(t)
                        }
                    }
                    function u(e) {
                        var t;
                        e.done ? r(e.value) : (t = e.value,
                        t instanceof n ? t : new n(function(e) {
                            e(t)
                        }
                        )).then(i, s)
                    }
                    u((a = a.apply(e, t || [])).next())
                }
                )
            }
            , u = this && this.__generator || function(e, t) {
                var n, a, r, o, i = {
                    label: 0,
                    sent: function() {
                        if (1 & r[0])
                            throw r[1];
                        return r[1]
                    },
                    trys: [],
                    ops: []
                };
                return o = {
                    next: s(0),
                    throw: s(1),
                    return: s(2)
                },
                "function" == typeof Symbol && (o[Symbol.iterator] = function() {
                    return this
                }
                ),
                o;
                function s(e) {
                    return function(t) {
                        return u([e, t])
                    }
                }
                function u(o) {
                    if (n)
                        throw new TypeError("Generator is already executing.");
                    for (; i; )
                        try {
                            if (n = 1,
                            a && (r = 2 & o[0] ? a.return : o[0] ? a.throw || ((r = a.return) && r.call(a),
                            0) : a.next) && !(r = r.call(a, o[1])).done)
                                return r;
                            switch (a = 0,
                            r && (o = [2 & o[0], r.value]),
                            o[0]) {
                            case 0:
                            case 1:
                                r = o;
                                break;
                            case 4:
                                return i.label++,
                                {
                                    value: o[1],
                                    done: !1
                                };
                            case 5:
                                i.label++,
                                a = o[1],
                                o = [0];
                                continue;
                            case 7:
                                o = i.ops.pop(),
                                i.trys.pop();
                                continue;
                            default:
                                if (!(r = (r = i.trys).length > 0 && r[r.length - 1]) && (6 === o[0] || 2 === o[0])) {
                                    i = 0;
                                    continue
                                }
                                if (3 === o[0] && (!r || o[1] > r[0] && o[1] < r[3])) {
                                    i.label = o[1];
                                    break
                                }
                                if (6 === o[0] && i.label < r[1]) {
                                    i.label = r[1],
                                    r = o;
                                    break
                                }
                                if (r && i.label < r[2]) {
                                    i.label = r[2],
                                    i.ops.push(o);
                                    break
                                }
                                r[2] && i.ops.pop(),
                                i.trys.pop();
                                continue
                            }
                            o = t.call(e, i)
                        } catch (s) {
                            o = [6, s],
                            a = 0
                        } finally {
                            n = r = 0
                        }
                    if (5 & o[0])
                        throw o[1];
                    return {
                        value: o[0] ? o[1] : void 0,
                        done: !0
                    }
                }
            }
            ;
            Object.defineProperty(n, "__esModule", {
                value: !0
            });
            var c = e("../Script/App")
              , l = e("../Script/Data")
              , f = e("../Script/Net")
              , d = cc._decorator
              , p = d.ccclass
              , h = d.property
              , g = function(e) {
                function t() {
                    var t = null !== e && e.apply(this, arguments) || this;
                    return t.lbTip = null,
                    t.isLoginFail = !1,
                    t
                }
                return o(t, e),
                t.prototype.onLoad = function() {
                    return s(this, void 0, void 0, function() {
                        var e;
                        return u(this, function(t) {
                            switch (t.label) {
                            case 0:
                                return this.isLoginFail = !1,
                                document.title = "\u8304\u7687\u7684\u5bb6",
                                "dev" != xysz.saas.getEnvByHostname() ? [3, 2] : [4, xysz.h5.showConsole()];
                            case 1:
                                t.sent(),
                                t.label = 2;
                            case 2:
                                return this.lbTip.string = "\u52a0\u8f7d\u4e2d.",
                                c.default.initServerInfo(),
                                [4, l.default.initSensors()];
                            case 3:
                                return t.sent(),
                                this.lbTip.string = "\u52a0\u8f7d\u4e2d..",
                                xysz.query.token && (e = decodeURIComponent(xysz.query.token),
                                l.default.wmInfo = JSON.parse(a.Base64.decode(e)),
                                l.default.wmInfo.channelInfo ? l.default.utmData = l.default.wmInfo.channelInfo : (l.default.utmData = {},
                                l.default.wmInfo.utm_campaign && (l.default.utmData.utm_campaign = l.default.wmInfo.utm_campaign),
                                l.default.wmInfo.utm_source && (l.default.utmData.utm_source = l.default.wmInfo.utm_source),
                                l.default.wmInfo.utm_medium && (l.default.utmData.utm_medium = l.default.wmInfo.utm_medium),
                                l.default.wmInfo.utm_term && (l.default.utmData.utm_term = l.default.wmInfo.utm_term),
                                l.default.wmInfo.utm_content && (l.default.utmData.utm_content = l.default.wmInfo.utm_content))),
                                this.lbTip.string = "\u52a0\u8f7d\u4e2d...",
                                "dev" == xysz.saas.getEnvByHostname() && setTimeout(function() {
                                    console.log("query:", xysz.query, l.default.wmInfo, location.href)
                                }, 1e3),
                                [4, xysz.wx.web.init()];
                            case 4:
                                return t.sent(),
                                this.lbTip.string = "\u52a0\u8f7d\u4e2d....",
                                this.doLogin(),
                                [2]
                            }
                        })
                    })
                }
                ,
                t.prototype.doLogin = function() {
                    return s(this, void 0, void 0, function() {
                        var e, t, n, a, r, o = this;
                        return u(this, function(i) {
                            switch (i.label) {
                            case 0:
                                return [3, 2];
                            case 1:
                                return i.sent(),
                                [3, 8];
                            case 2:
                                return l.default.wmInfo ? l.default.wmInfo.thirdAppId && l.default.wmInfo.openId && l.default.wmInfo.wid ? (this.lbTip.string = "\u52a0\u8f7d\u4e2d....-",
                                [4, f.default.common.thirdLogin({
                                    appId: l.default.wmInfo.thirdAppId,
                                    openId: l.default.wmInfo.openId,
                                    wid: l.default.wmInfo.wid
                                }, this.lbTip).catch(function(e) {
                                    o.isLoginFail = !0,
                                    o.lbTip && o.lbTip.string && (o.lbTip.string = (e.name ? e.name : "err") + ":" + (e.message ? e.message : e.toString())),
                                    o.scheduleOnce(function() {
                                        xysz.ui.showToast("\u7f51\u7edc\u5f02\u5e38\uff0c\u91cd\u65b0\u52a0\u8f7d..."),
                                        o.isLoginFail = !1,
                                        o.doLogin()
                                    }, 1)
                                })]) : (e = "",
                                l.default.wmInfo.thirdAppId ? l.default.wmInfo.openId ? l.default.wmInfo.wid ? l.default.wmInfo.unionid || (e = "unionid") : e = "wid" : e = "openId" : e = "thirdAppId",
                                this.lbTip.string = "token\u53c2\u6570\u9519\u8bef-\u7f3a\u5931" + e,
                                [2]) : [3, 7];
                            case 3:
                                return i.sent(),
                                l.default.wmInfo.userInfo && (l.default.wmInfo.userInfo.nickName || l.default.wmInfo.userInfo.avatarUrl || l.default.wmInfo.userInfo.phone) ? [4, f.default.common.getUserInfo()] : [3, 6];
                            case 4:
                                return i.sent(),
                                t = l.default.userInfo.isAuthorizeNickName ? null : l.default.wmInfo.userInfo.nickName,
                                n = l.default.userInfo.isAuthorizeAvatarUrl ? null : l.default.wmInfo.userInfo.avatarUrl,
                                [4, f.default.common.updateUserInfo(t, n)];
                            case 5:
                                i.sent(),
                                i.label = 6;
                            case 6:
                                return [3, 8];
                            case 7:
                                return this.lbTip.string = "\u4f20\u53c2\u5f02\u5e38\uff0ctoken\u4e0d\u80fd\u4e3a\u7a7a",
                                [2];
                            case 8:
                                return this.isLoginFail ? [2] : (this.lbTip.string = "\u52a0\u8f7d\u4e2d.....",
                                [4, f.default.common.getUserInfo()]);
                            case 9:
                                i.sent(),
                                i.label = 10;
                            case 10:
                                return i.trys.push([10, 12, , 13]),
                                [4, this.updateTask()];
                            case 11:
                            case 12:
                                return i.sent(),
                                [3, 13];
                            case 13:
                                if (this.lbTip.string = "\u52a0\u8f7d\u4e2d......",
                                l.default.userInfo.isAuthorizeNickName && l.default.userInfo.isAuthorizeAvatarUrl)
                                    cc.log("\u5df2\u6388\u6743\u7528\u6237");
                                else if (!l.default.wmInfo || "100091024" != l.default.wmInfo.wid) {
                                    for (r in console.log("\u8f6c\u5165\u6388\u6743\u4e2d\u8f6c\u9875\u9762"),
                                    a = {
                                        title: "\u6388\u6743\u4e2d\u8f6c\u9875",
                                        shareType: "auth",
                                        imageUrl: "",
                                        urlParams: {},
                                        user: l.default.userInfo.isAuthorizeNickName && l.default.userInfo.isAuthorizeAvatarUrl ? "true" : "false",
                                        is_new_user: "true"
                                    },
                                    l.default.utmData)
                                        a[r] = l.default.utmData[r];
                                    return c.default.gotoMiniProgramPage(a),
                                    [2]
                                }
                                return [4, Promise.all([xysz.res.loadBundle("abGame"), c.default.initOnlineOperation()])];
                            case 14:
                                return i.sent(),
                                this.afterLogin(),
                                [2]
                            }
                        })
                    })
                }
                ,
                t.prototype.updateTask = function() {
                    return s(this, void 0, void 0, function() {
                        var e, t, n;
                        return u(this, function(a) {
                            switch (a.label) {
                            case 0:
                                return xysz.query.adventureId || l.default.wmInfo && l.default.wmInfo.adventureId ? [4, f.default.common.helpAdventure(xysz.query.adventureId || l.default.wmInfo.adventureId)] : [3, 2];
                            case 1:
                                a.sent(),
                                l.default.autoToast = "\u6210\u529f\u534f\u52a9\u597d\u53cb",
                                a.label = 2;
                            case 2:
                                return xysz.query.userId || l.default.wmInfo && l.default.wmInfo.userId ? (t = (e = f.default.common).reportTask,
                                n = [1, xysz.query.userId || l.default.wmInfo.userId],
                                [4, c.default.getTaskIdByType(1)]) : [3, 5];
                            case 3:
                                return [4, t.apply(e, n.concat([a.sent()]))];
                            case 4:
                                a.sent(),
                                l.default.autoToast = "\u9080\u8bf7\u597d\u53cb\u6210\u529f",
                                a.label = 5;
                            case 5:
                                return xysz.query.friendUserId || l.default.wmInfo && l.default.wmInfo.friendUserId ? [4, f.default.common.addFriend(xysz.query.friendUserId || l.default.wmInfo.friendUserId, 2, 2)] : [3, 7];
                            case 6:
                                a.sent(),
                                l.default.autoToast = "\u9080\u8bf7\u597d\u53cb\u6210\u529f",
                                a.label = 7;
                            case 7:
                                return [2]
                            }
                        })
                    })
                }
                ,
                t.prototype.afterLogin = function() {
                    return s(this, void 0, void 0, function() {
                        return u(this, function() {
                            return c.default.initShareInfo(),
                            l.default.loginSensors(),
                            l.default.isFirstLogin = !0,
                            c.default.gotoNextScene("Plant"),
                            [2]
                        })
                    })
                }
                ,
                i([h(cc.Label)], t.prototype, "lbTip", void 0),
                i([p], t)
            }(cc.Component);
            n.default = g,
            cc._RF.pop()
        }
        ).call(this, "undefined" != typeof global ? global : "undefined" != typeof self ? self : "undefined" != typeof window ? window : {})
    }
    , {
        "../Script/App": "App",
        "../Script/Data": "Data",
        "../Script/Net": "Net"
    }],
    ViewEmpty: [function(e, t, n) {
        "use strict";
        cc._RF.push(t, "049c7ykiZlEtK3Zftg6WvC9", "ViewEmpty");
        var a, r = this && this.__extends || (a = function(e, t) {
            return (a = Object.setPrototypeOf || {
                __proto__: []
            }instanceof Array && function(e, t) {
                e.__proto__ = t
            }
            || function(e, t) {
                for (var n in t)
                    Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n])
            }
            )(e, t)
        }
        ,
        function(e, t) {
            function n() {
                this.constructor = e
            }
            a(e, t),
            e.prototype = null === t ? Object.create(t) : (n.prototype = t.prototype,
            new n)
        }
        ), o = this && this.__decorate || function(e, t, n, a) {
            var r, o = arguments.length, i = o < 3 ? t : null === a ? a = Object.getOwnPropertyDescriptor(t, n) : a;
            if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
                i = Reflect.decorate(e, t, n, a);
            else
                for (var s = e.length - 1; s >= 0; s--)
                    (r = e[s]) && (i = (o < 3 ? r(i) : o > 3 ? r(t, n, i) : r(t, n)) || i);
            return o > 3 && i && Object.defineProperty(t, n, i),
            i
        }
        ;
        Object.defineProperty(n, "__esModule", {
            value: !0
        });
        var i = cc._decorator
          , s = i.ccclass
          , u = (i.property,
        function(e) {
            function t() {
                return null !== e && e.apply(this, arguments) || this
            }
            return r(t, e),
            o([s], t)
        }(xysz.ViewBase));
        n.default = u,
        cc._RF.pop()
    }
    , {}]
}, {}, ["App", "ConstantGlobal", "Data", "RoundRectMask", "ViewEmpty", "Net", "SceneReady"]);
