(function(t, e) {
    "object" == typeof exports && "undefined" != typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define(e) : (t = "undefined" != typeof globalThis ? globalThis : t || self).xysz = e()
}
)(this, function() {
    "use strict";
    var t = function(e, n) {
        return (t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                Object.prototype.hasOwnProperty.call(e, n) && (t[n] = e[n])
        }
        )(e, n)
    };
    function e(e, n) {
        if ("function" != typeof n && null !== n)
            throw new TypeError("Class extends value " + String(n) + " is not a constructor or null");
        function o() {
            this.constructor = e
        }
        t(e, n),
        e.prototype = null === n ? Object.create(n) : (o.prototype = n.prototype,
        new o)
    }
    var n = function() {
        return (n = Object.assign || function(t) {
            for (var e, n = 1, o = arguments.length; n < o; n++)
                for (var r in e = arguments[n])
                    Object.prototype.hasOwnProperty.call(e, r) && (t[r] = e[r]);
            return t
        }
        ).apply(this, arguments)
    };
    function o(t, e, n, o) {
        var r, i = arguments.length, s = i < 3 ? e : null === o ? o = Object.getOwnPropertyDescriptor(e, n) : o;
        if ("object" == typeof Reflect && "function" == typeof Reflect.decorate)
            s = Reflect.decorate(t, e, n, o);
        else
            for (var c = t.length - 1; c >= 0; c--)
                (r = t[c]) && (s = (i < 3 ? r(s) : i > 3 ? r(e, n, s) : r(e, n)) || s);
        return i > 3 && s && Object.defineProperty(e, n, s),
        s
    }
    function r(t, e, n, o) {
        return new (n || (n = Promise))(function(r, i) {
            function s(t) {
                try {
                    a(o.next(t))
                } catch (e) {
                    i(e)
                }
            }
            function c(t) {
                try {
                    a(o.throw(t))
                } catch (e) {
                    i(e)
                }
            }
            function a(t) {
                var e;
                t.done ? r(t.value) : (e = t.value,
                e instanceof n ? e : new n(function(t) {
                    t(e)
                }
                )).then(s, c)
            }
            a((o = o.apply(t, e || [])).next())
        }
        )
    }
    function i(t, e) {
        var n, o, r, i, s = {
            label: 0,
            sent: function() {
                if (1 & r[0])
                    throw r[1];
                return r[1]
            },
            trys: [],
            ops: []
        };
        return i = {
            next: c(0),
            throw: c(1),
            return: c(2)
        },
        "function" == typeof Symbol && (i[Symbol.iterator] = function() {
            return this
        }
        ),
        i;
        function c(t) {
            return function(e) {
                return a([t, e])
            }
        }
        function a(i) {
            if (n)
                throw new TypeError("Generator is already executing.");
            for (; s; )
                try {
                    if (n = 1,
                    o && (r = 2 & i[0] ? o.return : i[0] ? o.throw || ((r = o.return) && r.call(o),
                    0) : o.next) && !(r = r.call(o, i[1])).done)
                        return r;
                    switch (o = 0,
                    r && (i = [2 & i[0], r.value]),
                    i[0]) {
                    case 0:
                    case 1:
                        r = i;
                        break;
                    case 4:
                        return s.label++,
                        {
                            value: i[1],
                            done: !1
                        };
                    case 5:
                        s.label++,
                        o = i[1],
                        i = [0];
                        continue;
                    case 7:
                        i = s.ops.pop(),
                        s.trys.pop();
                        continue;
                    default:
                        if (!(r = (r = s.trys).length > 0 && r[r.length - 1]) && (6 === i[0] || 2 === i[0])) {
                            s = 0;
                            continue
                        }
                        if (3 === i[0] && (!r || i[1] > r[0] && i[1] < r[3])) {
                            s.label = i[1];
                            break
                        }
                        if (6 === i[0] && s.label < r[1]) {
                            s.label = r[1],
                            r = i;
                            break
                        }
                        if (r && s.label < r[2]) {
                            s.label = r[2],
                            s.ops.push(i);
                            break
                        }
                        r[2] && s.ops.pop(),
                        s.trys.pop();
                        continue
                    }
                    i = e.call(t, s)
                } catch (c) {
                    i = [6, c],
                    o = 0
                } finally {
                    n = r = 0
                }
            if (5 & i[0])
                throw i[1];
            return {
                value: i[0] ? i[1] : void 0,
                done: !0
            }
        }
    }
    var s = {
        Socket: {
            Open: "Open",
            Message: "Message",
            SilenceTimeout: "SilenceTimeout",
            ConnectTimeout: "ConnectTimeout",
            RecvTimeout: "RecvTimeout",
            Disconnect: "Disconnect"
        }
    }
      , c = {
        SocketInfo: "socket_info",
        ViewOpened: "ViewOpened",
        ViewClosed: "ViewClosed",
        ViewEmpty: "ViewEmpty",
        ViewBack: "ViewBack",
        DeviceOrientation: "DeviceOrientation"
    }
      , a = {
        browser_wx: "browser_wx",
        program_wx: "program_wx",
        other: "other",
        taobao: "taobao"
    }
      , u = cc._decorator
      , l = u.ccclass
      , h = u.property
      , f = cc.Enum({
        None: 0,
        Scale: 1,
        DrawerBottom: 2
    })
      , p = function(t) {
        function n() {
            var e = null !== t && t.apply(this, arguments) || this;
            return e.animStyle = f.Scale,
            e.ndCore = null,
            e.emptyClose = !1,
            e.btnClose = null,
            e.maskColor = cc.color(0, 0, 0, 192),
            e._isAllowClose = !1,
            e
        }
        return e(n, t),
        n.prototype.onOpenFinish = function() {}
        ,
        n.prototype.onCloseStart = function() {}
        ,
        n.prototype.loadComplete = function() {}
        ,
        n.prototype.startComplete = function() {}
        ,
        n.prototype.destroyComplete = function() {}
        ,
        n.prototype.setData = function() {}
        ,
        n.prototype.onLoad = function() {
            var t = this;
            this.node.width = cc.winSize.width,
            this.node.height = cc.winSize.height,
            this.drawMask(),
            cc.view.on("design-resolution-changed", this.drawMask, this),
            this.getComponent(cc.BlockInputEvents) || this.addComponent(cc.BlockInputEvents),
            this.emptyClose && (this.allowClickEmptyClose(),
            this.btnClose = null),
            this.btnClose && this.btnClose.node.once("click", function() {
                t.closeSelf(),
                xysz.sound.voiceClick()
            }),
            this.initCore(),
            this.loadComplete()
        }
        ,
        n.prototype.drawMask = function() {
            this.getComponent(cc.Graphics) || this.addComponent(cc.Graphics);
            var t = this.getComponent(cc.Graphics);
            t.clear(),
            t.fillColor = this.maskColor,
            t.rect(-cc.winSize.width / 2, -cc.winSize.height / 2, cc.winSize.width, cc.winSize.height),
            t.fill()
        }
        ,
        n.prototype.initCore = function() {
            this.animStyle === f.DrawerBottom ? this.ndCore.y = 1.5 * -cc.winSize.height : this.animStyle === f.Scale && (this.ndCore.scale = 0)
        }
        ,
        n.prototype.start = function() {
            return r(this, void 0, void 0, function() {
                var t = this;
                return i(this, function(e) {
                    switch (e.label) {
                    case 0:
                        return cc.game.emit(c.ViewOpened, this.node.name),
                        this.startComplete(),
                        this.animStyle === f.None ? [3, 2] : [4, new Promise(function(e) {
                            return cc.tween(t.ndCore).then(t.getOpenTweenPart()).call(e).start()
                        }
                        )];
                    case 1:
                        e.sent(),
                        e.label = 2;
                    case 2:
                        return this._isAllowClose = !0,
                        this.onOpenFinish(),
                        [2]
                    }
                })
            })
        }
        ,
        n.prototype.getOpenTweenPart = function() {
            if (this.animStyle === f.DrawerBottom) {
                var t = .5 * -cc.winSize.height;
                return cc.tween().to(.4, {
                    y: t
                }).to(.1, {
                    y: t - 20
                }).to(.1, {
                    y: t
                }).to(.1, {
                    y: t - 10
                }).to(.1, {
                    y: t
                })
            }
            if (this.animStyle === f.Scale)
                return cc.tween().to(.2, {
                    scale: 1.1
                }).to(.2, {
                    scale: 1
                })
        }
        ,
        n.prototype.onDestroy = function() {
            console.log("onDestroyonDestroy---------"),
            cc.game.targetOff(this),
            cc.view.targetOff(this);
            var t = this.node.name;
            this.scheduleOnce(function() {
                console.log("onDestroy-scheduleOnce"),
                cc.game.emit(c.ViewClosed, t)
            }),
            this.destroyComplete()
        }
        ,
        n.prototype.closeSelf = function() {
            return r(this, void 0, void 0, function() {
                var t = this;
                return i(this, function(e) {
                    switch (e.label) {
                    case 0:
                        return cc.isValid(this.node, !0) ? (this.onCloseStart(),
                        this.animStyle === f.None ? [3, 2] : [4, new Promise(function(e) {
                            return cc.tween(t.ndCore).then(t.getCloseTweenPart()).call(e).start()
                        }
                        )]) : [2];
                    case 1:
                        e.sent(),
                        e.label = 2;
                    case 2:
                        return this.node.destroy(),
                        [2]
                    }
                })
            })
        }
        ,
        n.prototype.getCloseTweenPart = function() {
            return this.animStyle === f.DrawerBottom ? cc.tween().to(.3, {
                y: 1.5 * -cc.winSize.height
            }) : this.animStyle === f.Scale ? cc.tween().to(.1, {
                scale: 1.1
            }).to(.2, {
                scale: 0
            }) : void 0
        }
        ,
        n.prototype.allowClickEmptyClose = function() {
            var t = this;
            this.node.getComponent(cc.Button) || this.node.addComponent(cc.Button),
            this.ndCore && !this.ndCore.getComponent(cc.BlockInputEvents) && this.ndCore.addComponent(cc.BlockInputEvents),
            this.node.on("click", function() {
                xysz.sound.voiceClick(),
                t._isAllowClose && (t.node.off("click"),
                t.closeSelf())
            })
        }
        ,
        n.prototype.hideShadow = function() {
            this.getComponent(cc.Graphics).destroy()
        }
        ,
        o([h({
            type: f,
            tooltip: "\u5f39\u7a97\u6253\u5f00\u52a8\u753b\u7c7b\u578b"
        })], n.prototype, "animStyle", void 0),
        o([h({
            type: cc.Node,
            tooltip: "\u6709\u52a8\u753b\u5fc5\u987b\u8bbe\u7f6e\uff0c\u52a8\u753b\u4f5c\u7528\u4e8e\u6b64\u8282\u70b9",
            visible: function() {
                return this.animStyle !== f.None
            }
        })], n.prototype, "ndCore", void 0),
        o([h({
            tooltip: "\u662f\u5426\u5141\u8bb8\u70b9\u51fbndCore\u533a\u57df\u4e4b\u5916\u5219\u5173\u95ed\u754c\u9762",
            visible: function() {
                return !!this.ndCore
            }
        })], n.prototype, "emptyClose", void 0),
        o([h(cc.Button)], n.prototype, "btnClose", void 0),
        o([h(cc.Color)], n.prototype, "maskColor", void 0),
        o([l], n)
    }(cc.Component)
      , d = function() {
        function t(t, e) {
            void 0 === e && (e = ""),
            this._pfb = null,
            this._pool = null,
            this._pfb = t,
            this._pool = new cc.NodePool(e)
        }
        return t.prototype.get = function() {
            var t = this._pool.get();
            return t || (t = cc.instantiate(this._pfb)),
            t
        }
        ,
        t.prototype.put = function(t) {
            this._pool.put(t)
        }
        ,
        t.prototype.clear = function() {
            this._pool.clear()
        }
        ,
        t
    }()
      , m = {
        searchBFS: function(t, e, n) {
            for (var o = t[n][e], r = [{
                x: e,
                y: n
            }], i = [{
                x: e,
                y: n
            }], s = [{
                x: e,
                y: n
            }], c = [{
                x: 1,
                y: 0
            }, {
                x: -1,
                y: 0
            }, {
                x: 0,
                y: 1
            }, {
                x: 0,
                y: -1
            }], a = function() {
                var e = r.pop();
                c.forEach(function(n) {
                    var c = n.x + e.x
                      , a = n.y + e.y;
                    i.find(function(t) {
                        return t.x === c && t.y === a
                    }) || (i.push({
                        x: c,
                        y: a
                    }),
                    c >= 0 && c < t[0].length && a >= 0 && a < t.length && t[a][c] === o && (r.push({
                        x: c,
                        y: a
                    }),
                    s.push({
                        x: c,
                        y: a
                    })))
                })
            }; r.length > 0; )
                a();
            return s
        },
        isInTriangle: function(t, e, n, o) {
            var r = t.subtract(o)
              , i = e.subtract(o)
              , s = n.subtract(o)
              , c = r.cross(i)
              , a = i.cross(s)
              , u = s.cross(r);
            return !(c * a < 0 || c * u < 0 || a * u < 0)
        },
        checkClickInRhombus: function(t, e, n, o) {
            var r = this.isInTriangle(cc.v2(e.x, e.y + o / 2), cc.v2(e.x, e.y - o / 2), cc.v2(e.x + n / 2, e.y), t)
              , i = this.isInTriangle(cc.v2(e.x, e.y + o / 2), cc.v2(e.x, e.y - o / 2), cc.v2(e.x - n / 2, e.y), t);
            return r || i
        }
    }
      , y = {
        swing: function(t) {
            cc.tween(t).repeatForever(cc.tween().to(Math.random() + 1, {
                angle: xysz.tool.getRangeValue(5, 8)
            }).to(Math.random() + 1, {
                angle: xysz.tool.getRangeValue(-8, -5)
            })).start()
        },
        float: function(t, e, n) {
            n || (n = Math.random() + 1),
            cc.tween(t).repeatForever(cc.tween().by(n / 2, {
                x: e.x,
                y: e.y
            }).by(n / 2, {
                x: -e.x,
                y: -e.y
            })).start()
        },
        rotateOnceBack: function(t, e, n) {
            cc.tween(t).by(n / 2, {
                angle: e
            }).by(n / 2, {
                angle: -e
            }).start()
        },
        rotateForever: function(t, e) {
            void 0 === e && (e = 5),
            cc.tween(t).repeatForever(cc.tween().by(e, {
                angle: 360
            })).start()
        },
        focusAnimForever: function(t) {
            var e = t.scaleX
              , n = t.scaleY;
            t.stopAllActions(),
            cc.tween(t).repeatForever(cc.tween().to(.8, {
                scaleX: 1.1 * e,
                scaleY: 1.1 * n
            }).to(.8, {
                scaleX: 1 * e,
                scaleY: 1 * n
            })).start()
        },
        focusAnimOnce: function(t) {
            var e = t.scaleX
              , n = t.scaleY;
            t.stopAllActions(),
            cc.tween(t).to(.8, {
                scaleX: 1.1 * e,
                scaleY: 1.1 * n
            }).to(.8, {
                scaleX: 1 * e,
                scaleY: 1 * n
            }).start()
        },
        moveForever: function(t, e, n, o) {
            void 0 === o && (o = .5),
            cc.tween(t).repeatForever(cc.tween().to(o, {
                x: e.x,
                y: e.y
            }).to(o, {
                x: n.x,
                y: n.y
            })).start()
        },
        shakeScreen: function() {
            cc.tween(cc.Camera.findCamera(cc.Canvas.instance.node).node).to(.02, {
                x: 5,
                y: 7
            }).to(.02, {
                x: -6,
                y: 7
            }).to(.02, {
                x: -13,
                y: 3
            }).to(.02, {
                x: 3,
                y: -6
            }).to(.02, {
                x: -5,
                y: 5
            }).to(.02, {
                x: 2,
                y: -8
            }).to(.02, {
                x: -8,
                y: -10
            }).to(.02, {
                x: 3,
                y: 10
            }).to(.02, {
                x: 0,
                y: 0
            }).start()
        },
        flyTween: function(t, e, n, o) {
            void 0 === o && (o = 1);
            for (var r = e.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), i = n.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), s = function() {
                var e = cc.instantiate(t);
                e.parent = cc.Canvas.instance.node,
                e.zIndex = 100,
                e.position = r,
                e.active = !0,
                cc.tween(e).delay(.5 * Math.random()).to(.8, {
                    position: i
                }).call(function() {
                    return e.destroy()
                }).start()
            }, c = 0; c < o; c++)
                s();
            return new Promise(function(t) {
                cc.tween({}).delay(1).call(t).start()
            }
            )
        },
        circleFlyTween: function(t, e, n, o) {
            void 0 === o && (o = 1);
            for (var r = e.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), i = n.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), s = function(e) {
                var n = cc.instantiate(t);
                n.parent = cc.Canvas.instance.node;
                var s = Math.PI / 180 * Math.round(360 / o)
                  , c = r.x + n.width * Math.sin(s * e)
                  , a = r.y + n.height * Math.cos(s * e);
                n.position = r,
                n.active = !0,
                n.zIndex = 100,
                cc.tween(n).to(.05, {
                    position: cc.v3(c, a)
                }).call(function() {
                    cc.tween(n).delay(.2 * Math.random()).to(.8, {
                        position: i
                    }).call(function() {
                        return n.destroy()
                    }).start()
                }).start()
            }, c = 0; c < o; c++)
                s(c);
            return new Promise(function(t) {
                cc.tween({}).delay(1).call(t).start()
            }
            )
        }
    }
      , g = function() {
        function t() {}
        return t.initEmptyNode = function(e, n) {
            void 0 === n && (n = !0);
            var o = new t;
            if (o._mainNode = new cc.Node,
            o._mainNode.width = cc.winSize.width,
            o._mainNode.height = cc.winSize.height,
            o._mainNode.addComponent(cc.BlockInputEvents),
            o._mainNode.parent = e,
            o._mainNode.zIndex = 100,
            n) {
                var r = o._mainNode.addComponent(cc.Graphics);
                r.clear(),
                r.fillColor = cc.color(0, 0, 0, 192),
                r.rect(-cc.winSize.width / 2, -cc.winSize.height / 2, cc.winSize.width, cc.winSize.height),
                r.fill()
            }
            return o
        }
        ,
        t.prototype.injectImage = function(t, e, n) {
            void 0 === e && (e = 0),
            void 0 === n && (n = 0);
            var o = xysz.res.createTrimSprite();
            return o.node.x = e,
            o.node.y = n,
            o.spriteFrame = xysz.ui.getSpriteFrame(t),
            o.node.parent = this._mainNode,
            this
        }
        ,
        t.prototype.listenFullTouch = function(t, e, n, o) {
            if (void 0 === n && (n = 0),
            void 0 === o && (o = 0),
            e) {
                var r = xysz.res.createTrimSprite();
                r.node.anchorX = 0,
                r.node.anchorY = 1,
                r.node.x = n + 20,
                r.node.y = o - 20,
                r.spriteFrame = xysz.ui.getSpriteFrame(e),
                r.node.parent = this._mainNode,
                cc.tween(r.node).repeatForever(cc.tween().by(1, {
                    x: -40,
                    y: 40
                }).by(1, {
                    x: 40,
                    y: -40
                })).start()
            }
            return this._mainNode.on(cc.Node.EventType.TOUCH_END, t.bind(null, this._mainNode)),
            this
        }
        ,
        t.prototype.injectNodeWithTouch = function(t, e, n, o) {
            void 0 === n && (n = "");
            var r = cc.instantiate(t);
            if (r.getComponentsInChildren(cc.Button).forEach(function(t) {
                return t.enabled = !1
            }),
            r.setPosition(xysz.tool.getWorldPos(t)),
            r.on(cc.Node.EventType.TOUCH_END, e.bind(null, this._mainNode, r)),
            r.parent = this._mainNode,
            o && o(r),
            n) {
                var i = xysz.res.createTrimSprite();
                i.node.anchorX = 0,
                i.node.anchorY = 1,
                i.node.x = 20,
                i.node.y = -20,
                i.spriteFrame = xysz.ui.getSpriteFrame(n),
                i.node.parent = r,
                cc.tween(i.node).repeatForever(cc.tween().by(1, {
                    x: -40,
                    y: 40
                }).by(1, {
                    x: 40,
                    y: -40
                })).start()
            }
            return this
        }
        ,
        t.prototype.injectNode = function(t, e) {
            var n = cc.instantiate(t);
            return n.getComponentsInChildren(cc.Button).forEach(function(t) {
                return t.enabled = !1
            }),
            n.setPosition(xysz.tool.getWorldPos(t)),
            n.parent = this._mainNode,
            e && e(n),
            this
        }
        ,
        t.prototype.injectText = function(e, n, o, r) {
            if (void 0 === o && (o = 0),
            void 0 === r && (r = 0),
            console.log("Guide.pfbTextObj", t.pfbTextObj),
            !t.pfbTextObj[e])
                return this;
            var i = cc.instantiate(t.pfbTextObj[e]);
            return i.parent = this._mainNode,
            i.setPosition(o, r),
            i.getComponent(cc.RichText) ? (i.getComponent(cc.RichText).imageAtlas = xysz.ui.getAtlas("ui"),
            i.getComponent(cc.RichText).string = n) : i.getComponent(cc.Label) && (i.getComponent(cc.Label).string = n),
            this
        }
        ,
        t.pfbTextObj = {},
        t
    }();
    function v(t) {
        if ("string" == typeof t)
            try {
                return JSON.parse(t),
                !0
            } catch (e) {
                return !1
            }
        return !1
    }
    var w = new (function() {
        function t() {
            this.defaults = {
                timeout: 5e3,
                headers: {},
                params: {}
            }
        }
        return t.prototype.create = function() {
            return new t
        }
        ,
        t.prototype.mergeDefaultConfig = function(t) {
            return t.baseURL || (t.baseURL = this.defaults.baseURL),
            this.defaults.headers && (t.headers ? t.headers = n(n({}, this.defaults.headers), t.headers) : t.headers = n({}, this.defaults.headers)),
            this.defaults.params && (t.params ? t.params = n(n({}, this.defaults.params), t.params) : t.params = n({}, this.defaults.params)),
            this.defaults.cloudAppId && (t.cloudAppId = this.defaults.cloudAppId),
            t
        }
        ,
        t.prototype.formatConfig = function(t) {
            return t.baseURL && t.baseURL.endsWith("/") && (t.baseURL = t.baseURL.substr(0, t.baseURL.length - 1)),
            t.path && !t.path.startsWith("/") && (t.path = "/" + t.path),
            t
        }
        ,
        t.prototype.doRequest = function(t) {
            var e = this;
            return new Promise(function(o, s) {
                return r(e, void 0, void 0, function() {
                    var e, r, c, a, u, l, h, f, p = this;
                    return i(this, function(i) {
                        switch (i.label) {
                        case 0:
                            if (this.requestFulfilled && (e = this.requestFulfilled(n({}, t))) && (t = e),
                            r = function(t) {
                                t.response && (v(t.response) ? t.data = JSON.parse(t.response) : t.data = t.response,
                                delete t.response),
                                p.responseFulfilled && (t = p.responseFulfilled(t))instanceof Error ? s(t) : o(t)
                            }
                            ,
                            !window.tbCloud)
                                return [3, 5];
                            i.label = 1;
                        case 1:
                            return i.trys.push([1, 3, , 4]),
                            (c = {
                                path: t.path,
                                method: t.method,
                                params: t.params,
                                body: t.data,
                                exts: {
                                    cloudAppId: t.cloudAppId,
                                    timeout: 5e3
                                }
                            }).headers = t.headers,
                            [4, window.tbCloud.application.httpRequest(c)];
                        case 2:
                            return a = i.sent(),
                            r({
                                response: a,
                                path: t.path
                            }),
                            [3, 4];
                        case 3:
                            return u = i.sent(),
                            s(u),
                            [3, 4];
                        case 4:
                            return [2];
                        case 5:
                            for (m in l = "",
                            t.params)
                                null !== t.params[m] && void 0 !== t.params[m] && (l ? l += "&" + m + "=" + t.params[m] : "" != t.path ? l += "&" + m + "=" + t.params[m] : l += "?" + m + "=" + t.params[m]);
                            for (m in h = "" + t.baseURL + t.path + l,
                            (f = new XMLHttpRequest).timeout = 6e3,
                            f.open(t.method, h),
                            t.headers)
                                null !== t.headers[m] && void 0 !== t.headers[m] && f.setRequestHeader(m, t.headers[m]);
                            if (f.ontimeout = function() {
                                r({
                                    data: {
                                        code: "timeout"
                                    }
                                })
                            }
                            ,
                            f.onloadend = function() {
                                var e = f.response
                                  , n = f.readyState
                                  , o = f.responseURL
                                  , i = f.status
                                  , c = {
                                    response: e,
                                    readyState: n,
                                    responseURL: o,
                                    status: i,
                                    path: t.path
                                };
                                console.log("status::", f.status),
                                4 == f.readyState && f.status >= 200 && f.status < 400 ? r(c) : (cc.error(i),
                                s(i))
                            }
                            ,
                            t.formData) {
                                var d = new FormData;
                                for (var m in t.formData)
                                    d.append(m, t.formData[m]);
                                f.send(d)
                            } else
                                !t.data || "application/json" !== t.headers["content-type"] && "application/json" !== t.headers["Content-Type"] ? f.send(t.data) : f.send(JSON.stringify(t.data));
                            return [2]
                        }
                    })
                })
            }
            )
        }
        ,
        t.prototype.raw = function(t, e, n, o) {
            return void 0 === e && (e = "GET"),
            new Promise(function(r, i) {
                var s = new XMLHttpRequest;
                if (s.open(e, t),
                o)
                    for (var c in o)
                        null !== o[c] && void 0 !== o[c] && s.setRequestHeader(c, o[c]);
                s.onloadend = function() {
                    4 == s.readyState && s.status >= 200 && s.status < 400 ? v(s.response) ? r(JSON.parse(s.response)) : r(s.response) : i(s.status)
                }
                ,
                n && o && ("application/json" === o["content-type"] || "application/json" === o["Content-Type"]) ? s.send(JSON.stringify(n)) : s.send(n)
            }
            )
        }
        ,
        t.prototype.get = function(t, e) {
            return (e = e || {}).method = "GET",
            e.path = t,
            e.formData ? xysz.http.defaults.headers["content-type"] = null : xysz.http.defaults.headers["content-type"] = "application/json",
            e = this.mergeDefaultConfig(e),
            e = this.formatConfig(e),
            this.doRequest(e)
        }
        ,
        t.prototype.post = function(t, e, n) {
            return (n = n || {}).data = e,
            n.method = "POST",
            n.path = t,
            n.formData = n.data && n.data.formData ? n.data.formData : null,
            n.formData ? xysz.http.defaults.headers["content-type"] = null : xysz.http.defaults.headers["content-type"] = "application/json",
            n = this.mergeDefaultConfig(n),
            n = this.formatConfig(n),
            this.doRequest(n)
        }
        ,
        t.prototype.setRequestInterceptor = function(t) {
            this.requestFulfilled = t
        }
        ,
        t.prototype.setResponseInterceptor = function(t) {
            this.responseFulfilled = t
        }
        ,
        t
    }());
    function _(t, e) {
        return t(e = {
            exports: {}
        }, e.exports),
        e.exports
    }
    "undefined" != typeof globalThis ? globalThis : "undefined" != typeof window ? window : "undefined" != typeof global ? global : "undefined" != typeof self && self;
    var x = _(function(t) {
        (function() {
            function e(t) {
                this.mode = o.MODE_8BIT_BYTE,
                this.data = t
            }
            e.prototype = {
                getLength: function() {
                    return this.data.length
                },
                write: function(t) {
                    for (var e = 0; e < this.data.length; e++)
                        t.put(this.data.charCodeAt(e), 8)
                }
            };
            var n = function(t, e) {
                this.typeNumber = t,
                this.errorCorrectLevel = e,
                this.modules = null,
                this.moduleCount = 0,
                this.dataCache = null,
                this.dataList = new Array
            };
            t.exports && (t.exports = n),
            n.prototype = {
                addData: function(t) {
                    var n = new e(t);
                    this.dataList.push(n),
                    this.dataCache = null
                },
                isDark: function(t, e) {
                    if (t < 0 || this.moduleCount <= t || e < 0 || this.moduleCount <= e)
                        throw new Error(t + "," + e);
                    return this.modules[t][e]
                },
                getModuleCount: function() {
                    return this.moduleCount
                },
                make: function() {
                    if (this.typeNumber < 1) {
                        var t = 1;
                        for (t = 1; t < 40; t++) {
                            for (var e = a.getRSBlocks(t, this.errorCorrectLevel), n = new u, o = 0, i = 0; i < e.length; i++)
                                o += e[i].dataCount;
                            for (i = 0; i < this.dataList.length; i++) {
                                var s = this.dataList[i];
                                n.put(s.mode, 4),
                                n.put(s.getLength(), r.getLengthInBits(s.mode, t)),
                                s.write(n)
                            }
                            if (n.getLengthInBits() <= 8 * o)
                                break
                        }
                        this.typeNumber = t
                    }
                    this.makeImpl(!1, this.getBestMaskPattern())
                },
                makeImpl: function(t, e) {
                    this.moduleCount = 4 * this.typeNumber + 17,
                    this.modules = new Array(this.moduleCount);
                    for (var o = 0; o < this.moduleCount; o++) {
                        this.modules[o] = new Array(this.moduleCount);
                        for (var r = 0; r < this.moduleCount; r++)
                            this.modules[o][r] = null
                    }
                    this.setupPositionProbePattern(0, 0),
                    this.setupPositionProbePattern(this.moduleCount - 7, 0),
                    this.setupPositionProbePattern(0, this.moduleCount - 7),
                    this.setupPositionAdjustPattern(),
                    this.setupTimingPattern(),
                    this.setupTypeInfo(t, e),
                    this.typeNumber >= 7 && this.setupTypeNumber(t),
                    null == this.dataCache && (this.dataCache = n.createData(this.typeNumber, this.errorCorrectLevel, this.dataList)),
                    this.mapData(this.dataCache, e)
                },
                setupPositionProbePattern: function(t, e) {
                    for (var n = -1; n <= 7; n++)
                        if (!(t + n <= -1 || this.moduleCount <= t + n))
                            for (var o = -1; o <= 7; o++)
                                e + o <= -1 || this.moduleCount <= e + o || (this.modules[t + n][e + o] = 0 <= n && n <= 6 && (0 == o || 6 == o) || 0 <= o && o <= 6 && (0 == n || 6 == n) || 2 <= n && n <= 4 && 2 <= o && o <= 4)
                },
                getBestMaskPattern: function() {
                    for (var t = 0, e = 0, n = 0; n < 8; n++) {
                        this.makeImpl(!0, n);
                        var o = r.getLostPoint(this);
                        (0 == n || t > o) && (t = o,
                        e = n)
                    }
                    return e
                },
                createMovieClip: function(t, e, n) {
                    var o = t.createEmptyMovieClip(e, n);
                    this.make();
                    for (var r = 0; r < this.modules.length; r++)
                        for (var i = 1 * r, s = 0; s < this.modules[r].length; s++) {
                            var c = 1 * s;
                            this.modules[r][s] && (o.beginFill(0, 100),
                            o.moveTo(c, i),
                            o.lineTo(c + 1, i),
                            o.lineTo(c + 1, i + 1),
                            o.lineTo(c, i + 1),
                            o.endFill())
                        }
                    return o
                },
                setupTimingPattern: function() {
                    for (var t = 8; t < this.moduleCount - 8; t++)
                        null == this.modules[t][6] && (this.modules[t][6] = t % 2 == 0);
                    for (var e = 8; e < this.moduleCount - 8; e++)
                        null == this.modules[6][e] && (this.modules[6][e] = e % 2 == 0)
                },
                setupPositionAdjustPattern: function() {
                    for (var t = r.getPatternPosition(this.typeNumber), e = 0; e < t.length; e++)
                        for (var n = 0; n < t.length; n++) {
                            var o = t[e]
                              , i = t[n];
                            if (null == this.modules[o][i])
                                for (var s = -2; s <= 2; s++)
                                    for (var c = -2; c <= 2; c++)
                                        this.modules[o + s][i + c] = -2 == s || 2 == s || -2 == c || 2 == c || 0 == s && 0 == c
                        }
                },
                setupTypeNumber: function(t) {
                    for (var e = r.getBCHTypeNumber(this.typeNumber), n = 0; n < 18; n++) {
                        var o = !t && 1 == (e >> n & 1);
                        this.modules[Math.floor(n / 3)][n % 3 + this.moduleCount - 8 - 3] = o
                    }
                    for (n = 0; n < 18; n++)
                        o = !t && 1 == (e >> n & 1),
                        this.modules[n % 3 + this.moduleCount - 8 - 3][Math.floor(n / 3)] = o
                },
                setupTypeInfo: function(t, e) {
                    for (var n = this.errorCorrectLevel << 3 | e, o = r.getBCHTypeInfo(n), i = 0; i < 15; i++) {
                        var s = !t && 1 == (o >> i & 1);
                        i < 6 ? this.modules[i][8] = s : i < 8 ? this.modules[i + 1][8] = s : this.modules[this.moduleCount - 15 + i][8] = s
                    }
                    for (i = 0; i < 15; i++)
                        s = !t && 1 == (o >> i & 1),
                        i < 8 ? this.modules[8][this.moduleCount - i - 1] = s : i < 9 ? this.modules[8][15 - i - 1 + 1] = s : this.modules[8][15 - i - 1] = s;
                    this.modules[this.moduleCount - 8][8] = !t
                },
                mapData: function(t, e) {
                    for (var n = -1, o = this.moduleCount - 1, i = 7, s = 0, c = this.moduleCount - 1; c > 0; c -= 2)
                        for (6 == c && c--; ; ) {
                            for (var a = 0; a < 2; a++)
                                if (null == this.modules[o][c - a]) {
                                    var u = !1;
                                    s < t.length && (u = 1 == (t[s] >>> i & 1)),
                                    r.getMask(e, o, c - a) && (u = !u),
                                    this.modules[o][c - a] = u,
                                    -1 == --i && (s++,
                                    i = 7)
                                }
                            if ((o += n) < 0 || this.moduleCount <= o) {
                                o -= n,
                                n = -n;
                                break
                            }
                        }
                }
            },
            n.PAD0 = 236,
            n.PAD1 = 17,
            n.createData = function(t, e, o) {
                for (var i = a.getRSBlocks(t, e), s = new u, c = 0; c < o.length; c++) {
                    var l = o[c];
                    s.put(l.mode, 4),
                    s.put(l.getLength(), r.getLengthInBits(l.mode, t)),
                    l.write(s)
                }
                var h = 0;
                for (c = 0; c < i.length; c++)
                    h += i[c].dataCount;
                if (s.getLengthInBits() > 8 * h)
                    throw new Error("code length overflow. (" + s.getLengthInBits() + ">" + 8 * h + ")");
                for (s.getLengthInBits() + 4 <= 8 * h && s.put(0, 4); s.getLengthInBits() % 8 != 0; )
                    s.putBit(!1);
                for (; !(s.getLengthInBits() >= 8 * h || (s.put(n.PAD0, 8),
                s.getLengthInBits() >= 8 * h)); )
                    s.put(n.PAD1, 8);
                return n.createBytes(s, i)
            }
            ,
            n.createBytes = function(t, e) {
                for (var n = 0, o = 0, i = 0, s = new Array(e.length), a = new Array(e.length), u = 0; u < e.length; u++) {
                    var l = e[u].dataCount
                      , h = e[u].totalCount - l;
                    o = Math.max(o, l),
                    i = Math.max(i, h),
                    s[u] = new Array(l);
                    for (var f = 0; f < s[u].length; f++)
                        s[u][f] = 255 & t.buffer[f + n];
                    n += l;
                    var p = r.getErrorCorrectPolynomial(h)
                      , d = new c(s[u],p.getLength() - 1).mod(p);
                    for (a[u] = new Array(p.getLength() - 1),
                    f = 0; f < a[u].length; f++) {
                        var m = f + d.getLength() - a[u].length;
                        a[u][f] = m >= 0 ? d.get(m) : 0
                    }
                }
                var y = 0;
                for (f = 0; f < e.length; f++)
                    y += e[f].totalCount;
                var g = new Array(y)
                  , v = 0;
                for (f = 0; f < o; f++)
                    for (u = 0; u < e.length; u++)
                        f < s[u].length && (g[v++] = s[u][f]);
                for (f = 0; f < i; f++)
                    for (u = 0; u < e.length; u++)
                        f < a[u].length && (g[v++] = a[u][f]);
                return g
            }
            ;
            for (var o = {
                MODE_NUMBER: 1,
                MODE_ALPHA_NUM: 2,
                MODE_8BIT_BYTE: 4,
                MODE_KANJI: 8
            }, r = {
                PATTERN_POSITION_TABLE: [[], [6, 18], [6, 22], [6, 26], [6, 30], [6, 34], [6, 22, 38], [6, 24, 42], [6, 26, 46], [6, 28, 50], [6, 30, 54], [6, 32, 58], [6, 34, 62], [6, 26, 46, 66], [6, 26, 48, 70], [6, 26, 50, 74], [6, 30, 54, 78], [6, 30, 56, 82], [6, 30, 58, 86], [6, 34, 62, 90], [6, 28, 50, 72, 94], [6, 26, 50, 74, 98], [6, 30, 54, 78, 102], [6, 28, 54, 80, 106], [6, 32, 58, 84, 110], [6, 30, 58, 86, 114], [6, 34, 62, 90, 118], [6, 26, 50, 74, 98, 122], [6, 30, 54, 78, 102, 126], [6, 26, 52, 78, 104, 130], [6, 30, 56, 82, 108, 134], [6, 34, 60, 86, 112, 138], [6, 30, 58, 86, 114, 142], [6, 34, 62, 90, 118, 146], [6, 30, 54, 78, 102, 126, 150], [6, 24, 50, 76, 102, 128, 154], [6, 28, 54, 80, 106, 132, 158], [6, 32, 58, 84, 110, 136, 162], [6, 26, 54, 82, 110, 138, 166], [6, 30, 58, 86, 114, 142, 170]],
                G15: 1335,
                G18: 7973,
                G15_MASK: 21522,
                getBCHTypeInfo: function(t) {
                    for (var e = t << 10; r.getBCHDigit(e) - r.getBCHDigit(r.G15) >= 0; )
                        e ^= r.G15 << r.getBCHDigit(e) - r.getBCHDigit(r.G15);
                    return (t << 10 | e) ^ r.G15_MASK
                },
                getBCHTypeNumber: function(t) {
                    for (var e = t << 12; r.getBCHDigit(e) - r.getBCHDigit(r.G18) >= 0; )
                        e ^= r.G18 << r.getBCHDigit(e) - r.getBCHDigit(r.G18);
                    return t << 12 | e
                },
                getBCHDigit: function(t) {
                    for (var e = 0; 0 != t; )
                        e++,
                        t >>>= 1;
                    return e
                },
                getPatternPosition: function(t) {
                    return r.PATTERN_POSITION_TABLE[t - 1]
                },
                getMask: function(t, e, n) {
                    switch (t) {
                    case 0:
                        return (e + n) % 2 == 0;
                    case 1:
                        return e % 2 == 0;
                    case 2:
                        return n % 3 == 0;
                    case 3:
                        return (e + n) % 3 == 0;
                    case 4:
                        return (Math.floor(e / 2) + Math.floor(n / 3)) % 2 == 0;
                    case 5:
                        return e * n % 2 + e * n % 3 == 0;
                    case 6:
                        return (e * n % 2 + e * n % 3) % 2 == 0;
                    case 7:
                        return (e * n % 3 + (e + n) % 2) % 2 == 0;
                    default:
                        throw new Error("bad maskPattern:" + t)
                    }
                },
                getErrorCorrectPolynomial: function(t) {
                    for (var e = new c([1],0), n = 0; n < t; n++)
                        e = e.multiply(new c([1, i.gexp(n)],0));
                    return e
                },
                getLengthInBits: function(t, e) {
                    if (1 <= e && e < 10)
                        switch (t) {
                        case o.MODE_NUMBER:
                            return 10;
                        case o.MODE_ALPHA_NUM:
                            return 9;
                        case o.MODE_8BIT_BYTE:
                        case o.MODE_KANJI:
                            return 8;
                        default:
                            throw new Error("mode:" + t)
                        }
                    else if (e < 27)
                        switch (t) {
                        case o.MODE_NUMBER:
                            return 12;
                        case o.MODE_ALPHA_NUM:
                            return 11;
                        case o.MODE_8BIT_BYTE:
                            return 16;
                        case o.MODE_KANJI:
                            return 10;
                        default:
                            throw new Error("mode:" + t)
                        }
                    else {
                        if (!(e < 41))
                            throw new Error("type:" + e);
                        switch (t) {
                        case o.MODE_NUMBER:
                            return 14;
                        case o.MODE_ALPHA_NUM:
                            return 13;
                        case o.MODE_8BIT_BYTE:
                            return 16;
                        case o.MODE_KANJI:
                            return 12;
                        default:
                            throw new Error("mode:" + t)
                        }
                    }
                },
                getLostPoint: function(t) {
                    for (var e = t.getModuleCount(), n = 0, o = 0; o < e; o++)
                        for (var r = 0; r < e; r++) {
                            for (var i = 0, s = t.isDark(o, r), c = -1; c <= 1; c++)
                                if (!(o + c < 0 || e <= o + c))
                                    for (var a = -1; a <= 1; a++)
                                        r + a < 0 || e <= r + a || 0 == c && 0 == a || s == t.isDark(o + c, r + a) && i++;
                            i > 5 && (n += 3 + i - 5)
                        }
                    for (o = 0; o < e - 1; o++)
                        for (r = 0; r < e - 1; r++) {
                            var u = 0;
                            t.isDark(o, r) && u++,
                            t.isDark(o + 1, r) && u++,
                            t.isDark(o, r + 1) && u++,
                            t.isDark(o + 1, r + 1) && u++,
                            0 != u && 4 != u || (n += 3)
                        }
                    for (o = 0; o < e; o++)
                        for (r = 0; r < e - 6; r++)
                            t.isDark(o, r) && !t.isDark(o, r + 1) && t.isDark(o, r + 2) && t.isDark(o, r + 3) && t.isDark(o, r + 4) && !t.isDark(o, r + 5) && t.isDark(o, r + 6) && (n += 40);
                    for (r = 0; r < e; r++)
                        for (o = 0; o < e - 6; o++)
                            t.isDark(o, r) && !t.isDark(o + 1, r) && t.isDark(o + 2, r) && t.isDark(o + 3, r) && t.isDark(o + 4, r) && !t.isDark(o + 5, r) && t.isDark(o + 6, r) && (n += 40);
                    var l = 0;
                    for (r = 0; r < e; r++)
                        for (o = 0; o < e; o++)
                            t.isDark(o, r) && l++;
                    return n + Math.abs(100 * l / e / e - 50) / 5 * 10
                }
            }, i = {
                glog: function(t) {
                    if (t < 1)
                        throw new Error("glog(" + t + ")");
                    return i.LOG_TABLE[t]
                },
                gexp: function(t) {
                    for (; t < 0; )
                        t += 255;
                    for (; t >= 256; )
                        t -= 255;
                    return i.EXP_TABLE[t]
                },
                EXP_TABLE: new Array(256),
                LOG_TABLE: new Array(256)
            }, s = 0; s < 8; s++)
                i.EXP_TABLE[s] = 1 << s;
            for (s = 8; s < 256; s++)
                i.EXP_TABLE[s] = i.EXP_TABLE[s - 4] ^ i.EXP_TABLE[s - 5] ^ i.EXP_TABLE[s - 6] ^ i.EXP_TABLE[s - 8];
            for (s = 0; s < 255; s++)
                i.LOG_TABLE[i.EXP_TABLE[s]] = s;
            function c(t, e) {
                if (null == t.length)
                    throw new Error(t.length + "/" + e);
                for (var n = 0; n < t.length && 0 == t[n]; )
                    n++;
                this.num = new Array(t.length - n + e);
                for (var o = 0; o < t.length - n; o++)
                    this.num[o] = t[o + n]
            }
            function a(t, e) {
                this.totalCount = t,
                this.dataCount = e
            }
            function u() {
                this.buffer = new Array,
                this.length = 0
            }
            c.prototype = {
                get: function(t) {
                    return this.num[t]
                },
                getLength: function() {
                    return this.num.length
                },
                multiply: function(t) {
                    for (var e = new Array(this.getLength() + t.getLength() - 1), n = 0; n < this.getLength(); n++)
                        for (var o = 0; o < t.getLength(); o++)
                            e[n + o] ^= i.gexp(i.glog(this.get(n)) + i.glog(t.get(o)));
                    return new c(e,0)
                },
                mod: function(t) {
                    if (this.getLength() - t.getLength() < 0)
                        return this;
                    for (var e = i.glog(this.get(0)) - i.glog(t.get(0)), n = new Array(this.getLength()), o = 0; o < this.getLength(); o++)
                        n[o] = this.get(o);
                    for (o = 0; o < t.getLength(); o++)
                        n[o] ^= i.gexp(i.glog(t.get(o)) + e);
                    return new c(n,0).mod(t)
                }
            },
            a.RS_BLOCK_TABLE = [[1, 26, 19], [1, 26, 16], [1, 26, 13], [1, 26, 9], [1, 44, 34], [1, 44, 28], [1, 44, 22], [1, 44, 16], [1, 70, 55], [1, 70, 44], [2, 35, 17], [2, 35, 13], [1, 100, 80], [2, 50, 32], [2, 50, 24], [4, 25, 9], [1, 134, 108], [2, 67, 43], [2, 33, 15, 2, 34, 16], [2, 33, 11, 2, 34, 12], [2, 86, 68], [4, 43, 27], [4, 43, 19], [4, 43, 15], [2, 98, 78], [4, 49, 31], [2, 32, 14, 4, 33, 15], [4, 39, 13, 1, 40, 14], [2, 121, 97], [2, 60, 38, 2, 61, 39], [4, 40, 18, 2, 41, 19], [4, 40, 14, 2, 41, 15], [2, 146, 116], [3, 58, 36, 2, 59, 37], [4, 36, 16, 4, 37, 17], [4, 36, 12, 4, 37, 13], [2, 86, 68, 2, 87, 69], [4, 69, 43, 1, 70, 44], [6, 43, 19, 2, 44, 20], [6, 43, 15, 2, 44, 16], [4, 101, 81], [1, 80, 50, 4, 81, 51], [4, 50, 22, 4, 51, 23], [3, 36, 12, 8, 37, 13], [2, 116, 92, 2, 117, 93], [6, 58, 36, 2, 59, 37], [4, 46, 20, 6, 47, 21], [7, 42, 14, 4, 43, 15], [4, 133, 107], [8, 59, 37, 1, 60, 38], [8, 44, 20, 4, 45, 21], [12, 33, 11, 4, 34, 12], [3, 145, 115, 1, 146, 116], [4, 64, 40, 5, 65, 41], [11, 36, 16, 5, 37, 17], [11, 36, 12, 5, 37, 13], [5, 109, 87, 1, 110, 88], [5, 65, 41, 5, 66, 42], [5, 54, 24, 7, 55, 25], [11, 36, 12], [5, 122, 98, 1, 123, 99], [7, 73, 45, 3, 74, 46], [15, 43, 19, 2, 44, 20], [3, 45, 15, 13, 46, 16], [1, 135, 107, 5, 136, 108], [10, 74, 46, 1, 75, 47], [1, 50, 22, 15, 51, 23], [2, 42, 14, 17, 43, 15], [5, 150, 120, 1, 151, 121], [9, 69, 43, 4, 70, 44], [17, 50, 22, 1, 51, 23], [2, 42, 14, 19, 43, 15], [3, 141, 113, 4, 142, 114], [3, 70, 44, 11, 71, 45], [17, 47, 21, 4, 48, 22], [9, 39, 13, 16, 40, 14], [3, 135, 107, 5, 136, 108], [3, 67, 41, 13, 68, 42], [15, 54, 24, 5, 55, 25], [15, 43, 15, 10, 44, 16], [4, 144, 116, 4, 145, 117], [17, 68, 42], [17, 50, 22, 6, 51, 23], [19, 46, 16, 6, 47, 17], [2, 139, 111, 7, 140, 112], [17, 74, 46], [7, 54, 24, 16, 55, 25], [34, 37, 13], [4, 151, 121, 5, 152, 122], [4, 75, 47, 14, 76, 48], [11, 54, 24, 14, 55, 25], [16, 45, 15, 14, 46, 16], [6, 147, 117, 4, 148, 118], [6, 73, 45, 14, 74, 46], [11, 54, 24, 16, 55, 25], [30, 46, 16, 2, 47, 17], [8, 132, 106, 4, 133, 107], [8, 75, 47, 13, 76, 48], [7, 54, 24, 22, 55, 25], [22, 45, 15, 13, 46, 16], [10, 142, 114, 2, 143, 115], [19, 74, 46, 4, 75, 47], [28, 50, 22, 6, 51, 23], [33, 46, 16, 4, 47, 17], [8, 152, 122, 4, 153, 123], [22, 73, 45, 3, 74, 46], [8, 53, 23, 26, 54, 24], [12, 45, 15, 28, 46, 16], [3, 147, 117, 10, 148, 118], [3, 73, 45, 23, 74, 46], [4, 54, 24, 31, 55, 25], [11, 45, 15, 31, 46, 16], [7, 146, 116, 7, 147, 117], [21, 73, 45, 7, 74, 46], [1, 53, 23, 37, 54, 24], [19, 45, 15, 26, 46, 16], [5, 145, 115, 10, 146, 116], [19, 75, 47, 10, 76, 48], [15, 54, 24, 25, 55, 25], [23, 45, 15, 25, 46, 16], [13, 145, 115, 3, 146, 116], [2, 74, 46, 29, 75, 47], [42, 54, 24, 1, 55, 25], [23, 45, 15, 28, 46, 16], [17, 145, 115], [10, 74, 46, 23, 75, 47], [10, 54, 24, 35, 55, 25], [19, 45, 15, 35, 46, 16], [17, 145, 115, 1, 146, 116], [14, 74, 46, 21, 75, 47], [29, 54, 24, 19, 55, 25], [11, 45, 15, 46, 46, 16], [13, 145, 115, 6, 146, 116], [14, 74, 46, 23, 75, 47], [44, 54, 24, 7, 55, 25], [59, 46, 16, 1, 47, 17], [12, 151, 121, 7, 152, 122], [12, 75, 47, 26, 76, 48], [39, 54, 24, 14, 55, 25], [22, 45, 15, 41, 46, 16], [6, 151, 121, 14, 152, 122], [6, 75, 47, 34, 76, 48], [46, 54, 24, 10, 55, 25], [2, 45, 15, 64, 46, 16], [17, 152, 122, 4, 153, 123], [29, 74, 46, 14, 75, 47], [49, 54, 24, 10, 55, 25], [24, 45, 15, 46, 46, 16], [4, 152, 122, 18, 153, 123], [13, 74, 46, 32, 75, 47], [48, 54, 24, 14, 55, 25], [42, 45, 15, 32, 46, 16], [20, 147, 117, 4, 148, 118], [40, 75, 47, 7, 76, 48], [43, 54, 24, 22, 55, 25], [10, 45, 15, 67, 46, 16], [19, 148, 118, 6, 149, 119], [18, 75, 47, 31, 76, 48], [34, 54, 24, 34, 55, 25], [20, 45, 15, 61, 46, 16]],
            a.getRSBlocks = function(t, e) {
                var n = a.getRsBlockTable(t, e);
                if (null == n)
                    throw new Error("bad rs block @ typeNumber:" + t + "/errorCorrectLevel:" + e);
                for (var o = n.length / 3, r = new Array, i = 0; i < o; i++)
                    for (var s = n[3 * i + 0], c = n[3 * i + 1], u = n[3 * i + 2], l = 0; l < s; l++)
                        r.push(new a(c,u));
                return r
            }
            ,
            a.getRsBlockTable = function(t, e) {
                switch (e) {
                case 1:
                    return a.RS_BLOCK_TABLE[4 * (t - 1) + 0];
                case 0:
                    return a.RS_BLOCK_TABLE[4 * (t - 1) + 1];
                case 3:
                    return a.RS_BLOCK_TABLE[4 * (t - 1) + 2];
                case 2:
                    return a.RS_BLOCK_TABLE[4 * (t - 1) + 3];
                default:
                    return
                }
            }
            ,
            u.prototype = {
                get: function(t) {
                    var e = Math.floor(t / 8);
                    return 1 == (this.buffer[e] >>> 7 - t % 8 & 1)
                },
                put: function(t, e) {
                    for (var n = 0; n < e; n++)
                        this.putBit(1 == (t >>> e - n - 1 & 1))
                },
                getLengthInBits: function() {
                    return this.length
                },
                putBit: function(t) {
                    var e = Math.floor(this.length / 8);
                    this.buffer.length <= e && this.buffer.push(0),
                    t && (this.buffer[e] |= 128 >>> this.length % 8),
                    this.length++
                }
            }
        }
        )()
    })
      , b = function() {
        function t() {}
        return t.getRangeValue = function(t, e) {
            return Math.floor(Math.random() * (e - t + 1)) + t
        }
        ,
        t.getPosBaseCenter = function(t, e) {
            return e - t / 2 + .5
        }
        ,
        t.randomValue = function(t) {
            return Math.floor(Math.random() * t)
        }
        ,
        t.convertToColor = function(t) {
            return cc.color().fromHEX(t)
        }
        ,
        t.adjustMaxLength = function(t, e) {
            if (t.spriteFrame) {
                var n = t.spriteFrame.getRect();
                if (e instanceof cc.Size) {
                    var o = e
                      , r = Math.min(o.width / n.width, o.height / n.height);
                    t.node.width = n.width * r,
                    t.node.height = n.height * r
                } else if ("number" == typeof e) {
                    var i = e;
                    r = Math.min(i / n.width, i / n.height),
                    t.node.width = n.width * r,
                    t.node.height = n.height * r
                }
            }
        }
        ,
        t.bindWechatAvatar = function(t, e, n) {
            return e ? this.bindImageToSprite(t, e + "?aaa=aa.jpg", n) : Promise.resolve(null)
        }
        ,
        t.bindImageToSprite = function(e, n, o) {
            return r(this, void 0, Promise, function() {
                function s(n) {
                    e.isValid && (n.packable = !1,
                    e.spriteFrame = new cc.SpriteFrame(n),
                    t.adjustMaxLength(e, o))
                }
                var c = this;
                return i(this, function() {
                    return e.spriteFrame = null,
                    n && n.length ? [2, new Promise(function(t, e) {
                        return r(c, void 0, void 0, function() {
                            return i(this, function(o) {
                                switch (o.label) {
                                case 0:
                                    return n.startsWith("http") ? (cc.assetManager.loadRemote(n, function(n, o) {
                                        n ? e() : (s(o),
                                        t(null))
                                    }),
                                    [3, 4]) : [3, 1];
                                case 1:
                                    return n ? (n.startsWith("data:") || (n = "data:image/png;base64," + n),
                                    [4, xysz.res.base64ToTexture(n)]) : [3, 3];
                                case 2:
                                    return s(o.sent()),
                                    t(null),
                                    [3, 4];
                                case 3:
                                    t(null),
                                    o.label = 4;
                                case 4:
                                    return [2]
                                }
                            })
                        })
                    }
                    )] : [2]
                })
            })
        }
        ,
        t.convertToCanvasBox = function(t) {
            var e = cc.view.getViewportRect().clone()
              , n = t.clone();
            n.y = cc.winSize.height - n.y - t.height;
            var o = e.height / cc.winSize.height;
            return n.x = n.x * o + e.x,
            n.y = n.y * o + e.y,
            n.width *= o,
            n.height *= o,
            n
        }
        ,
        t.convertToDeviceBox = function(t) {
            var e = t.clone();
            e.y = cc.winSize.height - e.y - t.height;
            var n = cc.view.getViewportRect().clone();
            n.x /= cc.view.getDevicePixelRatio(),
            n.y /= cc.view.getDevicePixelRatio(),
            n.width /= cc.view.getDevicePixelRatio(),
            n.height /= cc.view.getDevicePixelRatio();
            var o = n.height / cc.winSize.height;
            return e.x = e.x * o + n.x,
            e.y = e.y * o + n.y,
            e.width *= o,
            e.height *= o,
            e
        }
        ,
        t.getSortedQuery = function(t) {
            var e = Object.keys(t).sort()
              , n = "";
            return e.forEach(function(e) {
                if (t[e] || 0 === t[e]) {
                    var o;
                    o = t[e]instanceof Object ? e + "=" + JSON.stringify(t[e]) : e + "=" + t[e],
                    n && o && (n += "&"),
                    n += o
                }
            }),
            n
        }
        ,
        t.generateNoncestr = function(t) {
            void 0 === t && (t = 32);
            for (var e = "", n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], o = 0; o < t; o++)
                e += n[Math.round(Math.random() * (n.length - 1))];
            return e
        }
        ,
        t.throttle = function(t, e) {
            void 0 === e && (e = 1e3);
            var n = 0;
            return function() {
                var o = this
                  , r = arguments
                  , i = Date.now();
                i - n >= e && (t.apply(o, r),
                n = Date.now())
            }
        }
        ,
        t.debounce = function(t, e, n) {
            var o, r;
            return void 0 === e && (e = 1e3),
            void 0 === n && (n = !1),
            function() {
                var i = this
                  , s = arguments;
                if (o && clearTimeout(o),
                n) {
                    var c = !o;
                    o = setTimeout(function() {
                        o = null
                    }, e),
                    c && (r = t.apply(i, s))
                } else
                    o = setTimeout(function() {
                        t.apply(i, s)
                    }, e);
                return r
            }
        }
        ,
        t.parseQuery = function(t) {
            t.startsWith("?") && (t = t.substr(1));
            var e = {};
            return t ? (t.split("&").forEach(function(t) {
                if (/=/.test(t)) {
                    var n = t.split("=")
                      , o = n[0]
                      , r = n[1];
                    e.hasOwnProperty(o) ? e[o] = [].concat(e[o], r) : e[o] = r
                } else
                    e[t] = !0
            }),
            e) : {}
        }
        ,
        t.worldDistance = function(t, e, n, o) {
            e = e || 0,
            n = n || 0,
            o = o || 0;
            var r = (t = t || 0) * Math.PI / 180
              , i = n * Math.PI / 180
              , s = r - i
              , c = e * Math.PI / 180 - o * Math.PI / 180;
            return 12756274 * Math.asin(Math.sqrt(Math.pow(Math.sin(s / 2), 2) + Math.cos(r) * Math.cos(i) * Math.pow(Math.sin(c / 2), 2)))
        }
        ,
        t.isLongScreen = function() {
            return cc.winSize.height / cc.winSize.width > 2
        }
        ,
        t.scheduleCallback = function(t, e, n, o) {
            if (void 0 === o && (o = 0),
            e > 0) {
                var r = 0;
                t.schedule(function() {
                    return n(r++)
                }, o, e - 1)
            }
        }
        ,
        t.getWorldPos = function(t) {
            return t.convertToWorldSpaceAR(cc.Vec3.ZERO).sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2))
        }
        ,
        t.asyncDelay = function(t, e) {
            return new Promise(function(n) {
                return t.scheduleOnce(n, e)
            }
            )
        }
        ,
        t.tweenDelay = function(t) {
            return void 0 === t && (t = 0),
            new Promise(function(e) {
                return cc.tween({}).delay(t).call(e).start()
            }
            )
        }
        ,
        t.optimizeUnit = function(t) {
            for (var e = t.childrenCount, n = 0; n < e; n++) {
                var o = t.children[0];
                o.parent = t.parent,
                o.zIndex = n + 1,
                o.scale *= t.scale,
                o.x = t.x + o.x * t.scale,
                o.y = t.y + o.y * t.scale
            }
        }
        ,
        t.formatNickname = function(t, e) {
            return t ? t.length > e ? t.substr(0, e) + "..." : t : ""
        }
        ,
        t.drawQRCode = function(t, e) {
            if (t && e && x) {
                var n = new x(-1,0);
                n.addData(t),
                n.make();
                var o = e;
                o.fillColor = cc.Color.WHITE,
                o.rect(-e.node.width / 2, -e.node.height / 2, e.node.width, e.node.height),
                o.fill();
                var r = e.node.width - 10
                  , i = e.node.height - 10;
                o.fillColor = cc.Color.BLACK;
                for (var s = r / n.getModuleCount(), c = i / n.getModuleCount(), a = 0; a < n.getModuleCount(); a++)
                    for (var u = 0; u < n.getModuleCount(); u++)
                        if (n.isDark(a, u)) {
                            var l = Math.ceil((u + 1) * s) - Math.floor(u * s)
                              , h = Math.ceil((a + 1) * s) - Math.floor(a * s);
                            o.rect(Math.round(u * s) - r / 2, Math.round(a * c) - i / 2, l, h),
                            o.fill()
                        }
            } else
                console.log("\u8bf7\u5148\u52a0\u8f7dQRCode\u7b2c\u4e09\u65b9\u4ee3\u7801\u5e93")
        }
        ,
        t.pairOfflineScreen = function() {
            cc.Canvas.instance.node.scaleX = cc.winSize.width / cc.Canvas.instance.designResolution.width
        }
        ,
        t.getScreenOrientation = function() {
            return cc.winSize.width > cc.winSize.height ? 0 : 1
        }
        ,
        t.listenToggleContainer = function(t, e, n) {
            t.toggleItems.forEach(function(o) {
                o.node.on("toggle", function(o) {
                    var r = t.toggleItems.indexOf(o);
                    t.toggleItems.forEach(function(t) {
                        return t.interactable = !0
                    }),
                    t.toggleItems[r].interactable = !1,
                    e.call(n, r)
                })
            })
        }
        ,
        t.manualModifyToggleTab = function(t, e) {
            t.toggleItems.forEach(function(t, n) {
                t.interactable = n !== e,
                t.isChecked = n == e
            })
        }
        ,
        t.flyTween = function(t, e, n, o) {
            void 0 === o && (o = 1);
            for (var r = e.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), i = n.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), s = function() {
                var e = cc.instantiate(t);
                e.parent = cc.Canvas.instance.node,
                e.zIndex = 100,
                e.position = r,
                e.active = !0,
                cc.tween(e).delay(.5 * Math.random()).to(.8, {
                    position: i
                }).call(function() {
                    return e.destroy()
                }).start()
            }, c = 0; c < o; c++)
                s();
            return new Promise(function(t) {
                cc.tween({}).delay(1).call(t).start()
            }
            )
        }
        ,
        t.circleFlyTween = function(t, e, n, o) {
            void 0 === o && (o = 1);
            for (var r = e.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), i = n.sub(cc.v3(cc.winSize.width / 2, cc.winSize.height / 2)), s = function(e) {
                var n = cc.instantiate(t);
                n.parent = cc.Canvas.instance.node;
                var s = Math.PI / 180 * Math.round(360 / o)
                  , c = r.x + 100 * Math.sin(s * e)
                  , a = r.y + 100 * Math.cos(s * e);
                n.position = r,
                n.active = !0,
                n.zIndex = 100,
                cc.tween(n).to(.05, {
                    position: cc.v3(c, a)
                }).call(function() {
                    cc.tween(n).delay(.2 * Math.random()).to(.8, {
                        position: i
                    }).call(function() {
                        return n.destroy()
                    }).start()
                }).start()
            }, c = 0; c < o; c++)
                s(c);
            return new Promise(function(t) {
                cc.tween({}).delay(1).call(t).start()
            }
            )
        }
        ,
        t.convertListTotalToSeparate = function(t) {
            for (var e = [], n = t.length - 1; n >= 0; n--)
                e.unshift(t[n] - (t[n - 1] || 0));
            return e
        }
        ,
        t.convertListSeparateToTotal = function(t) {
            for (var e = [], n = 0; n < t.length; n++)
                e.push(t[n] + (t[n - 1] || 0));
            return e
        }
        ,
        t.progressNearOne = function(t, e) {
            var n = Date.now();
            t.schedule(function() {
                var t = 1 - 1 / (1 + (Date.now() - n) / 1e3);
                e(Math.max(t, .01))
            })
        }
        ,
        t.drawGraphicsShadow = function(t, e) {
            void 0 === e && (e = cc.color(0, 0, 0, 192));
            var n = t.getComponent(cc.Graphics);
            n || (n = t.addComponent(cc.Graphics));
            var o = t.getBoundingBox();
            n.fillColor = e,
            n.rect(o.x, o.y, o.width, o.height),
            n.fill()
        }
        ,
        t.nodeVisibility = function(t, e) {
            for (var n = 0, o = t.length; n < o; n++) {
                var r = t[n]
                  , i = r.convertToWorldSpaceAR(cc.v2(0, r.height - r.height * r.anchorY))
                  , s = r.convertToWorldSpaceAR(cc.v2(0, -r.height * r.anchorY))
                  , c = e.convertToNodeSpaceAR(i)
                  , a = e.convertToNodeSpaceAR(s);
                c.y > -e.height * e.anchorY && a.y < e.height - e.height * e.anchorY ? r.opacity = 255 : r.opacity = 0
            }
        }
        ,
        t.listenDataChange = function(t, e) {
            e.forEach(function(e) {
                Object.defineProperty(t, e.key, {
                    get: function() {
                        return t._store = t._store || {},
                        t._store[e.key]
                    },
                    set: function(n) {
                        if (t._store = t._store || {},
                        e.modifyFunc) {
                            var o = e.modifyFunc(n, t._store[e.key]);
                            o && (n = o)
                        }
                        t._store[e.key] = n,
                        e.boardcast && cc.game.emit(e.boardcast, n)
                    }
                })
            })
        }
        ,
        t.generateOptimizeVerticleScrollView = function(t) {
            if (t.sv.content.getComponent(cc.Layout) && t.sv.content.getComponent(cc.Layout).enabled)
                cc.error("generateOptimizeVerticleScrollView\u51fd\u6570\u7684sv\u4e0d\u80fd\u4f7f\u7528Layout\u7ec4\u4ef6");
            else {
                var e = t.paddingTop || 0
                  , n = t.paddingBottom || 0
                  , o = t.spacingY || 0
                  , r = t.pfb.data.height + o;
                t.sv.content.anchorY = 1,
                t.sv.content.height = t.maxCount * r + e + n - o;
                for (var i = Math.min(Math.ceil(t.sv.content.parent.height / r) + 1, t.maxCount), s = 0; s < i; s++) {
                    var c = cc.instantiate(t.pfb);
                    c.y = (s + .5) * -r - e + .5 * o,
                    c.parent = t.sv.content,
                    t.func(c, s)
                }
                var a = 0;
                t.sv.node.on("scrolling", function() {
                    var n = a;
                    if (a = Math.floor((t.sv.content.y - t.sv.node.height / 2) / r),
                    a = Math.min(a, t.maxCount - i),
                    (a = Math.max(a, 0)) > n) {
                        a = n + 1;
                        var s = t.sv.content.children.shift();
                        t.sv.content.children.push(s),
                        s.y = (a - .5 + i) * -r - e + .5 * o,
                        t.func(s, a + i - 1)
                    } else
                        a < n && (a = n - 1,
                        s = t.sv.content.children.pop(),
                        t.sv.content.children.unshift(s),
                        s.y = (a + .5) * -r - e + .5 * o,
                        t.func(s, a))
                })
            }
        }
        ,
        t.asyncModifyChildren = function(t, e, n, o, r) {
            var i = e.children.filter(function(t) {
                return t.name === n.name
            }).length
              , s = i - o;
            if (s > 0)
                for (var c = 0; c < s; c++) {
                    var a = e.children.find(function(t) {
                        return t.name === n.name
                    });
                    a && e.removeChild(a)
                }
            var u = e.children.filter(function(t) {
                return t.name === n.name
            });
            u.forEach(r);
            var l = o - i;
            if (l > 0) {
                var h = 0;
                t.schedule(function() {
                    var t = cc.instantiate(n);
                    t.name = n.name,
                    e.addChild(t),
                    r(t, u.length + h),
                    h++
                }, 0, l - 1)
            }
        }
        ,
        t.getNodePath = function(t) {
            for (var e = ""; t; )
                e = "/" + t.name + e,
                t = t.parent;
            return e
        }
        ,
        t.globalSchedule = function(t, e) {
            var n = new cc.Node;
            cc.game.addPersistRootNode(n),
            n.addComponent(cc.Component).schedule(t, e)
        }
        ,
        t.mergeUrl = function(t, e) {
            return t.endsWith("/") || (t += "/"),
            e.startsWith("/") && (e = e.substr(1)),
            t + e
        }
        ,
        t.darkComponent = function(t) {
            t.setMaterial(0, cc.Material.getBuiltinMaterial("2d-gray-sprite"))
        }
        ,
        t.colorSprite = function(t) {
            t.setMaterial(0, cc.Material.getBuiltinMaterial("2d-sprite"))
        }
        ,
        t.randomColor = function(t) {
            return void 0 === t && (t = !1),
            cc.color(xysz.tool.randomValue(255), xysz.tool.randomValue(255), xysz.tool.randomValue(255), t ? xysz.tool.randomValue(255) : 255)
        }
        ,
        t.isValidIP = function(t) {
            return /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/.test(t)
        }
        ,
        t.bindTbAvatar = function(e, n, o) {
            var s = this;
            if (n && n.length)
                return new Promise(function(t, e) {
                    return r(s, void 0, void 0, function() {
                        return i(this, function() {
                            return n.startsWith("http") && cc.assetManager.loadRemote(n, {
                                ext: ".png"
                            }, function(n, o) {
                                n ? e() : (c(o),
                                t(null))
                            }),
                            [2]
                        })
                    })
                }
                );
            function c(n) {
                e.isValid && (n.packable = !1,
                e.spriteFrame = new cc.SpriteFrame(n),
                t.adjustMaxLength(e, o))
            }
        }
        ,
        t.tbAddToLog = function(t, e) {
            xysz.tbLog[t] = e
        }
        ,
        t
    }();
    function C(t, e) {
        var n = S(JSON.stringify(e))
          , o = n.length + 3
          , r = new Uint8Array(o + 4)
          , i = 0;
        return r[i++] = o >> 24 & 255,
        r[i++] = o >> 16 & 255,
        r[i++] = o >> 8 & 255,
        r[i++] = 255 & o,
        r[i++] = 1,
        r[i++] = t >> 8 & 255,
        r[i++] = 255 & t,
        P(r, 7, n, 0, n.length),
        r
    }
    function S(t) {
        for (var e = [], n = 0; n < t.length; n++) {
            var o = t.charCodeAt(n);
            o <= 127 ? e.push(o) : o <= 2047 ? e.push(192 | o >> 6, 128 | 63 & o) : o <= 65535 ? e.push(224 | o >> 12, 128 | (4032 & o) >> 6, 128 | 63 & o) : e.push(240 | o >> 18, 128 | (258048 & o) >> 12, 128 | (4032 & o) >> 6, 128 | 63 & o)
        }
        return new Uint8Array(e)
    }
    function z(t) {
        for (var e = [], n = 0, o = 0, r = t.length; n < r; )
            t[n] < 128 ? (o = t[n],
            n += 1) : t[n] < 224 ? (o = ((63 & t[n]) << 6) + (63 & t[n + 1]),
            n += 2) : t[n] < 240 ? (o = ((15 & t[n]) << 12) + ((63 & t[n + 1]) << 6) + (63 & t[n + 2]),
            n += 3) : (o = ((7 & t[n]) << 18) + ((63 & t[n + 1]) << 12) + ((63 & t[n + 1]) << 6) + (63 & t[n + 2]),
            n += 4),
            e.push(o);
        return String.fromCharCode.apply(null, e)
    }
    function P(t, e, n, o, r) {
        for (var i = 0; i < r; i++)
            t[e++] = n[o++]
    }
    var k, B = new (function() {
        function t() {
            this._ws = null,
            this._info = null,
            this._silenceCheckTime = 4e3,
            this._connectCheckTime = 3e3,
            this._recvCheckTime = 8e3,
            this._connectTimer = null,
            this._silenceTimer = null,
            this._recvTimer = null,
            this.connect = b.throttle(this.connect.bind(this)),
            this.disconnect = b.throttle(this.disconnect.bind(this))
        }
        return t.prototype.create = function() {
            return new t
        }
        ,
        t.prototype.initInfo = function(t) {
            this._info = t,
            this._info.flag = t.flag || b.generateNoncestr()
        }
        ,
        t.prototype.connect = function() {
            var t = this;
            if (cc.log("sock - connect()"),
            !this._info.address)
                throw new Error("pleast call initAddress() first");
            this._ws = new WebSocket(this._info.address),
            this._info.binaryType && (this._ws.binaryType = this._info.binaryType),
            this._ws.onopen = function() {
                cc.log("onopen"),
                t.stopConnectCheck(),
                t.startSilenceCheck(),
                cc.game.emit(c.SocketInfo, {
                    _sub: s.Socket.Open,
                    flag: t._info.flag
                })
            }
            ,
            this._ws.onmessage = function(e) {
                if (t.stopRecvCheck(),
                t.startSilenceCheck(),
                !t.recvFulfilled)
                    throw new Error("\u63a5\u6536\u6d88\u606f\u8bf7\u5148\u8bbe\u7f6e\u6570\u636e\u89e3\u5bc6\u65b9\u6cd5 -> setRecvInterceptor()");
                var n = t.recvFulfilled(e.data);
                if (n instanceof Error) {
                    if (!t.recvRejected)
                        throw n;
                    t.recvRejected(n)
                } else
                    cc.game.emit(c.SocketInfo, {
                        _sub: s.Socket.Message,
                        flag: t._info.flag,
                        data: n
                    })
            }
            ,
            this.startConnectCheck()
        }
        ,
        t.prototype.disconnect = function() {
            this._ws && (cc.log("sock - disconnect()"),
            cc.game.emit(c.SocketInfo, {
                _sub: s.Socket.Disconnect,
                flag: this._info.flag
            }),
            this._ws.onopen = null,
            this._ws.onmessage = null,
            this._ws.onclose = null,
            this._ws.close(),
            this.stopConnectCheck(),
            this.stopSilenceCheck(),
            this.stopRecvCheck()),
            this._ws = null
        }
        ,
        t.prototype.startConnectCheck = function() {
            var t = this;
            this._connectTimer = setTimeout(function() {
                cc.game.emit(c.SocketInfo, {
                    _sub: s.Socket.ConnectTimeout,
                    flag: t._info.flag
                })
            }, this._connectCheckTime)
        }
        ,
        t.prototype.stopConnectCheck = function() {
            this._connectTimer && (clearTimeout(this._connectTimer),
            this._connectTimer = null)
        }
        ,
        t.prototype.startSilenceCheck = function() {
            var t = this;
            this.stopSilenceCheck(),
            this._silenceTimer = setTimeout(function() {
                cc.game.emit(c.SocketInfo, {
                    _sub: s.Socket.SilenceTimeout,
                    flag: t._info.flag
                })
            }, this._silenceCheckTime)
        }
        ,
        t.prototype.stopSilenceCheck = function() {
            this._silenceTimer && (clearTimeout(this._silenceTimer),
            this._silenceTimer = null)
        }
        ,
        t.prototype.startRecvCheck = function() {
            var t = this;
            this.stopRecvCheck(),
            this._recvTimer = setTimeout(function() {
                cc.game.emit(c.SocketInfo, {
                    _sub: s.Socket.RecvTimeout,
                    flag: t._info.flag
                })
            }, this._recvCheckTime)
        }
        ,
        t.prototype.stopRecvCheck = function() {
            this._recvTimer && (clearTimeout(this._recvTimer),
            this._recvTimer = null)
        }
        ,
        t.prototype.send = function(t) {
            if (this._ws && this._ws.readyState === WebSocket.OPEN) {
                if (!t.id)
                    return void this._ws.send(t.data);
                if (!this.sendFulfilled)
                    throw new Error("\u53d1\u9001\u6d88\u606f\u8bf7\u5148\u8bbe\u7f6e\u6570\u636e\u52a0\u5bc6\u65b9\u6cd5 -> setSendInterceptor");
                var e = this.sendFulfilled(t);
                if (e instanceof Error) {
                    if (!this.sendRejected)
                        throw e;
                    this.sendRejected(e)
                } else
                    this.startRecvCheck(),
                    this._ws.send(e)
            }
        }
        ,
        t.prototype.setSendInterceptor = function(t, e) {
            this.sendFulfilled = t,
            this.sendRejected = e
        }
        ,
        t.prototype.setRecvInterceptor = function(t, e) {
            this.recvFulfilled = t,
            this.recvRejected = e
        }
        ,
        t.prototype.mydogDecode = function(t) {
            var e = new Uint8Array(t);
            try {
                for (var n = 0; n < e.length; ) {
                    var o = e[n] << 24 | e[n + 1] << 16 | e[n + 2] << 8 | e[n + 3];
                    if (1 === e[n + 4])
                        return {
                            id: e[n + 5] << 8 | e[n + 6],
                            data: JSON.parse(z(e.subarray(n + 7, n + 4 + o)))
                        };
                    if (2 === e[n + 4]) {
                        var r = JSON.parse(z(e.subarray(n + 5, n + 4 + o)));
                        return r.id = -1,
                        r
                    }
                    if (3 === e[n + 4])
                        return {
                            id: -2,
                            data: null
                        };
                    n += o + 4
                }
            } catch (i) {
                console.log(i)
            }
        }
        ,
        t.prototype.mydogEncode = function(t) {
            return C(t.id, t.data || null)
        }
        ,
        t.prototype.mydogShakeVerify = function() {
            var t = new Uint8Array(5);
            t[0] = 0,
            t[1] = 0,
            t[2] = 0,
            t[3] = 1,
            t[4] = 2,
            this.send({
                id: null,
                data: t.buffer
            })
        }
        ,
        t.prototype.mydogHeartBeat = function() {
            var t = new Uint8Array(5);
            t[0] = 0,
            t[1] = 0,
            t[2] = 0,
            t[3] = 1,
            t[4] = 3,
            this.send({
                id: null,
                data: t.buffer
            })
        }
        ,
        t
    }());
    (function(t) {
        t[t.View = 7] = "View",
        t[t.Toast = 8] = "Toast",
        t[t.Loading = 9] = "Loading"
    }
    )(k || (k = {}));
    var A, T = function() {
        function t() {
            var t = this;
            this._pfbToast = null,
            this._bundleName = "game",
            this._viewList = [],
            this._isOpening = !1,
            this._isLoading = !1,
            this._pfbLoading = null,
            this._openLoading = !1,
            this._atlasKV = null,
            this._spriteFrameKV = null,
            this._sfPixel = null,
            cc.game.on(c.ViewClosed, function(e) {
                console.log("MSG_MAIN.ViewClosed-----------------" + e),
                0 === this.getOpenedViewCount() ? cc.game.emit(c.ViewEmpty, e) : cc.game.emit(c.ViewBack, this.getLayer(k.View).children[0].name, e),
                t.checkPopup()
            }, this),
            this._atlasKV = new Map,
            this._spriteFrameKV = new Map,
            cc.director.once(cc.Director.EVENT_AFTER_SCENE_LAUNCH, function() {
                t._sfPixel || xysz.res.base64ToTexture("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWP4////fwAJ+wP9CNHoHgAAAABJRU5ErkJggg==").then(function(e) {
                    return t._sfPixel = new cc.SpriteFrame(e)
                })
            })
        }
        return t.prototype.createDefaultToast = function() {
            return r(this, void 0, void 0, function() {
                var t, e, n, o, r, s;
                return i(this, function() {
                    return t = .9 * cc.winSize.width,
                    e = .15 * t,
                    (n = new cc.Node).width = t,
                    n.height = e,
                    o = new cc.Node,
                    (r = o.addComponent(cc.Sprite)).spriteFrame = this._sfPixel,
                    r.sizeMode = cc.Sprite.SizeMode.CUSTOM,
                    o.name = "image",
                    o.height = e,
                    o.width = t,
                    n.addChild(o, -1),
                    (s = xysz.res.createNewLabel()).horizontalAlign = cc.Label.HorizontalAlign.CENTER,
                    s.verticalAlign = cc.Label.VerticalAlign.CENTER,
                    s.overflow = cc.Label.Overflow.SHRINK,
                    s.enableWrapText = !0,
                    s.node.width = t - 10,
                    s.node.height = e - 10,
                    s.node.name = "label",
                    s.node.color = cc.Color.BLACK,
                    n.addChild(s.node),
                    [2, n]
                })
            })
        }
        ,
        t.prototype.setToastPrefab = function(t, e, n) {
            this._pfbToast = t,
            e && (this._pfbToast.data.getComponentInChildren(cc.Sprite).spriteFrame = e),
            n && this._pfbToast.data.getComponentInChildren(cc.RichText) && (this._pfbToast.data.getComponentInChildren(cc.RichText).imageAtlas = n)
        }
        ,
        t.prototype.setCurrBundleName = function(t) {
            this._bundleName = t
        }
        ,
        t.prototype.getLayer = function(t) {
            if (cc.Canvas.instance && cc.Canvas.instance.node) {
                var e = "layer_" + t
                  , n = cc.Canvas.instance.node.getChildByName(e);
                return n || ((n = new cc.Node).name = e,
                n.parent = cc.Canvas.instance.node,
                n.zIndex = t,
                n.width = cc.winSize.width,
                n.height = cc.winSize.height),
                n
            }
        }
        ,
        t.prototype.createDefaultLoading = function() {
            var t = new cc.Node;
            t.width = cc.winSize.width,
            t.height = cc.winSize.height;
            var e = new cc.Node;
            e.parent = t;
            var n = e.addComponent(cc.Sprite);
            n.spriteFrame = this._sfPixel,
            n.sizeMode = cc.Sprite.SizeMode.CUSTOM,
            e.width = cc.winSize.width,
            e.height = cc.winSize.height,
            e.opacity = 192,
            e.color = cc.Color.BLACK,
            e.addComponent(cc.BlockInputEvents);
            var o = xysz.res.createNewLabel();
            return o.node.parent = t,
            o.string = "\u52a0\u8f7d\u4e2d...",
            t
        }
        ,
        t.prototype.switchLoading = function(t) {
            this._openLoading = t
        }
        ,
        t.prototype.setLoading = function(t) {
            this._pfbLoading = t
        }
        ,
        t.prototype.showLoading = function() {
            console.log("showLoading"),
            this._isLoading || (this._pfbLoading ? cc.instantiate(this._pfbLoading).parent = this.getLayer(k.Loading) : this.createDefaultLoading().parent = this.getLayer(k.Loading),
            this._isLoading = !0)
        }
        ,
        t.prototype.hideLoading = function() {
            console.log("hideLoading"),
            this._isLoading = !1,
            this.getLayer(k.Loading).destroyAllChildren()
        }
        ,
        t.prototype.clearAllViewList = function() {
            this._viewList = []
        }
        ,
        t.prototype.addView = function(t) {
            return r(this, void 0, void 0, function() {
                return i(this, function(e) {
                    switch (e.label) {
                    case 0:
                        return "string" == typeof t && (t = {
                            viewName: t
                        }),
                        this._viewList.push(t),
                        t.priority && (this._viewList = this._viewList.sort(function(t, e) {
                            return t.priority - e.priority
                        })),
                        [4, this.checkPopup()];
                    case 1:
                        return e.sent(),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.isExistView = function(t) {
            return !!this.getLayer(k.View).getChildByName(t)
        }
        ,
        t.prototype.closeView = function(t) {
            return r(this, void 0, void 0, function() {
                var e, n;
                return i(this, function(o) {
                    switch (o.label) {
                    case 0:
                        return e = this.getLayer(k.View),
                        (n = e.getChildByName(t)) ? [4, n.getComponent(xysz.ViewBase).closeSelf()] : [2];
                    case 1:
                        return o.sent(),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.closeAllViews = function() {
            return r(this, void 0, void 0, function() {
                var t;
                return i(this, function(e) {
                    switch (e.label) {
                    case 0:
                        return (t = this.getLayer(k.View)) ? [4, Promise.all(t.children.map(function(t) {
                            return t.getComponent(xysz.ViewBase).closeSelf()
                        }))] : [2];
                    case 1:
                        return e.sent(),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.getOpenedViewCount = function() {
            return this.getLayer(k.View).childrenCount
        }
        ,
        t.prototype.addFloatNode = function(t) {
            var e = this.getLayer(k.Toast)
              , n = 0;
            e.childrenCount > 0 && (n = e.children[e.childrenCount - 1].y),
            t.x = 0,
            t.y = n - 80,
            t.parent = e,
            cc.tween(t).to(Math.min((100 - t.y) / 60, 2.5), {
                y: 100
            }).call(function() {
                return t.destroy()
            }).start()
        }
        ,
        t.prototype.addFixedNode = function(t) {
            var e = this.getLayer(k.Toast);
            e.destroyAllChildren(),
            t.parent = e,
            cc.tween(t).by(.5, {
                y: 50
            }).delay(.2).to(.6, {
                opacity: 0
            }).call(function() {
                return t.destroy()
            }).start()
        }
        ,
        t.prototype.showToast = function(t) {
            if (t && "" != t)
                return r(this, void 0, void 0, function() {
                    var e, n;
                    return i(this, function(o) {
                        switch (o.label) {
                        case 0:
                            return this._pfbToast ? [3, 2] : (e = this,
                            [4, this.createDefaultToast()]);
                        case 1:
                            e._pfbToast = o.sent(),
                            o.label = 2;
                        case 2:
                            return t.length > 100 && (t = t.substr(0, 100)),
                            ((n = cc.instantiate(this._pfbToast)).getComponentInChildren(cc.Label) || n.getComponentInChildren(cc.RichText)).string = t,
                            this.addFixedNode(n),
                            [2]
                        }
                    })
                })
        }
        ,
        t.prototype.checkPopup = function() {
            return r(this, void 0, void 0, function() {
                var t;
                return i(this, function(e) {
                    switch (e.label) {
                    case 0:
                        return console.log("checkPopupcheckPopup---------------", this._viewList.length),
                        0 === this._viewList.length ? [2] : (t = this._viewList.pop()).priority && (this._isOpening || this.getOpenedViewCount() > 0) ? (this._viewList.push(t),
                        [2]) : [4, this.execOpen_(t)];
                    case 1:
                        return e.sent(),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.execOpen_ = function(t) {
            return r(this, void 0, void 0, function() {
                var e, n, o;
                return i(this, function(r) {
                    switch (r.label) {
                    case 0:
                        if (console.log("execOpen_execOpen_execOpen_---------------", t),
                        e = this.getLayer(k.View),
                        n = e.getChildByName(t.viewName))
                            return [2];
                        t.bundleName = t.bundleName || this._bundleName,
                        o = null,
                        r.label = 1;
                    case 1:
                        return r.trys.push([1, 7, , 8]),
                        this._isOpening = !0,
                        this._openLoading ? [4, this.showLoading()] : [3, 3];
                    case 2:
                        r.sent(),
                        r.label = 3;
                    case 3:
                        return [4, xysz.res.loadAsset(t.bundleName, "prefab/" + t.viewName)];
                    case 4:
                        return o = r.sent(),
                        this._openLoading ? [4, this.hideLoading()] : [3, 6];
                    case 5:
                        r.sent(),
                        r.label = 6;
                    case 6:
                        return [3, 8];
                    case 7:
                        return r.sent(),
                        this._isOpening = !1,
                        this.checkPopup(),
                        [2];
                    case 8:
                        return this._isOpening = !1,
                        (n = e.getChildByName(t.viewName)) ? [2] : ((n = cc.instantiate(o)).name = t.viewName,
                        n.parent = e,
                        t.data && n.getComponent(xysz.ViewBase).setData(t.data),
                        [2])
                    }
                })
            })
        }
        ,
        t.prototype.addAtlas = function(t) {
            var e = this;
            t.name.includes(".") && (t.name = t.name.split(".")[0]),
            this._atlasKV.set(t.name, t),
            t.getSpriteFrames().forEach(function(t) {
                return e._spriteFrameKV.set(t.name, t)
            })
        }
        ,
        t.prototype.getAtlas = function(t) {
            return this._atlasKV.get(t)
        }
        ,
        t.prototype.addRemoteImage = function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return [4, xysz.res.loadRemoteRes(t)];
                    case 1:
                        return (n = i.sent()).packable = !1,
                        o = new cc.SpriteFrame(n),
                        r = e || t.split("/").ext_last().split(".")[0],
                        this._spriteFrameKV.set(r, o),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.addInnerImage = function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return [4, xysz.res.loadAsset(t, e, cc.Texture2D)];
                    case 1:
                        return (n = i.sent()).packable = !1,
                        o = new cc.SpriteFrame(n),
                        r = e.split("/").ext_last().split(".")[0],
                        this._spriteFrameKV.set(r, o),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.getSpriteFrame = function(t, e) {
            return e ? this._atlasKV.get(e).getSpriteFrame(t) : this._spriteFrameKV.get(t)
        }
        ,
        t.prototype.refreshSpriteFrame = function(t, e, n) {
            return r(this, void 0, void 0, function() {
                return i(this, function() {
                    return t.getComponent(cc.Sprite) && (t.getComponent(cc.Sprite).spriteFrame = xysz.ui.getSpriteFrame(e),
                    b.adjustMaxLength(t.getComponent(cc.Sprite), n)),
                    [2]
                })
            })
        }
        ,
        t
    }(), R = new (function() {
        function t() {
            this.private = {}
        }
        return t.prototype.initWithManifest = function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r, s, c, a, u, l, h, f, p, d, m;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return t.endsWith("/") || (t += "/"),
                        n = "" + t + e + "?_t=" + Date.now(),
                        [4, xysz.res.loadRemoteRes(n)];
                    case 1:
                        for (a in o = i.sent(),
                        r = cc.sys.localStorage.getItem("_manifest") || "{}",
                        s = JSON.parse(r),
                        c = [],
                        o.json)
                            c.push(a);
                        u = 0,
                        i.label = 2;
                    case 2:
                        return u < c.length ? (l = c[u],
                        h = o.json[l],
                        f = l.split(".")[0],
                        p = null,
                        s[l] === h && (d = cc.sys.localStorage.getItem(l)) && (p = JSON.parse(d)),
                        p ? [3, 4] : (n = "" + t + l + "?_t=" + Date.now(),
                        [4, xysz.res.loadRemoteRes(t + l)])) : [3, 6];
                    case 3:
                        m = i.sent(),
                        p = m.json,
                        cc.sys.localStorage.setItem(l, JSON.stringify(p)),
                        i.label = 4;
                    case 4:
                        this[f] = p,
                        i.label = 5;
                    case 5:
                        return u++,
                        [3, 2];
                    case 6:
                        return cc.sys.localStorage.setItem("_manifest", JSON.stringify(o.json)),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.initWithTotal = function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return t.endsWith("/") || (t += "/"),
                        n = "" + t + e + "?_t=" + Date.now(),
                        [4, xysz.res.loadRemoteRes(n)];
                    case 1:
                        for (r in (o = i.sent()).json)
                            this[r.split(".")[0]] = o.json[r];
                        return [2]
                    }
                })
            })
        }
        ,
        t.prototype.getInfo = function(t, e) {
            var n = this.getList(t);
            return n ? n.find(function(t) {
                return t.cfg_id == e
            }) : null
        }
        ,
        t.prototype.getList = function(t) {
            return t.includes(".") ? this[t.split(".")[0] + "s"] : this[t + "s"]
        }
        ,
        t
    }()), M = (A = _(function(t) {
        function e(n) {
            return "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? (t.exports = e = function(t) {
                return typeof t
            }
            ,
            t.exports.default = t.exports,
            t.exports.__esModule = !0) : (t.exports = e = function(t) {
                return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
            }
            ,
            t.exports.default = t.exports,
            t.exports.__esModule = !0),
            e(n)
        }
        t.exports = e,
        t.exports.default = t.exports,
        t.exports.__esModule = !0
    })) && A.__esModule && Object.prototype.hasOwnProperty.call(A, "default") ? A.default : A, D = function() {
        function t() {
            this.assyId = "",
            this.homeThemePath = ""
        }
        return Object.defineProperty(t.prototype, "info", {
            get: function() {
                return this._info
            },
            set: function(t) {
                this._info = t,
                this._info.beginTimestamp = xysz.time.getTimestamp(this._info.beginTime),
                this._info.endTimestamp = xysz.time.getTimestamp(this._info.endTime)
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(t.prototype, "game", {
            get: function() {
                return this._game
            },
            set: function(t) {
                this._game = t,
                this.filterGameSetting(this._game),
                this.homeThemePath = this._game.homePage.placeTheme.theme.themePath,
                this.assyId = this._game.gamePage.gameType.selectGame.assyId
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(t.prototype, "isPreviewMode", {
            get: function() {
                return "0" === xysz.query.edition
            },
            set: function() {},
            enumerable: !1,
            configurable: !0
        }),
        t.prototype.filterGameSetting = function(t) {
            for (var e in t)
                if (Object.prototype.hasOwnProperty.call(t, e))
                    if (t[e] && "object" === M(t[e]) && !e.startsWith("_"))
                        t[e].value && ("integer" === t[e].valueType ? t[e] = parseInt(t[e].value) : t[e] = t[e].value),
                        this.filterGameSetting(t[e]);
                    else if ("themePath" === e) {
                        var n = t[e];
                        n.endsWith("/") || (n += "/"),
                        t[e] = n
                    }
        }
        ,
        t.prototype.getEnvByHostname = function() {
            return ["devapi.xiaoyisz.com", "qiehuangdev.ioutu.cn", "localhost"].includes(location.hostname) ? "dev" : "prod"
        }
        ,
        t
    }(), E = new (function() {
        function t() {
            this.isOpen = !0,
            this.isSceneHide = !1,
            this._urlMap = new Map,
            this._voiceMap = new Map,
            this._bgmClip = null,
            this._isAllowResume = !1;
            var t = cc.sys.localStorage.getItem("game_setting");
            t && (this.isOpen = JSON.parse(t).sound)
        }
        return t.prototype.setOnlineStatus = function(t) {
            this.isOpen = t,
            this.refreshStatus_()
        }
        ,
        t.prototype.refreshStatus_ = function() {
            this.switchEffect_(),
            this.switchMusic_();
            var t = cc.sys.localStorage.getItem("game_setting")
              , e = {};
            t && (e = JSON.parse(t)),
            e.sound = this.isOpen,
            cc.sys.localStorage.setItem("game_setting", JSON.stringify(e))
        }
        ,
        t.prototype.switchEffect_ = function() {
            this.isOpen || cc.audioEngine.stopAllEffects()
        }
        ,
        t.prototype.switchMusic_ = function() {
            this.isOpen ? this.resumeMusic() : this.pauseMusic()
        }
        ,
        t.prototype.loadLocalSound = function(t, e, n) {
            return r(this, void 0, void 0, function() {
                var o, r, s, c, a;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        for (r in e.endsWith("/") || (e += "/"),
                        o = [],
                        n)
                            o.push(r);
                        s = 0,
                        i.label = 1;
                    case 1:
                        return s < o.length ? (c = o[s],
                        Object.prototype.hasOwnProperty.call(n, c) ? [4, xysz.res.loadAsset(t, "" + e + n[c])] : [3, 3]) : [3, 4];
                    case 2:
                        (a = i.sent()).name = n[c],
                        this._voiceMap.set(n[c], a),
                        i.label = 3;
                    case 3:
                        return s++,
                        [3, 1];
                    case 4:
                        return [2]
                    }
                })
            })
        }
        ,
        t.prototype.loadRemoteSound = function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r, s, c;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        for (o in t.endsWith("/") || (t += "/"),
                        n = [],
                        e)
                            n.push(o);
                        r = 0,
                        i.label = 1;
                    case 1:
                        return r < n.length ? (s = n[r],
                        Object.prototype.hasOwnProperty.call(e, s) ? (this._urlMap.set(e[s], "" + t + e[s] + ".mp3"),
                        xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? [3, 3] : [4, xysz.res.loadRemoteRes("" + t + e[s] + ".mp3")]) : [3, 3]) : [3, 4];
                    case 2:
                        (c = i.sent()).name = e[s],
                        this._voiceMap.set(e[s], c),
                        i.label = 3;
                    case 3:
                        return r++,
                        [3, 1];
                    case 4:
                        return [2]
                    }
                })
            })
        }
        ,
        t.prototype.playVoice = function(t, e) {
            if (void 0 === e && (e = !1),
            !this.isSceneHide)
                return r(this, void 0, void 0, function() {
                    var n;
                    return i(this, function() {
                        return this.isOpen && (xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? ((n = my.createInnerAudioContext()).onEnded(function() {
                            return n.destroy()
                        }),
                        n.isLoop = e,
                        n.src = this._urlMap.get(t),
                        n.play()) : cc.audioEngine.play(this._voiceMap.get(t), e, 1)),
                        [2]
                    })
                })
        }
        ,
        t.prototype.playMusic = function(t, e) {
            if (void 0 === e && (e = !0),
            !this.isSceneHide)
                return r(this, void 0, void 0, function() {
                    var n;
                    return i(this, function() {
                        return n = !1,
                        this._bgmClip && this._bgmClip.name === t || (this._isAllowResume = !1,
                        n = !0),
                        n && (xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? (this._bgmClip && this._bgmClip.destroy(),
                        this._bgmClip = my.createInnerAudioContext(),
                        this._bgmClip.loop = e,
                        this._bgmClip.src = this._urlMap.get(t)) : this._bgmClip = this._voiceMap.get(t)),
                        this.isOpen ? (this._bgmClip && (xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? this._bgmClip.play() : (!n && this._isAllowResume ? cc.audioEngine.resumeMusic() : (console.log(this._bgmClip),
                        cc.audioEngine.playMusic(this._bgmClip, e)),
                        this._isAllowResume = !0)),
                        [2]) : [2]
                    })
                })
        }
        ,
        t.prototype.voiceClick = function() {
            this.playVoice("sound_click")
        }
        ,
        t.prototype.resumeMusic = function() {
            this.isOpen && this._bgmClip && this.playMusic(this._bgmClip.name)
        }
        ,
        t.prototype.pauseMusic = function() {
            this._bgmClip && (xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? this._bgmClip.pause() : cc.audioEngine.pauseMusic())
        }
        ,
        t.prototype.stopMusic = function() {
            this._bgmClip && (xysz.runtime === xysz.C_Runtime.taobao && cc.sys.os === cc.sys.OS_ANDROID ? this._bgmClip.stop() : cc.audioEngine.stopMusic(),
            this._bgmClip = null)
        }
        ,
        t
    }()), L = function() {
        function t() {
            this._timeOffet = 0
        }
        return t.prototype.initServerTime = function(t) {
            this._timeOffet = Date.now() - t
        }
        ,
        t.prototype.getServerTime = function() {
            return Date.now() - this._timeOffet
        }
        ,
        t.prototype.convertZeroTime = function(t) {
            return t - xysz.time.convertTodayTime(t)
        }
        ,
        t.prototype.convertTodayTime = function(t) {
            return t % 864e5 - 6e4 * (new Date).getTimezoneOffset()
        }
        ,
        t.prototype.isInPeroid = function(t, e, n) {
            return t >= e && t <= n
        }
        ,
        t.prototype.getTimestamp = function(t) {
            return new Date(t.replace(/-/g, "/")).getTime()
        }
        ,
        t.prototype.formatTimestamp = function(t, e) {
            var n = new Date(t);
            return "" + n.getFullYear() + e + (n.getMonth() + 1) + e + n.getDate()
        }
        ,
        t.prototype.formatTimestampToDate = function(t, e, n) {
            void 0 === n && (n = !1);
            var o = new Date(t)
              , r = o.getMonth() + 1 < 10 ? "0" + (o.getMonth() + 1) : o.getMonth() + 1
              , i = o.getDate() < 10 ? "0" + o.getDate() : o.getDate()
              , s = o.getHours() < 10 ? "0" + o.getHours() : o.getHours()
              , c = o.getMinutes() < 10 ? "0" + o.getMinutes() : o.getMinutes()
              , a = o.getSeconds() < 10 ? "0" + o.getSeconds() : o.getSeconds();
            return (n ? "" : "" + o.getFullYear() + e) + r + e + i + " " + s + ":" + c + ":" + a
        }
        ,
        t.prototype.formatTimeCN = function(t) {
            if (t < 0)
                return "";
            var e = Math.ceil(t / 1e3)
              , n = Math.floor(e / 86400)
              , o = Math.floor(e % 86400 / 3600)
              , r = Math.floor(e % 3600 / 60)
              , i = e % 60;
            function s(t, e, n) {
                return void 0 === n && (n = !1),
                "" + (n ? t > 9 ? t : "0" + t : t) + e
            }
            var c = "";
            return (n > 0 || c.length > 0) && (c += s(n, "\u5929")),
            (o > 0 || c.length > 0) && (c += s(o, "\u5c0f\u65f6")),
            (r > 0 || c.length > 0) && (c += s(r, "\u5206")),
            (i > 0 || c.length > 0) && (c += s(i, "\u79d2")),
            c
        }
        ,
        t.prototype.formatTime = function(t, e) {
            if (void 0 === e && (e = 3),
            t < 0)
                return "";
            var n = Math.floor(t / 1e3)
              , o = Math.floor(n / 3600)
              , r = Math.floor(n % 3600 / 60)
              , i = n % 60;
            return 3 === e ? (o > 9 ? o : "0" + o) + ":" + (r > 9 ? r : "0" + r) + ":" + (i > 9 ? i : "0" + i) : 2 === e ? (r > 9 ? r : "0" + r) + ":" + (i > 9 ? i : "0" + i) : 1 === e ? "" + (i > 9 ? i : "0" + i) : void 0
        }
        ,
        t
    }(), O = new (function() {
        function t() {
            var t = this;
            this._btnClub = null,
            this.onshowInfo = null,
            window.wx && (wx.showShareMenu({
                withShareTicket: !0
            }),
            wx.onShow(function(e) {
                cc.log("onshow", e),
                t.onshowInfo = e
            }))
        }
        return t.prototype.vibrateShort = function() {
            window.wx && wx.vibrateShort({})
        }
        ,
        t.prototype.vibrateLong = function() {
            window.wx && wx.vibrateLong({})
        }
        ,
        t.prototype.login = function() {
            return window.wx ? new Promise(function(t, e) {
                wx.login({
                    timeout: 3e3,
                    success: function(e) {
                        return t(e.code)
                    },
                    fail: function() {
                        return e("\u5fae\u4fe1\u767b\u9646\u5931\u8d25,\u8bf7\u91cd\u8bd5")
                    }
                })
            }
            ) : Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301login")
        }
        ,
        t.prototype.checkSession = function() {
            if (window.wx)
                return new Promise(function(t) {
                    wx.checkSession({
                        success: function() {
                            return t(!0)
                        },
                        fail: function() {
                            return t(!1)
                        }
                    })
                }
                )
        }
        ,
        t.prototype.getUserInfo = function(t) {
            if (window.wx)
                return new Promise(function(e, n) {
                    wx.getUserInfo({
                        withCredentials: t,
                        lang: "zh_CN",
                        success: function(t) {
                            return e(t)
                        },
                        fail: function() {
                            return n("\u83b7\u53d6\u7528\u6237\u4fe1\u606f\u5931\u8d25,\u8bf7\u91cd\u8bd5")
                        }
                    })
                }
                )
        }
        ,
        t.prototype.getAuthInfo = function(t) {
            return window.wx ? new Promise(function(e, n) {
                wx.getSetting({
                    withSubscriptions: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function() {
                        return n("\u68c0\u67e5\u6743\u9650\u5931\u8d25")
                    }
                })
            }
            ) : Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301")
        }
        ,
        t.prototype.checkAuth = function(t) {
            return window.wx ? new Promise(function(e, n) {
                wx.getSetting({
                    success: function(n) {
                        return e(n.authSetting[t])
                    },
                    fail: function() {
                        return n("\u68c0\u67e5\u6743\u9650\u5931\u8d25")
                    }
                })
            }
            ) : Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301")
        }
        ,
        t.prototype.authorize = function(t) {
            return window.wx ? new Promise(function(e) {
                wx.authorize({
                    scope: t,
                    success: function() {
                        return e(!0)
                    },
                    fail: function() {
                        return e(!1)
                    }
                })
            }
            ) : Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301")
        }
        ,
        t.prototype.getInteractiveData = function(t) {
            return window.wx ? new Promise(function(e, n) {
                wx.getUserInteractiveStorage({
                    keyList: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            ) : Promise.resolve(null)
        }
        ,
        t.prototype.showGameClubBtn = function(t, e) {
            window.wx && (this._btnClub || t && (this._btnClub = wx.createGameClubButton({
                type: "text",
                text: "",
                style: {
                    left: t.x,
                    top: t.y,
                    width: t.width,
                    height: t.height
                }
            }),
            e && this._btnClub.onTap(e)),
            this._btnClub && this._btnClub.show())
        }
        ,
        t.prototype.hideGameClubBtn = function() {
            this._btnClub && this._btnClub.hide()
        }
        ,
        t.prototype.captureScene = function() {
            return new Promise(function(t, e) {
                window.wx && cc.game.canvas.toTempFilePath({
                    success: function(n) {
                        wx.saveImageToPhotosAlbum({
                            filePath: n.tempFilePath,
                            success: function() {
                                t(null)
                            },
                            fail: function() {
                                e()
                            }
                        })
                    },
                    fail: function(t) {
                        cc.log(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.captureRect = function(t) {
            return new Promise(function(e, o) {
                if (window.wx) {
                    var r = cc.game.canvas
                      , i = n({}, t)
                      , s = i.x
                      , c = i.y
                      , a = i.width
                      , u = i.height;
                    r.toTempFilePath({
                        x: s,
                        y: c,
                        width: a,
                        height: u,
                        success: function(t) {
                            wx.saveImageToPhotosAlbum({
                                filePath: t.tempFilePath,
                                success: function() {
                                    e(null)
                                },
                                fail: function() {
                                    o()
                                }
                            })
                        },
                        fail: function(t) {
                            cc.log(t)
                        }
                    })
                }
            }
            )
        }
        ,
        t.prototype.showModal = function(t, e, n) {
            return new Promise(function(o) {
                window.wx && wx.showModal({
                    title: t,
                    content: e,
                    showCancel: n,
                    success: o
                })
            }
            )
        }
        ,
        t.prototype.openSetting = function(t) {
            return new Promise(function(e) {
                window.wx && wx.openSetting({
                    withSubscriptions: t,
                    success: e
                })
            }
            )
        }
        ,
        t.prototype.getLocation = function() {
            return new Promise(function(t) {
                if (!window.wx)
                    return Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301");
                wx.getLocation({
                    altitude: "false",
                    success: t
                })
            }
            )
        }
        ,
        t.prototype.requestSubscribeMessage = function(t) {
            return new Promise(function(e) {
                if (!window.wx)
                    return Promise.reject("\u6b64\u5e73\u53f0\u4e0d\u652f\u6301");
                wx.requestSubscribeMessage({
                    tmplIds: t,
                    complete: e
                })
            }
            )
        }
        ,
        t.prototype.convertToCocosBox = function(t) {
            if (window.wx) {
                var e = wx.getSystemInfoSync()
                  , n = cc.winSize.width / e.screenWidth
                  , o = t.height;
                t.width *= n,
                t.height *= n,
                t.x *= n,
                t.y = cc.winSize.height - (t.y + o) * n
            }
            return t
        }
        ,
        t.prototype.convertToDeviceBox = function(t) {
            if (window.wx) {
                var e = wx.getSystemInfoSync()
                  , n = e.screenWidth / cc.winSize.width
                  , o = t.height;
                t.width *= n,
                t.height *= n,
                t.x *= n,
                t.y = e.screenHeight - (t.y + o) * n
            }
            return t
        }
        ,
        t
    }()), I = new (function() {
        function t() {}
        return t.prototype.init = function() {
            return r(this, void 0, void 0, function() {
                return i(this, function(t) {
                    switch (t.label) {
                    case 0:
                        return [4, xysz.h5.loadSDK("//res.wx.qq.com/open/js/jweixin-1.6.0.js")];
                    case 1:
                        return t.sent(),
                        "miniprogram" === window.__wxjs_environment && (xysz.runtime = a.program_wx),
                        wx.miniProgram.getEnv(function(t) {
                            t.miniprogram && (xysz.runtime = a.program_wx)
                        }),
                        window.WeixinJSBridge && WeixinJSBridge.on("onPageStateChange", function(t) {
                            "true" === t.active || !0 === t.active ? cc.game.emit(cc.game.EVENT_SHOW) : cc.game.emit(cc.game.EVENT_HIDE)
                        }),
                        [2]
                    }
                })
            })
        }
        ,
        t.prototype.officialCheckApis = function(t) {
            return new Promise(function(e) {
                wx.checkJsApi({
                    jsApiList: t,
                    success: function(n) {
                        if (console.log("checkJsApi----res", n),
                        n.checkResult && "checkJsApi:ok" == n.errMsg) {
                            var o = t.filter(function(t) {
                                return n.checkResult[t]
                            });
                            e(o)
                        } else
                            e(null)
                    },
                    fail: function(t) {
                        return console.log("fail", t)
                    },
                    complete: function(t) {
                        return console.log("complete", t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.wxJsApiConfig = function(t, e, n, o) {
            return void 0 === o && (o = !1),
            r(this, void 0, Promise, function() {
                var r, s;
                return i(this, function() {
                    return r = this.getWxSignature(e.nonceStr, t.sercerts, e.timestamp, n),
                    s = ["updateAppMessageShareData", "updateTimelineShareData", "closeWindow"],
                    [2, new Promise(function(n, i) {
                        wx.error(i),
                        wx.ready(n);
                        var c = {
                            debug: o,
                            appId: t.appId,
                            timestamp: e.timestamp,
                            nonceStr: e.nonceStr,
                            signature: r,
                            jsApiList: s,
                            openTagList: ["wx-open-launch-weapp"]
                        };
                        wx.config(c)
                    }
                    )]
                })
            })
        }
        ,
        t.prototype.wxGetLocation = function(t) {
            return void 0 === t && (t = "wgs84"),
            new Promise(function(e) {
                wx.getLocation({
                    type: t,
                    success: function(t) {
                        e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.wxScanQRCode = function(t) {
            return void 0 === t && (t = 0),
            new Promise(function(e) {
                wx.scanQRCode({
                    needResult: t,
                    scanType: ["qrCode", "barCode"],
                    success: function(t) {
                        e(t.resultStr)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getWxSignature = function(t, e, n, o) {
            var r = {
                noncestr: t,
                jsapi_ticket: e,
                timestamp: n,
                url: o
            }
              , i = b.getSortedQuery(r);
            return xysz.encrypt.Sha1.encode(i)
        }
        ,
        t.prototype.createJumpProgramTag = function(t, e, n, o) {
            var r = document.createElement("wx-open-launch-weapp");
            return r.id = xysz.tool.generateNoncestr(),
            r.setAttribute("username", e),
            r.setAttribute("path", n),
            r.style.width = t.width + "px",
            r.style.height = t.height + "px",
            r.innerHTML = '\n            <script type="text/wxtag-template">\n                <style>.wechat-btn { width: ' + t.width + "px; height:" + t.height + 'px; opacity:0; }</style>\n                <button class="wechat-btn"></button>\n            <\/script>',
            o && r.addEventListener("launch", function() {
                cc.game.targetOff(r),
                cc.game.once(cc.game.EVENT_SHOW, o, r)
            }),
            xysz.h5.addTagToTop(r, t.x + "px", t.y + "px"),
            r
        }
        ,
        t.prototype.navigateTo = function(t) {
            xysz.runtime === a.program_wx ? (console.log(t),
            wx.miniProgram.navigateTo(t)) : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.navigateBack = function() {
            xysz.runtime === a.program_wx ? wx.miniProgram.navigateBack() : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.switchTab = function(t) {
            xysz.runtime === a.program_wx ? (console.log(t),
            wx.miniProgram.switchTab(t)) : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.reLaunch = function(t) {
            xysz.runtime === a.program_wx ? (console.log(t),
            wx.miniProgram.reLaunch(t)) : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.redirectTo = function(t) {
            xysz.runtime === a.program_wx ? (console.log(t),
            wx.miniProgram.redirectTo(t)) : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.postMessage = function(t) {
            xysz.runtime === a.program_wx ? wx.miniProgram.postMessage(t) : console.log("\u8bf7\u5728\u5c0f\u7a0b\u5e8f\u5185\u8fdb\u884c\u5c1d\u8bd5")
        }
        ,
        t.prototype.closeWindow = function() {
            wx && wx.closeWindow()
        }
        ,
        t
    }()), N = function() {
        function t() {}
        return t.createTrimSprite = function() {
            var t = (new cc.Node).addComponent(cc.Sprite);
            return t.sizeMode = cc.Sprite.SizeMode.TRIMMED,
            t.trim = !0,
            t
        }
        ,
        t.createRawSprite = function() {
            var t = (new cc.Node).addComponent(cc.Sprite);
            return t.sizeMode = cc.Sprite.SizeMode.RAW,
            t.trim = !1,
            t
        }
        ,
        t.createNewLabel = function() {
            var t = (new cc.Node).addComponent(cc.Label);
            return t.fontSize = 30,
            t
        }
        ,
        t.loadRemoteRes = function(t) {
            return new Promise(function(e, n) {
                cc.assetManager.loadRemote(xysz.runtime === xysz.C_Runtime.taobao ? t + "?_t=" + Date.now() : t, function(t, o) {
                    t ? n(t) : e(o)
                })
            }
            )
        }
        ,
        t.loadRemoteSpine = function(t, e) {
            return r(this, void 0, Promise, function() {
                var n, o, r, s, c, a, u, l, h, f;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        t.endsWith("/") || (t += "/"),
                        i.label = 1;
                    case 1:
                        return i.trys.push([1, 8, , 9]),
                        [4, this.loadRemoteRes("" + t + e + ".json")];
                    case 2:
                        return n = i.sent(),
                        [4, this.loadRemoteRes("" + t + e + ".atlas")];
                    case 3:
                        o = i.sent(),
                        r = [],
                        s = [],
                        c = o.text.split("\n"),
                        a = 0,
                        i.label = 4;
                    case 4:
                        return a < c.length ? (u = c[a].trim()).endsWith(".png") ? (r.push(u),
                        [4, this.loadRemoteRes("" + t + u)]) : [3, 6] : [3, 7];
                    case 5:
                        l = i.sent(),
                        s.push(l),
                        i.label = 6;
                    case 6:
                        return a++,
                        [3, 4];
                    case 7:
                        return (h = new sp.SkeletonData).skeletonJson = n.json,
                        h.atlasText = o.text,
                        h.textures = s,
                        h.textureNames = r,
                        [2, h];
                    case 8:
                        return f = i.sent(),
                        [2, Promise.reject(f)];
                    case 9:
                        return [2]
                    }
                })
            })
        }
        ,
        t.loadRemoteDragonBones = function(t, e) {
            return r(this, void 0, Promise, function() {
                var n, o, r, s, c, a;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        t.endsWith("/") || (t += "/"),
                        i.label = 1;
                    case 1:
                        return i.trys.push([1, 5, , 6]),
                        [4, xysz.res.loadRemoteRes("" + t + e + "_ske.json")];
                    case 2:
                        return n = i.sent(),
                        [4, xysz.res.loadRemoteRes("" + t + e + "_tex.json")];
                    case 3:
                        return o = i.sent(),
                        [4, xysz.res.loadRemoteRes("" + t + e + "_tex.png")];
                    case 4:
                        return r = i.sent(),
                        (s = new dragonBones.DragonBonesAsset).dragonBonesJson = JSON.stringify(n.json),
                        (c = new dragonBones.DragonBonesAtlasAsset).atlasJson = JSON.stringify(o.json),
                        c.texture = r,
                        [2, {
                            dragonAsset: s,
                            dragonAtlasAsset: c
                        }];
                    case 5:
                        return a = i.sent(),
                        [2, Promise.reject(a)];
                    case 6:
                        return [2]
                    }
                })
            })
        }
        ,
        t.loadRemoteAtlas = function(t) {
            return r(this, void 0, Promise, function() {
                var e, n, o, r, s, c, a, u, l, h, f;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        if (!t.endsWith(".plist"))
                            return console.warn("\u8bf7\u4f20\u5165\u4ee5.plist\u7ed3\u675f\u7684\u5730\u5740"),
                            [2];
                        i.label = 1;
                    case 1:
                        return i.trys.push([1, 4, , 5]),
                        [4, this.loadRemoteRes(t)];
                    case 2:
                        return e = i.sent(),
                        n = t.replace(/[A-Za-z0-9]+.plist/, e._nativeAsset.metadata.textureFileName),
                        [4, this.loadRemoteRes(n)];
                    case 3:
                        for (s in o = i.sent(),
                        (r = new cc.SpriteAtlas).name = e._nativeAsset.metadata.textureFileName,
                        e._nativeAsset.frames)
                            c = e._nativeAsset.frames[s],
                            a = c.spriteOffset.replace(/{|}/g, "").split(",").map(function(t) {
                                return parseInt(t)
                            }),
                            u = c.spriteSourceSize.replace(/{|}/g, "").split(",").map(function(t) {
                                return parseInt(t)
                            }),
                            l = c.textureRect.replace(/{|}/g, "").split(",").map(function(t) {
                                return parseInt(t)
                            }),
                            h = s.substring(0, s.length - 4),
                            r._spriteFrames[h] = new cc.SpriteFrame(o,cc.rect(l[0], l[1], l[2], l[3]),c.textureRotated,cc.v2(a[0], a[1]),cc.size(u[0], u[1]));
                        return [2, r];
                    case 4:
                        return f = i.sent(),
                        [2, Promise.reject(f)];
                    case 5:
                        return [2]
                    }
                })
            })
        }
        ,
        t.dynamicGenerateAnimClip = function(t, e, n, o) {
            for (var r = [], i = 0; ; ) {
                var s;
                if (!(s = t instanceof cc.SpriteAtlas ? t.getSpriteFrame("" + e + i) : t.get("" + e + i))) {
                    var c = cc.AnimationClip.createWithSpriteFrames(r, n);
                    return c.name = o || e,
                    c
                }
                r.push(s),
                i++
            }
        }
        ,
        t.sliceTexture = function(t, e, n, o, r) {
            var i = cc.rect(0, 0, t.width, t.height)
              , s = i.width / o
              , c = i.height / r;
            return cc.rect(e, n, s, c)
        }
        ,
        t.getSliceTextureAtlas = function(t, e, n, o, s) {
            var c = this;
            return new Promise(function(a, u) {
                return r(c, void 0, void 0, function() {
                    return i(this, function() {
                        return cc.assetManager.loadRemote(t, function(t, r) {
                            if (t)
                                u();
                            else {
                                for (var i = new Map, c = new cc.SpriteAtlas, l = 0, h = 0; h < n; h++)
                                    for (var f = 0; f < e; f++) {
                                        var p = xysz.res.sliceTexture(r, f * o, h * s, e, n);
                                        i.set(l, {
                                            texture: r,
                                            rect: p
                                        });
                                        var d = cc.rect(p.x, p.y, o, s);
                                        c._spriteFrames[l] = new cc.SpriteFrame(r,d),
                                        l++
                                    }
                                a({
                                    map: i,
                                    atlas: c
                                })
                            }
                        }),
                        [2]
                    })
                })
            }
            )
        }
        ,
        t.loadLocalConfig = function() {
            return xysz.res.loadAsset("resources", "config", cc.JsonAsset).then(function(t) {
                return t.json
            })
        }
        ,
        t.loadBundle = function(t) {
            return r(this, void 0, Promise, function() {
                var e;
                return i(this, function(n) {
                    switch (n.label) {
                    case 0:
                        return (e = cc.assetManager.getBundle(t)) ? [3, 2] : [4, new Promise(function(n, o) {
                            cc.assetManager.loadBundle(t, function(t, r) {
                                t ? o() : (e = r,
                                n(null))
                            })
                        }
                        )];
                    case 1:
                        n.sent(),
                        n.label = 2;
                    case 2:
                        return [2, e]
                    }
                })
            })
        }
        ,
        t.loadAsset = function(t, e, n) {
            return r(this, void 0, void 0, function() {
                var o;
                return i(this, function(r) {
                    switch (r.label) {
                    case 0:
                        return [4, xysz.res.loadBundle(t)];
                    case 1:
                        return o = r.sent(),
                        [2, new Promise(function(t, r) {
                            o.load(e, n, function(e, n) {
                                e ? r(e) : t(n)
                            })
                        }
                        )]
                    }
                })
            })
        }
        ,
        t.loadAssetDir = function(t, e, n) {
            return r(this, void 0, void 0, function() {
                var o;
                return i(this, function(r) {
                    switch (r.label) {
                    case 0:
                        return [4, xysz.res.loadBundle(t)];
                    case 1:
                        return o = r.sent(),
                        [2, new Promise(function(t, r) {
                            o.loadDir(e, n, function(e, n) {
                                e ? r(e) : t(n)
                            })
                        }
                        )]
                    }
                })
            })
        }
        ,
        t.base64ToTexture = function(t) {
            return new Promise(function(e) {
                var n = new Image;
                n.src = t,
                n.onload = function() {
                    var t = new cc.Texture2D;
                    t.initWithElement(n),
                    t.handleLoadedTexture(),
                    e(t)
                }
            }
            )
        }
        ,
        t
    }(), j = {
        captureNode: function(t) {
            return r(this, void 0, void 0, function() {
                var e, n, o, r;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return [4, xysz.tool.tweenDelay()];
                    case 1:
                        return i.sent(),
                        [4, xysz.h5.captureCanvas()];
                    case 2:
                        return e = i.sent(),
                        n = t.getBoundingBoxToWorld(),
                        o = xysz.tool.convertToCanvasBox(n),
                        [4, xysz.h5.cutCapture(e, o)];
                    case 3:
                        return r = i.sent(),
                        [4, xysz.h5.generateImageTag(r)];
                    case 4:
                        return [2, i.sent()]
                    }
                })
            })
        },
        captureAndCoverNode: function(t, e) {
            return r(this, void 0, void 0, function() {
                var n, o, r, s;
                return i(this, function(i) {
                    switch (i.label) {
                    case 0:
                        return i.trys.push([0, 2, , 3]),
                        [4, xysz.h5.captureNode(t)];
                    case 1:
                        return n = i.sent(),
                        o = t.getBoundingBoxToWorld(),
                        r = xysz.tool.convertToDeviceBox(o),
                        n.style.width = r.width + "px",
                        n.style.height = r.height + "px",
                        xysz.h5.addTagToTop(n, r.x + "px", r.y + "px"),
                        e && xysz.h5.listenTagTouchTime(n, function(t) {
                            t > 300 && e()
                        }),
                        [2, n];
                    case 2:
                        return s = i.sent(),
                        cc.error(s),
                        [2, new Image];
                    case 3:
                        return [2]
                    }
                })
            })
        },
        captureCanvas: function() {
            return new Promise(function(t) {
                cc.director.once(cc.Director.EVENT_AFTER_DRAW, function() {
                    t(cc.game.canvas.toDataURL())
                })
            }
            )
        },
        generateImageTag: function(t) {
            return new Promise(function(e) {
                var n = new Image;
                n.src = t,
                n.onload = function() {
                    e(n)
                }
            }
            )
        },
        addTagToTop: function(t, e, n) {
            if (t)
                return t.style.position = "absolute",
                e && (t.style.left = e),
                n && (t.style.top = n),
                t.parentNode || cc.game.container.appendChild(t),
                t
        },
        tryRemoveTag: function(t) {
            t && t.parentNode && t.remove()
        },
        listenTagTouchTime: function(t, e) {
            if (t) {
                var n = 0;
                t.ontouchstart = function() {
                    n = Date.now()
                }
                ,
                t.ontouchend = function() {
                    e(Date.now() - n)
                }
                ,
                t.ontouchcancel = function() {
                    e(Date.now() - n)
                }
                ,
                t.onmousedown = function() {
                    n = Date.now()
                }
                ,
                t.onmouseup = function() {
                    e(Date.now() - n)
                }
            }
        },
        cutCapture: function(t, e) {
            return new Promise(function(n) {
                var o = document.createElement("canvas")
                  , r = o.getContext("2d");
                o.width = e.width,
                o.height = e.height;
                var i = new Image;
                i.src = t,
                i.onload = function() {
                    r.drawImage(i, e.x, e.y, e.width, e.height, 0, 0, e.width, e.height);
                    var t = o.toDataURL("image/jpg", 1);
                    n(t)
                }
            }
            )
        },
        copyContentH5: function(t) {
            var e = document.createElement("input");
            document.body.appendChild(e),
            e.setAttribute("value", t),
            e.setAttribute("readonly", "readonly"),
            e.select(),
            e.setSelectionRange(0, 999);
            var n = document.execCommand("copy");
            return document.body.removeChild(e),
            n
        },
        showConsole: function() {
            xysz.h5.loadSDK("https://gz-cdn-1258783731.cos.ap-guangzhou.myqcloud.com/qiehuang_game/h5/sdk/vconsole.min.js").then(function() {
                new VConsole
            })
        },
        browserFullScreen: function() {
            var t = document.documentElement;
            t.requestFullscreen ? t.requestFullscreen() : t.mozRequestFullScreen ? t.mozRequestFullScreen() : t.webkitRequestFullscreen ? t.webkitRequestFullscreen() : t.msRequestFullscreen && t.msRequestFullscreen()
        },
        browserExitFullscreen: function() {
            this.isFullScreen() && (document.exitFullscreen ? document.exitFullscreen() : document.msExitFullscreen ? document.msExitFullscreen() : document.mozCancelFullScreen ? document.mozCancelFullScreen() : document.webkitExitFullscreen && document.webkitExitFullscreen())
        },
        isFullScreen: function() {
            return !!(document.fullscreen || document.mozFullScreen || document.webkitIsFullScreen || document.webkitFullScreen || document.msFullScreen)
        },
        loadSDK: function(t) {
            return new Promise(function(e) {
                var n = document.createElement("script");
                n.type = "text/javascript",
                n.src = t,
                n.onload = e,
                document.body.appendChild(n)
            }
            )
        },
        listenNetworkStatus: function(t, e) {
            document.body.addEventListener && (window.addEventListener("online", t, !0),
            window.addEventListener("offline", e, !0))
        },
        getIsDeviceLandscape: function() {
            return 90 == window.orientation || -90 == window.orientation
        },
        addListenOrientationChange: function() {
            window.addEventListener("onorientationchange"in window ? "orientationchange" : "resize", function() {
                return cc.game.emit(c.DeviceOrientation)
            }, !1)
        },
        listenDeviceOrientation: function(t) {
            window.DeviceOrientationEvent ? window.addEventListener("deviceorientation", t, !1) : console.log("\u8be5\u6d4f\u89c8\u5668\u4e0d\u652f\u6301deviceOrientation")
        },
        drawDeviceBox: function(t) {
            var e = document.createElement("div");
            e.innerHTML = "testtest",
            e.style.backgroundColor = "#F00",
            e.style.width = t.width + "px",
            e.style.height = t.height + "px",
            xysz.h5.addTagToTop(e, t.x + "px", t.y + "px")
        }
    }, F = 8;
    function H(t) {
        return Y(V(q(t), t.length * F))
    }
    function V(t, e) {
        t[e >> 5] |= 128 << e % 32,
        t[14 + (e + 64 >>> 9 << 4)] = e;
        for (var n = 1732584193, o = -271733879, r = -1732584194, i = 271733878, s = 0; s < t.length; s += 16) {
            var c = n
              , a = o
              , u = r
              , l = i;
            n = U(n, o, r, i, t[s + 0], 7, -680876936),
            i = U(i, n, o, r, t[s + 1], 12, -389564586),
            r = U(r, i, n, o, t[s + 2], 17, 606105819),
            o = U(o, r, i, n, t[s + 3], 22, -1044525330),
            n = U(n, o, r, i, t[s + 4], 7, -176418897),
            i = U(i, n, o, r, t[s + 5], 12, 1200080426),
            r = U(r, i, n, o, t[s + 6], 17, -1473231341),
            o = U(o, r, i, n, t[s + 7], 22, -45705983),
            n = U(n, o, r, i, t[s + 8], 7, 1770035416),
            i = U(i, n, o, r, t[s + 9], 12, -1958414417),
            r = U(r, i, n, o, t[s + 10], 17, -42063),
            o = U(o, r, i, n, t[s + 11], 22, -1990404162),
            n = U(n, o, r, i, t[s + 12], 7, 1804603682),
            i = U(i, n, o, r, t[s + 13], 12, -40341101),
            r = U(r, i, n, o, t[s + 14], 17, -1502002290),
            n = K(n, o = U(o, r, i, n, t[s + 15], 22, 1236535329), r, i, t[s + 1], 5, -165796510),
            i = K(i, n, o, r, t[s + 6], 9, -1069501632),
            r = K(r, i, n, o, t[s + 11], 14, 643717713),
            o = K(o, r, i, n, t[s + 0], 20, -373897302),
            n = K(n, o, r, i, t[s + 5], 5, -701558691),
            i = K(i, n, o, r, t[s + 10], 9, 38016083),
            r = K(r, i, n, o, t[s + 15], 14, -660478335),
            o = K(o, r, i, n, t[s + 4], 20, -405537848),
            n = K(n, o, r, i, t[s + 9], 5, 568446438),
            i = K(i, n, o, r, t[s + 14], 9, -1019803690),
            r = K(r, i, n, o, t[s + 3], 14, -187363961),
            o = K(o, r, i, n, t[s + 8], 20, 1163531501),
            n = K(n, o, r, i, t[s + 13], 5, -1444681467),
            i = K(i, n, o, r, t[s + 2], 9, -51403784),
            r = K(r, i, n, o, t[s + 7], 14, 1735328473),
            n = G(n, o = K(o, r, i, n, t[s + 12], 20, -1926607734), r, i, t[s + 5], 4, -378558),
            i = G(i, n, o, r, t[s + 8], 11, -2022574463),
            r = G(r, i, n, o, t[s + 11], 16, 1839030562),
            o = G(o, r, i, n, t[s + 14], 23, -35309556),
            n = G(n, o, r, i, t[s + 1], 4, -1530992060),
            i = G(i, n, o, r, t[s + 4], 11, 1272893353),
            r = G(r, i, n, o, t[s + 7], 16, -155497632),
            o = G(o, r, i, n, t[s + 10], 23, -1094730640),
            n = G(n, o, r, i, t[s + 13], 4, 681279174),
            i = G(i, n, o, r, t[s + 0], 11, -358537222),
            r = G(r, i, n, o, t[s + 3], 16, -722521979),
            o = G(o, r, i, n, t[s + 6], 23, 76029189),
            n = G(n, o, r, i, t[s + 9], 4, -640364487),
            i = G(i, n, o, r, t[s + 12], 11, -421815835),
            r = G(r, i, n, o, t[s + 15], 16, 530742520),
            n = J(n, o = G(o, r, i, n, t[s + 2], 23, -995338651), r, i, t[s + 0], 6, -198630844),
            i = J(i, n, o, r, t[s + 7], 10, 1126891415),
            r = J(r, i, n, o, t[s + 14], 15, -1416354905),
            o = J(o, r, i, n, t[s + 5], 21, -57434055),
            n = J(n, o, r, i, t[s + 12], 6, 1700485571),
            i = J(i, n, o, r, t[s + 3], 10, -1894986606),
            r = J(r, i, n, o, t[s + 10], 15, -1051523),
            o = J(o, r, i, n, t[s + 1], 21, -2054922799),
            n = J(n, o, r, i, t[s + 8], 6, 1873313359),
            i = J(i, n, o, r, t[s + 15], 10, -30611744),
            r = J(r, i, n, o, t[s + 6], 15, -1560198380),
            o = J(o, r, i, n, t[s + 13], 21, 1309151649),
            n = J(n, o, r, i, t[s + 4], 6, -145523070),
            i = J(i, n, o, r, t[s + 11], 10, -1120210379),
            r = J(r, i, n, o, t[s + 2], 15, 718787259),
            o = J(o, r, i, n, t[s + 9], 21, -343485551),
            n = X(n, c),
            o = X(o, a),
            r = X(r, u),
            i = X(i, l)
        }
        return Array(n, o, r, i)
    }
    function W(t, e, n, o, r, i) {
        return X((s = X(X(e, t), X(o, i))) << (c = r) | s >>> 32 - c, n);
        var s, c
    }
    function U(t, e, n, o, r, i, s) {
        return W(e & n | ~e & o, t, e, r, i, s)
    }
    function K(t, e, n, o, r, i, s) {
        return W(e & o | n & ~o, t, e, r, i, s)
    }
    function G(t, e, n, o, r, i, s) {
        return W(e ^ n ^ o, t, e, r, i, s)
    }
    function J(t, e, n, o, r, i, s) {
        return W(n ^ (e | ~o), t, e, r, i, s)
    }
    function X(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }
    function q(t) {
        for (var e = Array(), n = (1 << F) - 1, o = 0; o < t.length * F; o += F)
            e[o >> 5] |= (t.charCodeAt(o / F) & n) << o % 32;
        return e
    }
    function Y(t) {
        for (var e = "", n = 0; n < 4 * t.length; n++)
            e += "0123456789abcdef".charAt(t[n >> 2] >> n % 4 * 8 + 4 & 15) + "0123456789abcdef".charAt(t[n >> 2] >> n % 4 * 8 & 15);
        return e
    }
    var Q = function() {
        function t() {}
        return t.encode = function(t) {
            console.log("=====MD5=====")
            console.log("param: ",t)
            var res = H(t)
            console.log("res: ",res)
            return res
            return H(t)
        }
        ,
        t
    }()
      , Z = 8;
    function $(t) {
        return st(tt(it(t), t.length * Z))
    }
    function tt(t, e) {
        t[e >> 5] |= 128 << 24 - e % 32,
        t[15 + (e + 64 >> 9 << 4)] = e;
        for (var n = Array(80), o = 1732584193, r = -271733879, i = -1732584194, s = 271733878, c = -1009589776, a = 0; a < t.length; a += 16) {
            for (var u = o, l = r, h = i, f = s, p = c, d = 0; d < 80; d++) {
                n[d] = d < 16 ? t[a + d] : rt(n[d - 3] ^ n[d - 8] ^ n[d - 14] ^ n[d - 16], 1);
                var m = ot(ot(rt(o, 5), et(d, r, i, s)), ot(ot(c, n[d]), nt(d)));
                c = s,
                s = i,
                i = rt(r, 30),
                r = o,
                o = m
            }
            o = ot(o, u),
            r = ot(r, l),
            i = ot(i, h),
            s = ot(s, f),
            c = ot(c, p)
        }
        return Array(o, r, i, s, c)
    }
    function et(t, e, n, o) {
        return t < 20 ? e & n | ~e & o : t < 40 ? e ^ n ^ o : t < 60 ? e & n | e & o | n & o : e ^ n ^ o
    }
    function nt(t) {
        return t < 20 ? 1518500249 : t < 40 ? 1859775393 : t < 60 ? -1894007588 : -899497514
    }
    function ot(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }
    function rt(t, e) {
        return t << e | t >>> 32 - e
    }
    function it(t) {
        for (var e = Array(), n = (1 << Z) - 1, o = 0; o < t.length * Z; o += Z)
            e[o >> 5] |= (t.charCodeAt(o / Z) & n) << 32 - Z - o % 32;
        return e
    }
    function st(t) {
        for (var e = "", n = 0; n < 4 * t.length; n++)
            e += "0123456789abcdef".charAt(t[n >> 2] >> 8 * (3 - n % 4) + 4 & 15) + "0123456789abcdef".charAt(t[n >> 2] >> 8 * (3 - n % 4) & 15);
        return e
    }
    var ct = function() {
        function t() {}
        return t.encode = function(t) {
            return $(t).toString()
        }
        ,
        t
    }();
    function at(t, e) {
        return e >>> t | e << 32 - t
    }
    function ut(t, e, n) {
        return t & e ^ ~t & n
    }
    function lt(t, e, n) {
        return t & e ^ t & n ^ e & n
    }
    function ht(t) {
        return at(2, t) ^ at(13, t) ^ at(22, t)
    }
    function ft(t) {
        return at(6, t) ^ at(11, t) ^ at(25, t)
    }
    function pt(t) {
        return at(7, t) ^ at(18, t) ^ t >>> 3
    }
    function dt(t) {
        return at(17, t) ^ at(19, t) ^ t >>> 10
    }
    function mt(t, e) {
        return t[15 & e] += dt(t[e + 14 & 15]) + t[e + 9 & 15] + pt(t[e + 1 & 15])
    }
    var yt, gt, vt, wt = new Array(1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298), _t = "0123456789abcdef";
    function xt(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }
    function bt() {
        var t, e, n, o, r, i, s, c, a, u, l = new Array(16);
        t = yt[0],
        e = yt[1],
        n = yt[2],
        o = yt[3],
        r = yt[4],
        i = yt[5],
        s = yt[6],
        c = yt[7];
        for (var h = 0; h < 16; h++)
            l[h] = vt[3 + (h << 2)] | vt[2 + (h << 2)] << 8 | vt[1 + (h << 2)] << 16 | vt[h << 2] << 24;
        for (var f = 0; f < 64; f++)
            a = c + ft(r) + ut(r, i, s) + wt[f],
            a += f < 16 ? l[f] : mt(l, f),
            u = ht(t) + lt(t, e, n),
            c = s,
            s = i,
            i = r,
            r = xt(o, a),
            o = n,
            n = e,
            e = t,
            t = xt(a, u);
        yt[0] += t,
        yt[1] += e,
        yt[2] += n,
        yt[3] += o,
        yt[4] += r,
        yt[5] += i,
        yt[6] += s,
        yt[7] += c
    }
    function Ct(t, e) {
        var n, o, r = 0;
        o = gt[0] >> 3 & 63;
        var i = 63 & e;
        for ((gt[0] += e << 3) < e << 3 && gt[1]++,
        gt[1] += e >> 29,
        n = 0; n + 63 < e; n += 64) {
            for (var s = o; s < 64; s++)
                vt[s] = t.charCodeAt(r++);
            bt(),
            o = 0
        }
        for (var c = 0; c < i; c++)
            vt[c] = t.charCodeAt(r++)
    }
    function St() {
        var t = gt[0] >> 3 & 63;
        if (vt[t++] = 128,
        t <= 56)
            for (var e = t; e < 56; e++)
                vt[e] = 0;
        else {
            for (e = t; e < 64; e++)
                vt[e] = 0;
            for (bt(),
            e = 0; e < 56; e++)
                vt[e] = 0
        }
        vt[56] = gt[1] >>> 24 & 255,
        vt[57] = gt[1] >>> 16 & 255,
        vt[58] = gt[1] >>> 8 & 255,
        vt[59] = 255 & gt[1],
        vt[60] = gt[0] >>> 24 & 255,
        vt[61] = gt[0] >>> 16 & 255,
        vt[62] = gt[0] >>> 8 & 255,
        vt[63] = 255 & gt[0],
        bt()
    }
    function zt() {
        for (var t = new String, e = 0; e < 8; e++)
            for (var n = 28; n >= 0; n -= 4)
                t += _t.charAt(yt[e] >>> n & 15);
        return t
    }
    var Pt = function() {
        function t() {}
        return t.encode = function(t) {
            return (e = t,
            yt = new Array(8),
            gt = new Array(2),
            vt = new Array(64),
            gt[0] = gt[1] = 0,
            yt[0] = 1779033703,
            yt[1] = 3144134277,
            yt[2] = 1013904242,
            yt[3] = 2773480762,
            yt[4] = 1359893119,
            yt[5] = 2600822924,
            yt[6] = 528734635,
            yt[7] = 1541459225,
            Ct(e, e.length),
            St(),
            zt()).toString();
            var e
        }
        ,
        t
    }()
      , kt = _(function(t) {
        t.exports = function() {
            var t, e, n, o, r, i, s, c, a, u, l, h, f, p, d, m, y, g, v, w, _, x, b, C, S, z, P, k, B, A, T, R, M, D, E, L, O, I, N, j, F, H, V, W, U, K, G, J, X, q, Y, Q, Z, $, tt, et, nt, ot, rt, it, st, ct, at, ut, lt, ht, ft, pt, dt, mt, yt, gt, vt, wt, _t, xt, bt, Ct, St, zt, Pt, kt, Bt, At, Tt, Rt, Mt, Dt, Et, Lt = Lt || (t = Math,
            e = Object.create || function(t) {
                var e;
                return Ot.prototype = t,
                e = new Ot,
                Ot.prototype = null,
                e
            }
            ,
            o = (n = {}).lib = {},
            r = o.Base = {
                extend: function(t) {
                    var n = e(this);
                    return t && n.mixIn(t),
                    n.hasOwnProperty("init") && this.init !== n.init || (n.init = function() {
                        n.$super.init.apply(this, arguments)
                    }
                    ),
                    (n.init.prototype = n).$super = this,
                    n
                },
                create: function() {
                    var t = this.extend();
                    return t.init.apply(t, arguments),
                    t
                },
                init: function() {},
                mixIn: function(t) {
                    for (var e in t)
                        t.hasOwnProperty(e) && (this[e] = t[e]);
                    t.hasOwnProperty("toString") && (this.toString = t.toString)
                },
                clone: function() {
                    return this.init.prototype.extend(this)
                }
            },
            i = o.WordArray = r.extend({
                init: function(t, e) {
                    t = this.words = t || [],
                    this.sigBytes = null != e ? e : 4 * t.length
                },
                toString: function(t) {
                    return (t || c).stringify(this)
                },
                concat: function(t) {
                    var e = this.words
                      , n = t.words
                      , o = this.sigBytes
                      , r = t.sigBytes;
                    if (this.clamp(),
                    o % 4)
                        for (var i = 0; i < r; i++) {
                            var s = n[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                            e[o + i >>> 2] |= s << 24 - (o + i) % 4 * 8
                        }
                    else
                        for (i = 0; i < r; i += 4)
                            e[o + i >>> 2] = n[i >>> 2];
                    return this.sigBytes += r,
                    this
                },
                clamp: function() {
                    var e = this.words
                      , n = this.sigBytes;
                    e[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                    e.length = t.ceil(n / 4)
                },
                clone: function() {
                    var t = r.clone.call(this);
                    return t.words = this.words.slice(0),
                    t
                },
                random: function(e) {
                    function n(e) {
                        e = e;
                        var n = 987654321
                          , o = 4294967295;
                        return function() {
                            var r = ((n = 36969 * (65535 & n) + (n >> 16) & o) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & o) & o;
                            return r /= 4294967296,
                            (r += .5) * (.5 < t.random() ? 1 : -1)
                        }
                    }
                    for (var o, r = [], s = 0; s < e; s += 4) {
                        var c = n(4294967296 * (o || t.random()));
                        o = 987654071 * c(),
                        r.push(4294967296 * c() | 0)
                    }
                    return new i.init(r,e)
                }
            }),
            s = n.enc = {},
            c = s.Hex = {
                stringify: function(t) {
                    for (var e = t.words, n = t.sigBytes, o = [], r = 0; r < n; r++) {
                        var i = e[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                        o.push((i >>> 4).toString(16)),
                        o.push((15 & i).toString(16))
                    }
                    return o.join("")
                },
                parse: function(t) {
                    for (var e = t.length, n = [], o = 0; o < e; o += 2)
                        n[o >>> 3] |= parseInt(t.substr(o, 2), 16) << 24 - o % 8 * 4;
                    return new i.init(n,e / 2)
                }
            },
            a = s.Latin1 = {
                stringify: function(t) {
                    for (var e = t.words, n = t.sigBytes, o = [], r = 0; r < n; r++) {
                        var i = e[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                        o.push(String.fromCharCode(i))
                    }
                    return o.join("")
                },
                parse: function(t) {
                    for (var e = t.length, n = [], o = 0; o < e; o++)
                        n[o >>> 2] |= (255 & t.charCodeAt(o)) << 24 - o % 4 * 8;
                    return new i.init(n,e)
                }
            },
            u = s.Utf8 = {
                stringify: function(t) {
                    try {
                        return decodeURIComponent(escape(a.stringify(t)))
                    } catch (t) {
                        throw new Error("Malformed UTF-8 data")
                    }
                },
                parse: function(t) {
                    return a.parse(unescape(encodeURIComponent(t)))
                }
            },
            l = o.BufferedBlockAlgorithm = r.extend({
                reset: function() {
                    this._data = new i.init,
                    this._nDataBytes = 0
                },
                _append: function(t) {
                    "string" == typeof t && (t = u.parse(t)),
                    this._data.concat(t),
                    this._nDataBytes += t.sigBytes
                },
                _process: function(e) {
                    var n = this._data
                      , o = n.words
                      , r = n.sigBytes
                      , s = this.blockSize
                      , c = r / (4 * s)
                      , a = (c = e ? t.ceil(c) : t.max((0 | c) - this._minBufferSize, 0)) * s
                      , u = t.min(4 * a, r);
                    if (a) {
                        for (var l = 0; l < a; l += s)
                            this._doProcessBlock(o, l);
                        var h = o.splice(0, a);
                        n.sigBytes -= u
                    }
                    return new i.init(h,u)
                },
                clone: function() {
                    var t = r.clone.call(this);
                    return t._data = this._data.clone(),
                    t
                },
                _minBufferSize: 0
            }),
            o.Hasher = l.extend({
                cfg: r.extend(),
                init: function(t) {
                    this.cfg = this.cfg.extend(t),
                    this.reset()
                },
                reset: function() {
                    l.reset.call(this),
                    this._doReset()
                },
                update: function(t) {
                    return this._append(t),
                    this._process(),
                    this
                },
                finalize: function(t) {
                    return t && this._append(t),
                    this._doFinalize()
                },
                blockSize: 16,
                _createHelper: function(t) {
                    return function(e, n) {
                        return new t.init(n).finalize(e)
                    }
                },
                _createHmacHelper: function(t) {
                    return function(e, n) {
                        return new h.HMAC.init(t,n).finalize(e)
                    }
                }
            }),
            h = n.algo = {},
            n);
            function Ot() {}
            function It(t, e, n) {
                return t ^ e ^ n
            }
            function Nt(t, e, n) {
                return t & e | ~t & n
            }
            function jt(t, e, n) {
                return (t | ~e) ^ n
            }
            function Ft(t, e, n) {
                return t & n | e & ~n
            }
            function Ht(t, e, n) {
                return t ^ (e | ~n)
            }
            function Vt(t, e) {
                return t << e | t >>> 32 - e
            }
            function Wt(t, e, n, o) {
                var r = this._iv;
                if (r) {
                    var i = r.slice(0);
                    this._iv = void 0
                } else
                    i = this._prevBlock;
                o.encryptBlock(i, 0);
                for (var s = 0; s < n; s++)
                    t[e + s] ^= i[s]
            }
            function Ut(t) {
                if (255 == (t >> 24 & 255)) {
                    var e = t >> 16 & 255
                      , n = t >> 8 & 255
                      , o = 255 & t;
                    255 === e ? (e = 0,
                    255 === n ? (n = 0,
                    255 === o ? o = 0 : ++o) : ++n) : ++e,
                    t = 0,
                    t += e << 16,
                    t += n << 8,
                    t += o
                } else
                    t += 1 << 24;
                return t
            }
            function Kt() {
                for (var t = this._X, e = this._C, n = 0; n < 8; n++)
                    Ct[n] = e[n];
                for (e[0] = e[0] + 1295307597 + this._b | 0,
                e[1] = e[1] + 3545052371 + (e[0] >>> 0 < Ct[0] >>> 0 ? 1 : 0) | 0,
                e[2] = e[2] + 886263092 + (e[1] >>> 0 < Ct[1] >>> 0 ? 1 : 0) | 0,
                e[3] = e[3] + 1295307597 + (e[2] >>> 0 < Ct[2] >>> 0 ? 1 : 0) | 0,
                e[4] = e[4] + 3545052371 + (e[3] >>> 0 < Ct[3] >>> 0 ? 1 : 0) | 0,
                e[5] = e[5] + 886263092 + (e[4] >>> 0 < Ct[4] >>> 0 ? 1 : 0) | 0,
                e[6] = e[6] + 1295307597 + (e[5] >>> 0 < Ct[5] >>> 0 ? 1 : 0) | 0,
                e[7] = e[7] + 3545052371 + (e[6] >>> 0 < Ct[6] >>> 0 ? 1 : 0) | 0,
                this._b = e[7] >>> 0 < Ct[7] >>> 0 ? 1 : 0,
                n = 0; n < 8; n++) {
                    var o = t[n] + e[n]
                      , r = 65535 & o
                      , i = o >>> 16
                      , s = ((r * r >>> 17) + r * i >>> 15) + i * i
                      , c = ((4294901760 & o) * o | 0) + ((65535 & o) * o | 0);
                    St[n] = s ^ c
                }
                t[0] = St[0] + (St[7] << 16 | St[7] >>> 16) + (St[6] << 16 | St[6] >>> 16) | 0,
                t[1] = St[1] + (St[0] << 8 | St[0] >>> 24) + St[7] | 0,
                t[2] = St[2] + (St[1] << 16 | St[1] >>> 16) + (St[0] << 16 | St[0] >>> 16) | 0,
                t[3] = St[3] + (St[2] << 8 | St[2] >>> 24) + St[1] | 0,
                t[4] = St[4] + (St[3] << 16 | St[3] >>> 16) + (St[2] << 16 | St[2] >>> 16) | 0,
                t[5] = St[5] + (St[4] << 8 | St[4] >>> 24) + St[3] | 0,
                t[6] = St[6] + (St[5] << 16 | St[5] >>> 16) + (St[4] << 16 | St[4] >>> 16) | 0,
                t[7] = St[7] + (St[6] << 8 | St[6] >>> 24) + St[5] | 0
            }
            function Gt() {
                for (var t = this._X, e = this._C, n = 0; n < 8; n++)
                    Mt[n] = e[n];
                for (e[0] = e[0] + 1295307597 + this._b | 0,
                e[1] = e[1] + 3545052371 + (e[0] >>> 0 < Mt[0] >>> 0 ? 1 : 0) | 0,
                e[2] = e[2] + 886263092 + (e[1] >>> 0 < Mt[1] >>> 0 ? 1 : 0) | 0,
                e[3] = e[3] + 1295307597 + (e[2] >>> 0 < Mt[2] >>> 0 ? 1 : 0) | 0,
                e[4] = e[4] + 3545052371 + (e[3] >>> 0 < Mt[3] >>> 0 ? 1 : 0) | 0,
                e[5] = e[5] + 886263092 + (e[4] >>> 0 < Mt[4] >>> 0 ? 1 : 0) | 0,
                e[6] = e[6] + 1295307597 + (e[5] >>> 0 < Mt[5] >>> 0 ? 1 : 0) | 0,
                e[7] = e[7] + 3545052371 + (e[6] >>> 0 < Mt[6] >>> 0 ? 1 : 0) | 0,
                this._b = e[7] >>> 0 < Mt[7] >>> 0 ? 1 : 0,
                n = 0; n < 8; n++) {
                    var o = t[n] + e[n]
                      , r = 65535 & o
                      , i = o >>> 16
                      , s = ((r * r >>> 17) + r * i >>> 15) + i * i
                      , c = ((4294901760 & o) * o | 0) + ((65535 & o) * o | 0);
                    Dt[n] = s ^ c
                }
                t[0] = Dt[0] + (Dt[7] << 16 | Dt[7] >>> 16) + (Dt[6] << 16 | Dt[6] >>> 16) | 0,
                t[1] = Dt[1] + (Dt[0] << 8 | Dt[0] >>> 24) + Dt[7] | 0,
                t[2] = Dt[2] + (Dt[1] << 16 | Dt[1] >>> 16) + (Dt[0] << 16 | Dt[0] >>> 16) | 0,
                t[3] = Dt[3] + (Dt[2] << 8 | Dt[2] >>> 24) + Dt[1] | 0,
                t[4] = Dt[4] + (Dt[3] << 16 | Dt[3] >>> 16) + (Dt[2] << 16 | Dt[2] >>> 16) | 0,
                t[5] = Dt[5] + (Dt[4] << 8 | Dt[4] >>> 24) + Dt[3] | 0,
                t[6] = Dt[6] + (Dt[5] << 16 | Dt[5] >>> 16) + (Dt[4] << 16 | Dt[4] >>> 16) | 0,
                t[7] = Dt[7] + (Dt[6] << 8 | Dt[6] >>> 24) + Dt[5] | 0
            }
            return f = Lt.lib.WordArray,
            Lt.enc.Base64 = {
                stringify: function(t) {
                    var e = t.words
                      , n = t.sigBytes
                      , o = this._map;
                    t.clamp();
                    for (var r = [], i = 0; i < n; i += 3)
                        for (var s = (e[i >>> 2] >>> 24 - i % 4 * 8 & 255) << 16 | (e[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255) << 8 | e[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, c = 0; c < 4 && i + .75 * c < n; c++)
                            r.push(o.charAt(s >>> 6 * (3 - c) & 63));
                    var a = o.charAt(64);
                    if (a)
                        for (; r.length % 4; )
                            r.push(a);
                    return r.join("")
                },
                parse: function(t) {
                    var e = t.length
                      , n = this._map
                      , o = this._reverseMap;
                    if (!o) {
                        o = this._reverseMap = [];
                        for (var r = 0; r < n.length; r++)
                            o[n.charCodeAt(r)] = r
                    }
                    var i = n.charAt(64);
                    if (i) {
                        var s = t.indexOf(i);
                        -1 !== s && (e = s)
                    }
                    return function(t, e, n) {
                        for (var o = [], r = 0, i = 0; i < e; i++)
                            if (i % 4) {
                                var s = n[t.charCodeAt(i - 1)] << i % 4 * 2
                                  , c = n[t.charCodeAt(i)] >>> 6 - i % 4 * 2;
                                o[r >>> 2] |= (s | c) << 24 - r % 4 * 8,
                                r++
                            }
                        return f.create(o, r)
                    }(t, e, o)
                },
                _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
            },
            function(t) {
                var e = Lt
                  , n = e.lib
                  , o = n.WordArray
                  , r = n.Hasher
                  , i = e.algo
                  , s = [];
                !function() {
                    for (var e = 0; e < 64; e++)
                        s[e] = 4294967296 * t.abs(t.sin(e + 1)) | 0
                }();
                var c = i.MD5 = r.extend({
                    _doReset: function() {
                        this._hash = new o.init([1732584193, 4023233417, 2562383102, 271733878])
                    },
                    _doProcessBlock: function(t, e) {
                        for (var n = 0; n < 16; n++) {
                            var o = e + n
                              , r = t[o];
                            t[o] = 16711935 & (r << 8 | r >>> 24) | 4278255360 & (r << 24 | r >>> 8)
                        }
                        var i = this._hash.words
                          , c = t[e + 0]
                          , f = t[e + 1]
                          , p = t[e + 2]
                          , d = t[e + 3]
                          , m = t[e + 4]
                          , y = t[e + 5]
                          , g = t[e + 6]
                          , v = t[e + 7]
                          , w = t[e + 8]
                          , _ = t[e + 9]
                          , x = t[e + 10]
                          , b = t[e + 11]
                          , C = t[e + 12]
                          , S = t[e + 13]
                          , z = t[e + 14]
                          , P = t[e + 15]
                          , k = i[0]
                          , B = i[1]
                          , A = i[2]
                          , T = i[3];
                        k = a(k, B, A, T, c, 7, s[0]),
                        T = a(T, k, B, A, f, 12, s[1]),
                        A = a(A, T, k, B, p, 17, s[2]),
                        B = a(B, A, T, k, d, 22, s[3]),
                        k = a(k, B, A, T, m, 7, s[4]),
                        T = a(T, k, B, A, y, 12, s[5]),
                        A = a(A, T, k, B, g, 17, s[6]),
                        B = a(B, A, T, k, v, 22, s[7]),
                        k = a(k, B, A, T, w, 7, s[8]),
                        T = a(T, k, B, A, _, 12, s[9]),
                        A = a(A, T, k, B, x, 17, s[10]),
                        B = a(B, A, T, k, b, 22, s[11]),
                        k = a(k, B, A, T, C, 7, s[12]),
                        T = a(T, k, B, A, S, 12, s[13]),
                        A = a(A, T, k, B, z, 17, s[14]),
                        k = u(k, B = a(B, A, T, k, P, 22, s[15]), A, T, f, 5, s[16]),
                        T = u(T, k, B, A, g, 9, s[17]),
                        A = u(A, T, k, B, b, 14, s[18]),
                        B = u(B, A, T, k, c, 20, s[19]),
                        k = u(k, B, A, T, y, 5, s[20]),
                        T = u(T, k, B, A, x, 9, s[21]),
                        A = u(A, T, k, B, P, 14, s[22]),
                        B = u(B, A, T, k, m, 20, s[23]),
                        k = u(k, B, A, T, _, 5, s[24]),
                        T = u(T, k, B, A, z, 9, s[25]),
                        A = u(A, T, k, B, d, 14, s[26]),
                        B = u(B, A, T, k, w, 20, s[27]),
                        k = u(k, B, A, T, S, 5, s[28]),
                        T = u(T, k, B, A, p, 9, s[29]),
                        A = u(A, T, k, B, v, 14, s[30]),
                        k = l(k, B = u(B, A, T, k, C, 20, s[31]), A, T, y, 4, s[32]),
                        T = l(T, k, B, A, w, 11, s[33]),
                        A = l(A, T, k, B, b, 16, s[34]),
                        B = l(B, A, T, k, z, 23, s[35]),
                        k = l(k, B, A, T, f, 4, s[36]),
                        T = l(T, k, B, A, m, 11, s[37]),
                        A = l(A, T, k, B, v, 16, s[38]),
                        B = l(B, A, T, k, x, 23, s[39]),
                        k = l(k, B, A, T, S, 4, s[40]),
                        T = l(T, k, B, A, c, 11, s[41]),
                        A = l(A, T, k, B, d, 16, s[42]),
                        B = l(B, A, T, k, g, 23, s[43]),
                        k = l(k, B, A, T, _, 4, s[44]),
                        T = l(T, k, B, A, C, 11, s[45]),
                        A = l(A, T, k, B, P, 16, s[46]),
                        k = h(k, B = l(B, A, T, k, p, 23, s[47]), A, T, c, 6, s[48]),
                        T = h(T, k, B, A, v, 10, s[49]),
                        A = h(A, T, k, B, z, 15, s[50]),
                        B = h(B, A, T, k, y, 21, s[51]),
                        k = h(k, B, A, T, C, 6, s[52]),
                        T = h(T, k, B, A, d, 10, s[53]),
                        A = h(A, T, k, B, x, 15, s[54]),
                        B = h(B, A, T, k, f, 21, s[55]),
                        k = h(k, B, A, T, w, 6, s[56]),
                        T = h(T, k, B, A, P, 10, s[57]),
                        A = h(A, T, k, B, g, 15, s[58]),
                        B = h(B, A, T, k, S, 21, s[59]),
                        k = h(k, B, A, T, m, 6, s[60]),
                        T = h(T, k, B, A, b, 10, s[61]),
                        A = h(A, T, k, B, p, 15, s[62]),
                        B = h(B, A, T, k, _, 21, s[63]),
                        i[0] = i[0] + k | 0,
                        i[1] = i[1] + B | 0,
                        i[2] = i[2] + A | 0,
                        i[3] = i[3] + T | 0
                    },
                    _doFinalize: function() {
                        var e = this._data
                          , n = e.words
                          , o = 8 * this._nDataBytes
                          , r = 8 * e.sigBytes;
                        n[r >>> 5] |= 128 << 24 - r % 32;
                        var i = t.floor(o / 4294967296)
                          , s = o;
                        n[15 + (64 + r >>> 9 << 4)] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
                        n[14 + (64 + r >>> 9 << 4)] = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8),
                        e.sigBytes = 4 * (n.length + 1),
                        this._process();
                        for (var c = this._hash, a = c.words, u = 0; u < 4; u++) {
                            var l = a[u];
                            a[u] = 16711935 & (l << 8 | l >>> 24) | 4278255360 & (l << 24 | l >>> 8)
                        }
                        return c
                    },
                    clone: function() {
                        var t = r.clone.call(this);
                        return t._hash = this._hash.clone(),
                        t
                    }
                });
                function a(t, e, n, o, r, i, s) {
                    var c = t + (e & n | ~e & o) + r + s;
                    return (c << i | c >>> 32 - i) + e
                }
                function u(t, e, n, o, r, i, s) {
                    var c = t + (e & o | n & ~o) + r + s;
                    return (c << i | c >>> 32 - i) + e
                }
                function l(t, e, n, o, r, i, s) {
                    var c = t + (e ^ n ^ o) + r + s;
                    return (c << i | c >>> 32 - i) + e
                }
                function h(t, e, n, o, r, i, s) {
                    var c = t + (n ^ (e | ~o)) + r + s;
                    return (c << i | c >>> 32 - i) + e
                }
                e.MD5 = r._createHelper(c),
                e.HmacMD5 = r._createHmacHelper(c)
            }(Math),
            d = (p = Lt).lib,
            m = d.WordArray,
            y = d.Hasher,
            g = p.algo,
            v = [],
            w = g.SHA1 = y.extend({
                _doReset: function() {
                    this._hash = new m.init([1732584193, 4023233417, 2562383102, 271733878, 3285377520])
                },
                _doProcessBlock: function(t, e) {
                    for (var n = this._hash.words, o = n[0], r = n[1], i = n[2], s = n[3], c = n[4], a = 0; a < 80; a++) {
                        if (a < 16)
                            v[a] = 0 | t[e + a];
                        else {
                            var u = v[a - 3] ^ v[a - 8] ^ v[a - 14] ^ v[a - 16];
                            v[a] = u << 1 | u >>> 31
                        }
                        var l = (o << 5 | o >>> 27) + c + v[a];
                        l += a < 20 ? 1518500249 + (r & i | ~r & s) : a < 40 ? 1859775393 + (r ^ i ^ s) : a < 60 ? (r & i | r & s | i & s) - 1894007588 : (r ^ i ^ s) - 899497514,
                        c = s,
                        s = i,
                        i = r << 30 | r >>> 2,
                        r = o,
                        o = l
                    }
                    n[0] = n[0] + o | 0,
                    n[1] = n[1] + r | 0,
                    n[2] = n[2] + i | 0,
                    n[3] = n[3] + s | 0,
                    n[4] = n[4] + c | 0
                },
                _doFinalize: function() {
                    var t = this._data
                      , e = t.words
                      , n = 8 * this._nDataBytes
                      , o = 8 * t.sigBytes;
                    return e[o >>> 5] |= 128 << 24 - o % 32,
                    e[14 + (64 + o >>> 9 << 4)] = Math.floor(n / 4294967296),
                    e[15 + (64 + o >>> 9 << 4)] = n,
                    t.sigBytes = 4 * e.length,
                    this._process(),
                    this._hash
                },
                clone: function() {
                    var t = y.clone.call(this);
                    return t._hash = this._hash.clone(),
                    t
                }
            }),
            p.SHA1 = y._createHelper(w),
            p.HmacSHA1 = y._createHmacHelper(w),
            function(t) {
                var e = Lt
                  , n = e.lib
                  , o = n.WordArray
                  , r = n.Hasher
                  , i = e.algo
                  , s = []
                  , c = [];
                !function() {
                    function e(e) {
                        for (var n = t.sqrt(e), o = 2; o <= n; o++)
                            if (!(e % o))
                                return;
                        return 1
                    }
                    function n(t) {
                        return 4294967296 * (t - (0 | t)) | 0
                    }
                    for (var o = 2, r = 0; r < 64; )
                        e(o) && (r < 8 && (s[r] = n(t.pow(o, .5))),
                        c[r] = n(t.pow(o, 1 / 3)),
                        r++),
                        o++
                }();
                var a = []
                  , u = i.SHA256 = r.extend({
                    _doReset: function() {
                        this._hash = new o.init(s.slice(0))
                    },
                    _doProcessBlock: function(t, e) {
                        for (var n = this._hash.words, o = n[0], r = n[1], i = n[2], s = n[3], u = n[4], l = n[5], h = n[6], f = n[7], p = 0; p < 64; p++) {
                            if (p < 16)
                                a[p] = 0 | t[e + p];
                            else {
                                var d = a[p - 15]
                                  , m = (d << 25 | d >>> 7) ^ (d << 14 | d >>> 18) ^ d >>> 3
                                  , y = a[p - 2]
                                  , g = (y << 15 | y >>> 17) ^ (y << 13 | y >>> 19) ^ y >>> 10;
                                a[p] = m + a[p - 7] + g + a[p - 16]
                            }
                            var v = o & r ^ o & i ^ r & i
                              , w = (o << 30 | o >>> 2) ^ (o << 19 | o >>> 13) ^ (o << 10 | o >>> 22)
                              , _ = f + ((u << 26 | u >>> 6) ^ (u << 21 | u >>> 11) ^ (u << 7 | u >>> 25)) + (u & l ^ ~u & h) + c[p] + a[p];
                            f = h,
                            h = l,
                            l = u,
                            u = s + _ | 0,
                            s = i,
                            i = r,
                            r = o,
                            o = _ + (w + v) | 0
                        }
                        n[0] = n[0] + o | 0,
                        n[1] = n[1] + r | 0,
                        n[2] = n[2] + i | 0,
                        n[3] = n[3] + s | 0,
                        n[4] = n[4] + u | 0,
                        n[5] = n[5] + l | 0,
                        n[6] = n[6] + h | 0,
                        n[7] = n[7] + f | 0
                    },
                    _doFinalize: function() {
                        var e = this._data
                          , n = e.words
                          , o = 8 * this._nDataBytes
                          , r = 8 * e.sigBytes;
                        return n[r >>> 5] |= 128 << 24 - r % 32,
                        n[14 + (64 + r >>> 9 << 4)] = t.floor(o / 4294967296),
                        n[15 + (64 + r >>> 9 << 4)] = o,
                        e.sigBytes = 4 * n.length,
                        this._process(),
                        this._hash
                    },
                    clone: function() {
                        var t = r.clone.call(this);
                        return t._hash = this._hash.clone(),
                        t
                    }
                });
                e.SHA256 = r._createHelper(u),
                e.HmacSHA256 = r._createHmacHelper(u)
            }(Math),
            function() {
                var t = Lt.lib.WordArray
                  , e = Lt.enc;
                function n(t) {
                    return t << 8 & 4278255360 | t >>> 8 & 16711935
                }
                e.Utf16 = e.Utf16BE = {
                    stringify: function(t) {
                        for (var e = t.words, n = t.sigBytes, o = [], r = 0; r < n; r += 2) {
                            var i = e[r >>> 2] >>> 16 - r % 4 * 8 & 65535;
                            o.push(String.fromCharCode(i))
                        }
                        return o.join("")
                    },
                    parse: function(e) {
                        for (var n = e.length, o = [], r = 0; r < n; r++)
                            o[r >>> 1] |= e.charCodeAt(r) << 16 - r % 2 * 16;
                        return t.create(o, 2 * n)
                    }
                },
                e.Utf16LE = {
                    stringify: function(t) {
                        for (var e = t.words, o = t.sigBytes, r = [], i = 0; i < o; i += 2) {
                            var s = n(e[i >>> 2] >>> 16 - i % 4 * 8 & 65535);
                            r.push(String.fromCharCode(s))
                        }
                        return r.join("")
                    },
                    parse: function(e) {
                        for (var o = e.length, r = [], i = 0; i < o; i++)
                            r[i >>> 1] |= n(e.charCodeAt(i) << 16 - i % 2 * 16);
                        return t.create(r, 2 * o)
                    }
                }
            }(),
            function() {
                if ("function" == typeof ArrayBuffer) {
                    var t = Lt.lib.WordArray
                      , e = t.init;
                    (t.init = function(t) {
                        if (t instanceof ArrayBuffer && (t = new Uint8Array(t)),
                        (t instanceof Int8Array || "undefined" != typeof Uint8ClampedArray && t instanceof Uint8ClampedArray || t instanceof Int16Array || t instanceof Uint16Array || t instanceof Int32Array || t instanceof Uint32Array || t instanceof Float32Array || t instanceof Float64Array) && (t = new Uint8Array(t.buffer,t.byteOffset,t.byteLength)),
                        t instanceof Uint8Array) {
                            for (var n = t.byteLength, o = [], r = 0; r < n; r++)
                                o[r >>> 2] |= t[r] << 24 - r % 4 * 8;
                            e.call(this, o, n)
                        } else
                            e.apply(this, arguments)
                    }
                    ).prototype = t
                }
            }(),
            x = (_ = Lt).lib,
            b = x.WordArray,
            C = x.Hasher,
            S = _.algo,
            z = b.create([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8, 3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12, 1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2, 4, 0, 5, 9, 7, 12, 2, 10, 14, 1, 3, 8, 11, 6, 15, 13]),
            P = b.create([5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12, 6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2, 15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13, 8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14, 12, 15, 10, 4, 1, 5, 8, 7, 6, 2, 13, 14, 0, 3, 9, 11]),
            k = b.create([11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8, 7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12, 11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5, 11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12, 9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6]),
            B = b.create([8, 9, 9, 11, 13, 15, 15, 5, 7, 7, 8, 11, 14, 14, 12, 6, 9, 13, 15, 7, 12, 8, 9, 11, 7, 7, 12, 7, 6, 15, 13, 11, 9, 7, 15, 11, 8, 6, 6, 14, 12, 13, 5, 14, 13, 13, 7, 5, 15, 5, 8, 11, 14, 14, 6, 14, 6, 9, 12, 9, 12, 5, 15, 8, 8, 5, 12, 9, 12, 5, 14, 6, 8, 13, 6, 5, 15, 13, 11, 11]),
            A = b.create([0, 1518500249, 1859775393, 2400959708, 2840853838]),
            T = b.create([1352829926, 1548603684, 1836072691, 2053994217, 0]),
            R = S.RIPEMD160 = C.extend({
                _doReset: function() {
                    this._hash = b.create([1732584193, 4023233417, 2562383102, 271733878, 3285377520])
                },
                _doProcessBlock: function(t, e) {
                    for (var n = 0; n < 16; n++) {
                        var o = e + n
                          , r = t[o];
                        t[o] = 16711935 & (r << 8 | r >>> 24) | 4278255360 & (r << 24 | r >>> 8)
                    }
                    var i, s, c, a, u, l, h, f, p, d, m, y = this._hash.words, g = A.words, v = T.words, w = z.words, _ = P.words, x = k.words, b = B.words;
                    for (l = i = y[0],
                    h = s = y[1],
                    f = c = y[2],
                    p = a = y[3],
                    d = u = y[4],
                    n = 0; n < 80; n += 1)
                        m = i + t[e + w[n]] | 0,
                        m += n < 16 ? It(s, c, a) + g[0] : n < 32 ? Nt(s, c, a) + g[1] : n < 48 ? jt(s, c, a) + g[2] : n < 64 ? Ft(s, c, a) + g[3] : Ht(s, c, a) + g[4],
                        m = (m = Vt(m |= 0, x[n])) + u | 0,
                        i = u,
                        u = a,
                        a = Vt(c, 10),
                        c = s,
                        s = m,
                        m = l + t[e + _[n]] | 0,
                        m += n < 16 ? Ht(h, f, p) + v[0] : n < 32 ? Ft(h, f, p) + v[1] : n < 48 ? jt(h, f, p) + v[2] : n < 64 ? Nt(h, f, p) + v[3] : It(h, f, p) + v[4],
                        m = (m = Vt(m |= 0, b[n])) + d | 0,
                        l = d,
                        d = p,
                        p = Vt(f, 10),
                        f = h,
                        h = m;
                    m = y[1] + c + p | 0,
                    y[1] = y[2] + a + d | 0,
                    y[2] = y[3] + u + l | 0,
                    y[3] = y[4] + i + h | 0,
                    y[4] = y[0] + s + f | 0,
                    y[0] = m
                },
                _doFinalize: function() {
                    var t = this._data
                      , e = t.words
                      , n = 8 * this._nDataBytes
                      , o = 8 * t.sigBytes;
                    e[o >>> 5] |= 128 << 24 - o % 32,
                    e[14 + (64 + o >>> 9 << 4)] = 16711935 & (n << 8 | n >>> 24) | 4278255360 & (n << 24 | n >>> 8),
                    t.sigBytes = 4 * (e.length + 1),
                    this._process();
                    for (var r = this._hash, i = r.words, s = 0; s < 5; s++) {
                        var c = i[s];
                        i[s] = 16711935 & (c << 8 | c >>> 24) | 4278255360 & (c << 24 | c >>> 8)
                    }
                    return r
                },
                clone: function() {
                    var t = C.clone.call(this);
                    return t._hash = this._hash.clone(),
                    t
                }
            }),
            _.RIPEMD160 = C._createHelper(R),
            _.HmacRIPEMD160 = C._createHmacHelper(R),
            M = Lt.lib.Base,
            D = Lt.enc.Utf8,
            Lt.algo.HMAC = M.extend({
                init: function(t, e) {
                    t = this._hasher = new t.init,
                    "string" == typeof e && (e = D.parse(e));
                    var n = t.blockSize
                      , o = 4 * n;
                    e.sigBytes > o && (e = t.finalize(e)),
                    e.clamp();
                    for (var r = this._oKey = e.clone(), i = this._iKey = e.clone(), s = r.words, c = i.words, a = 0; a < n; a++)
                        s[a] ^= 1549556828,
                        c[a] ^= 909522486;
                    r.sigBytes = i.sigBytes = o,
                    this.reset()
                },
                reset: function() {
                    var t = this._hasher;
                    t.reset(),
                    t.update(this._iKey)
                },
                update: function(t) {
                    return this._hasher.update(t),
                    this
                },
                finalize: function(t) {
                    var e = this._hasher
                      , n = e.finalize(t);
                    return e.reset(),
                    e.finalize(this._oKey.clone().concat(n))
                }
            }),
            O = (L = (E = Lt).lib).Base,
            I = L.WordArray,
            j = (N = E.algo).SHA1,
            F = N.HMAC,
            H = N.PBKDF2 = O.extend({
                cfg: O.extend({
                    keySize: 4,
                    hasher: j,
                    iterations: 1
                }),
                init: function(t) {
                    this.cfg = this.cfg.extend(t)
                },
                compute: function(t, e) {
                    for (var n = this.cfg, o = F.create(n.hasher, t), r = I.create(), i = I.create([1]), s = r.words, c = i.words, a = n.keySize, u = n.iterations; s.length < a; ) {
                        var l = o.update(e).finalize(i);
                        o.reset();
                        for (var h = l.words, f = h.length, p = l, d = 1; d < u; d++) {
                            p = o.finalize(p),
                            o.reset();
                            for (var m = p.words, y = 0; y < f; y++)
                                h[y] ^= m[y]
                        }
                        r.concat(l),
                        c[0]++
                    }
                    return r.sigBytes = 4 * a,
                    r
                }
            }),
            E.PBKDF2 = function(t, e, n) {
                return H.create(n).compute(t, e)
            }
            ,
            U = (W = (V = Lt).lib).Base,
            K = W.WordArray,
            J = (G = V.algo).MD5,
            X = G.EvpKDF = U.extend({
                cfg: U.extend({
                    keySize: 4,
                    hasher: J,
                    iterations: 1
                }),
                init: function(t) {
                    this.cfg = this.cfg.extend(t)
                },
                compute: function(t, e) {
                    for (var n = this.cfg, o = n.hasher.create(), r = K.create(), i = r.words, s = n.keySize, c = n.iterations; i.length < s; ) {
                        a && o.update(a);
                        var a = o.update(t).finalize(e);
                        o.reset();
                        for (var u = 1; u < c; u++)
                            a = o.finalize(a),
                            o.reset();
                        r.concat(a)
                    }
                    return r.sigBytes = 4 * s,
                    r
                }
            }),
            V.EvpKDF = function(t, e, n) {
                return X.create(n).compute(t, e)
            }
            ,
            Y = (q = Lt).lib.WordArray,
            Q = q.algo,
            Z = Q.SHA256,
            $ = Q.SHA224 = Z.extend({
                _doReset: function() {
                    this._hash = new Y.init([3238371032, 914150663, 812702999, 4144912697, 4290775857, 1750603025, 1694076839, 3204075428])
                },
                _doFinalize: function() {
                    var t = Z._doFinalize.call(this);
                    return t.sigBytes -= 4,
                    t
                }
            }),
            q.SHA224 = Z._createHelper($),
            q.HmacSHA224 = Z._createHmacHelper($),
            tt = Lt.lib,
            et = tt.Base,
            nt = tt.WordArray,
            (ot = Lt.x64 = {}).Word = et.extend({
                init: function(t, e) {
                    this.high = t,
                    this.low = e
                }
            }),
            ot.WordArray = et.extend({
                init: function(t, e) {
                    t = this.words = t || [],
                    this.sigBytes = null != e ? e : 8 * t.length
                },
                toX32: function() {
                    for (var t = this.words, e = t.length, n = [], o = 0; o < e; o++) {
                        var r = t[o];
                        n.push(r.high),
                        n.push(r.low)
                    }
                    return nt.create(n, this.sigBytes)
                },
                clone: function() {
                    for (var t = et.clone.call(this), e = t.words = this.words.slice(0), n = e.length, o = 0; o < n; o++)
                        e[o] = e[o].clone();
                    return t
                }
            }),
            function(t) {
                var e = Lt
                  , n = e.lib
                  , o = n.WordArray
                  , r = n.Hasher
                  , i = e.x64.Word
                  , s = e.algo
                  , c = []
                  , a = []
                  , u = [];
                !function() {
                    for (var t = 1, e = 0, n = 0; n < 24; n++) {
                        c[t + 5 * e] = (n + 1) * (n + 2) / 2 % 64;
                        var o = (2 * t + 3 * e) % 5;
                        t = e % 5,
                        e = o
                    }
                    for (t = 0; t < 5; t++)
                        for (e = 0; e < 5; e++)
                            a[t + 5 * e] = e + (2 * t + 3 * e) % 5 * 5;
                    for (var r = 1, s = 0; s < 24; s++) {
                        for (var l = 0, h = 0, f = 0; f < 7; f++) {
                            if (1 & r) {
                                var p = (1 << f) - 1;
                                p < 32 ? h ^= 1 << p : l ^= 1 << p - 32
                            }
                            128 & r ? r = r << 1 ^ 113 : r <<= 1
                        }
                        u[s] = i.create(l, h)
                    }
                }();
                var l = [];
                !function() {
                    for (var t = 0; t < 25; t++)
                        l[t] = i.create()
                }();
                var h = s.SHA3 = r.extend({
                    cfg: r.cfg.extend({
                        outputLength: 512
                    }),
                    _doReset: function() {
                        for (var t = this._state = [], e = 0; e < 25; e++)
                            t[e] = new i.init;
                        this.blockSize = (1600 - 2 * this.cfg.outputLength) / 32
                    },
                    _doProcessBlock: function(t, e) {
                        for (var n = this._state, o = this.blockSize / 2, r = 0; r < o; r++) {
                            var i = t[e + 2 * r]
                              , s = t[e + 2 * r + 1];
                            i = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
                            s = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8),
                            (B = n[r]).high ^= s,
                            B.low ^= i
                        }
                        for (var h = 0; h < 24; h++) {
                            for (var f = 0; f < 5; f++) {
                                for (var p = 0, d = 0, m = 0; m < 5; m++)
                                    p ^= (B = n[f + 5 * m]).high,
                                    d ^= B.low;
                                var y = l[f];
                                y.high = p,
                                y.low = d
                            }
                            for (f = 0; f < 5; f++) {
                                var g = l[(f + 4) % 5]
                                  , v = l[(f + 1) % 5]
                                  , w = v.high
                                  , _ = v.low;
                                for (p = g.high ^ (w << 1 | _ >>> 31),
                                d = g.low ^ (_ << 1 | w >>> 31),
                                m = 0; m < 5; m++)
                                    (B = n[f + 5 * m]).high ^= p,
                                    B.low ^= d
                            }
                            for (var x = 1; x < 25; x++) {
                                var b = (B = n[x]).high
                                  , C = B.low
                                  , S = c[x];
                                S < 32 ? (p = b << S | C >>> 32 - S,
                                d = C << S | b >>> 32 - S) : (p = C << S - 32 | b >>> 64 - S,
                                d = b << S - 32 | C >>> 64 - S);
                                var z = l[a[x]];
                                z.high = p,
                                z.low = d
                            }
                            var P = l[0]
                              , k = n[0];
                            for (P.high = k.high,
                            P.low = k.low,
                            f = 0; f < 5; f++)
                                for (m = 0; m < 5; m++) {
                                    var B = n[x = f + 5 * m]
                                      , A = l[x]
                                      , T = l[(f + 1) % 5 + 5 * m]
                                      , R = l[(f + 2) % 5 + 5 * m];
                                    B.high = A.high ^ ~T.high & R.high,
                                    B.low = A.low ^ ~T.low & R.low
                                }
                            B = n[0];
                            var M = u[h];
                            B.high ^= M.high,
                            B.low ^= M.low
                        }
                    },
                    _doFinalize: function() {
                        var e = this._data
                          , n = e.words
                          , r = (this._nDataBytes,
                        8 * e.sigBytes)
                          , i = 32 * this.blockSize;
                        n[r >>> 5] |= 1 << 24 - r % 32,
                        n[(t.ceil((1 + r) / i) * i >>> 5) - 1] |= 128,
                        e.sigBytes = 4 * n.length,
                        this._process();
                        for (var s = this._state, c = this.cfg.outputLength / 8, a = c / 8, u = [], l = 0; l < a; l++) {
                            var h = s[l]
                              , f = h.high
                              , p = h.low;
                            f = 16711935 & (f << 8 | f >>> 24) | 4278255360 & (f << 24 | f >>> 8),
                            p = 16711935 & (p << 8 | p >>> 24) | 4278255360 & (p << 24 | p >>> 8),
                            u.push(p),
                            u.push(f)
                        }
                        return new o.init(u,c)
                    },
                    clone: function() {
                        for (var t = r.clone.call(this), e = t._state = this._state.slice(0), n = 0; n < 25; n++)
                            e[n] = e[n].clone();
                        return t
                    }
                });
                e.SHA3 = r._createHelper(h),
                e.HmacSHA3 = r._createHmacHelper(h)
            }(Math),
            function() {
                var t = Lt
                  , e = t.lib.Hasher
                  , n = t.x64
                  , o = n.Word
                  , r = n.WordArray
                  , i = t.algo;
                function s() {
                    return o.create.apply(o, arguments)
                }
                var c = [s(1116352408, 3609767458), s(1899447441, 602891725), s(3049323471, 3964484399), s(3921009573, 2173295548), s(961987163, 4081628472), s(1508970993, 3053834265), s(2453635748, 2937671579), s(2870763221, 3664609560), s(3624381080, 2734883394), s(310598401, 1164996542), s(607225278, 1323610764), s(1426881987, 3590304994), s(1925078388, 4068182383), s(2162078206, 991336113), s(2614888103, 633803317), s(3248222580, 3479774868), s(3835390401, 2666613458), s(4022224774, 944711139), s(264347078, 2341262773), s(604807628, 2007800933), s(770255983, 1495990901), s(1249150122, 1856431235), s(1555081692, 3175218132), s(1996064986, 2198950837), s(2554220882, 3999719339), s(2821834349, 766784016), s(2952996808, 2566594879), s(3210313671, 3203337956), s(3336571891, 1034457026), s(3584528711, 2466948901), s(113926993, 3758326383), s(338241895, 168717936), s(666307205, 1188179964), s(773529912, 1546045734), s(1294757372, 1522805485), s(1396182291, 2643833823), s(1695183700, 2343527390), s(1986661051, 1014477480), s(2177026350, 1206759142), s(2456956037, 344077627), s(2730485921, 1290863460), s(2820302411, 3158454273), s(3259730800, 3505952657), s(3345764771, 106217008), s(3516065817, 3606008344), s(3600352804, 1432725776), s(4094571909, 1467031594), s(275423344, 851169720), s(430227734, 3100823752), s(506948616, 1363258195), s(659060556, 3750685593), s(883997877, 3785050280), s(958139571, 3318307427), s(1322822218, 3812723403), s(1537002063, 2003034995), s(1747873779, 3602036899), s(1955562222, 1575990012), s(2024104815, 1125592928), s(2227730452, 2716904306), s(2361852424, 442776044), s(2428436474, 593698344), s(2756734187, 3733110249), s(3204031479, 2999351573), s(3329325298, 3815920427), s(3391569614, 3928383900), s(3515267271, 566280711), s(3940187606, 3454069534), s(4118630271, 4000239992), s(116418474, 1914138554), s(174292421, 2731055270), s(289380356, 3203993006), s(460393269, 320620315), s(685471733, 587496836), s(852142971, 1086792851), s(1017036298, 365543100), s(1126000580, 2618297676), s(1288033470, 3409855158), s(1501505948, 4234509866), s(1607167915, 987167468), s(1816402316, 1246189591)]
                  , a = [];
                !function() {
                    for (var t = 0; t < 80; t++)
                        a[t] = s()
                }();
                var u = i.SHA512 = e.extend({
                    _doReset: function() {
                        this._hash = new r.init([new o.init(1779033703,4089235720), new o.init(3144134277,2227873595), new o.init(1013904242,4271175723), new o.init(2773480762,1595750129), new o.init(1359893119,2917565137), new o.init(2600822924,725511199), new o.init(528734635,4215389547), new o.init(1541459225,327033209)])
                    },
                    _doProcessBlock: function(t, e) {
                        for (var n = this._hash.words, o = n[0], r = n[1], i = n[2], s = n[3], u = n[4], l = n[5], h = n[6], f = n[7], p = o.high, d = o.low, m = r.high, y = r.low, g = i.high, v = i.low, w = s.high, _ = s.low, x = u.high, b = u.low, C = l.high, S = l.low, z = h.high, P = h.low, k = f.high, B = f.low, A = p, T = d, R = m, M = y, D = g, E = v, L = w, O = _, I = x, N = b, j = C, F = S, H = z, V = P, W = k, U = B, K = 0; K < 80; K++) {
                            var G = a[K];
                            if (K < 16)
                                var J = G.high = 0 | t[e + 2 * K]
                                  , X = G.low = 0 | t[e + 2 * K + 1];
                            else {
                                var q = a[K - 15]
                                  , Y = q.high
                                  , Q = q.low
                                  , Z = (Y >>> 1 | Q << 31) ^ (Y >>> 8 | Q << 24) ^ Y >>> 7
                                  , $ = (Q >>> 1 | Y << 31) ^ (Q >>> 8 | Y << 24) ^ (Q >>> 7 | Y << 25)
                                  , tt = a[K - 2]
                                  , et = tt.high
                                  , nt = tt.low
                                  , ot = (et >>> 19 | nt << 13) ^ (et << 3 | nt >>> 29) ^ et >>> 6
                                  , rt = (nt >>> 19 | et << 13) ^ (nt << 3 | et >>> 29) ^ (nt >>> 6 | et << 26)
                                  , it = a[K - 7]
                                  , st = it.high
                                  , ct = it.low
                                  , at = a[K - 16]
                                  , ut = at.high
                                  , lt = at.low;
                                J = (J = (J = Z + st + ((X = $ + ct) >>> 0 < $ >>> 0 ? 1 : 0)) + ot + ((X += rt) >>> 0 < rt >>> 0 ? 1 : 0)) + ut + ((X += lt) >>> 0 < lt >>> 0 ? 1 : 0),
                                G.high = J,
                                G.low = X
                            }
                            var ht, ft = I & j ^ ~I & H, pt = N & F ^ ~N & V, dt = A & R ^ A & D ^ R & D, mt = T & M ^ T & E ^ M & E, yt = (A >>> 28 | T << 4) ^ (A << 30 | T >>> 2) ^ (A << 25 | T >>> 7), gt = (T >>> 28 | A << 4) ^ (T << 30 | A >>> 2) ^ (T << 25 | A >>> 7), vt = (I >>> 14 | N << 18) ^ (I >>> 18 | N << 14) ^ (I << 23 | N >>> 9), wt = (N >>> 14 | I << 18) ^ (N >>> 18 | I << 14) ^ (N << 23 | I >>> 9), _t = c[K], xt = _t.high, bt = _t.low, Ct = W + vt + ((ht = U + wt) >>> 0 < U >>> 0 ? 1 : 0), St = gt + mt;
                            W = H,
                            U = V,
                            H = j,
                            V = F,
                            j = I,
                            F = N,
                            I = L + (Ct = (Ct = (Ct = Ct + ft + ((ht += pt) >>> 0 < pt >>> 0 ? 1 : 0)) + xt + ((ht += bt) >>> 0 < bt >>> 0 ? 1 : 0)) + J + ((ht += X) >>> 0 < X >>> 0 ? 1 : 0)) + ((N = O + ht | 0) >>> 0 < O >>> 0 ? 1 : 0) | 0,
                            L = D,
                            O = E,
                            D = R,
                            E = M,
                            R = A,
                            M = T,
                            A = Ct + (yt + dt + (St >>> 0 < gt >>> 0 ? 1 : 0)) + ((T = ht + St | 0) >>> 0 < ht >>> 0 ? 1 : 0) | 0
                        }
                        d = o.low = d + T,
                        o.high = p + A + (d >>> 0 < T >>> 0 ? 1 : 0),
                        y = r.low = y + M,
                        r.high = m + R + (y >>> 0 < M >>> 0 ? 1 : 0),
                        v = i.low = v + E,
                        i.high = g + D + (v >>> 0 < E >>> 0 ? 1 : 0),
                        _ = s.low = _ + O,
                        s.high = w + L + (_ >>> 0 < O >>> 0 ? 1 : 0),
                        b = u.low = b + N,
                        u.high = x + I + (b >>> 0 < N >>> 0 ? 1 : 0),
                        S = l.low = S + F,
                        l.high = C + j + (S >>> 0 < F >>> 0 ? 1 : 0),
                        P = h.low = P + V,
                        h.high = z + H + (P >>> 0 < V >>> 0 ? 1 : 0),
                        B = f.low = B + U,
                        f.high = k + W + (B >>> 0 < U >>> 0 ? 1 : 0)
                    },
                    _doFinalize: function() {
                        var t = this._data
                          , e = t.words
                          , n = 8 * this._nDataBytes
                          , o = 8 * t.sigBytes;
                        return e[o >>> 5] |= 128 << 24 - o % 32,
                        e[30 + (128 + o >>> 10 << 5)] = Math.floor(n / 4294967296),
                        e[31 + (128 + o >>> 10 << 5)] = n,
                        t.sigBytes = 4 * e.length,
                        this._process(),
                        this._hash.toX32()
                    },
                    clone: function() {
                        var t = e.clone.call(this);
                        return t._hash = this._hash.clone(),
                        t
                    },
                    blockSize: 32
                });
                t.SHA512 = e._createHelper(u),
                t.HmacSHA512 = e._createHmacHelper(u)
            }(),
            it = (rt = Lt).x64,
            st = it.Word,
            ct = it.WordArray,
            at = rt.algo,
            ut = at.SHA512,
            lt = at.SHA384 = ut.extend({
                _doReset: function() {
                    this._hash = new ct.init([new st.init(3418070365,3238371032), new st.init(1654270250,914150663), new st.init(2438529370,812702999), new st.init(355462360,4144912697), new st.init(1731405415,4290775857), new st.init(2394180231,1750603025), new st.init(3675008525,1694076839), new st.init(1203062813,3204075428)])
                },
                _doFinalize: function() {
                    var t = ut._doFinalize.call(this);
                    return t.sigBytes -= 16,
                    t
                }
            }),
            rt.SHA384 = ut._createHelper(lt),
            rt.HmacSHA384 = ut._createHmacHelper(lt),
            Lt.lib.Cipher || function() {
                var t = Lt
                  , e = t.lib
                  , n = e.Base
                  , o = e.WordArray
                  , r = e.BufferedBlockAlgorithm
                  , i = t.enc
                  , s = (i.Utf8,
                i.Base64)
                  , c = t.algo.EvpKDF
                  , a = e.Cipher = r.extend({
                    cfg: n.extend(),
                    createEncryptor: function(t, e) {
                        return this.create(this._ENC_XFORM_MODE, t, e)
                    },
                    createDecryptor: function(t, e) {
                        return this.create(this._DEC_XFORM_MODE, t, e)
                    },
                    init: function(t, e, n) {
                        this.cfg = this.cfg.extend(n),
                        this._xformMode = t,
                        this._key = e,
                        this.reset()
                    },
                    reset: function() {
                        r.reset.call(this),
                        this._doReset()
                    },
                    process: function(t) {
                        return this._append(t),
                        this._process()
                    },
                    finalize: function(t) {
                        return t && this._append(t),
                        this._doFinalize()
                    },
                    keySize: 4,
                    ivSize: 4,
                    _ENC_XFORM_MODE: 1,
                    _DEC_XFORM_MODE: 2,
                    _createHelper: function(t) {
                        return {
                            encrypt: function(e, n, o) {
                                return u(n).encrypt(t, e, n, o)
                            },
                            decrypt: function(e, n, o) {
                                return u(n).decrypt(t, e, n, o)
                            }
                        }
                    }
                });
                function u(t) {
                    return "string" == typeof t ? _ : v
                }
                e.StreamCipher = a.extend({
                    _doFinalize: function() {
                        return this._process(!0)
                    },
                    blockSize: 1
                });
                var l, h = t.mode = {}, f = e.BlockCipherMode = n.extend({
                    createEncryptor: function(t, e) {
                        return this.Encryptor.create(t, e)
                    },
                    createDecryptor: function(t, e) {
                        return this.Decryptor.create(t, e)
                    },
                    init: function(t, e) {
                        this._cipher = t,
                        this._iv = e
                    }
                }), p = h.CBC = ((l = f.extend()).Encryptor = l.extend({
                    processBlock: function(t, e) {
                        var n = this._cipher
                          , o = n.blockSize;
                        d.call(this, t, e, o),
                        n.encryptBlock(t, e),
                        this._prevBlock = t.slice(e, e + o)
                    }
                }),
                l.Decryptor = l.extend({
                    processBlock: function(t, e) {
                        var n = this._cipher
                          , o = n.blockSize
                          , r = t.slice(e, e + o);
                        n.decryptBlock(t, e),
                        d.call(this, t, e, o),
                        this._prevBlock = r
                    }
                }),
                l);
                function d(t, e, n) {
                    var o = this._iv;
                    if (o) {
                        var r = o;
                        this._iv = void 0
                    } else
                        r = this._prevBlock;
                    for (var i = 0; i < n; i++)
                        t[e + i] ^= r[i]
                }
                var m = (t.pad = {}).Pkcs7 = {
                    pad: function(t, e) {
                        for (var n = 4 * e, r = n - t.sigBytes % n, i = r << 24 | r << 16 | r << 8 | r, s = [], c = 0; c < r; c += 4)
                            s.push(i);
                        var a = o.create(s, r);
                        t.concat(a)
                    },
                    unpad: function(t) {
                        var e = 255 & t.words[t.sigBytes - 1 >>> 2];
                        t.sigBytes -= e
                    }
                }
                  , y = (e.BlockCipher = a.extend({
                    cfg: a.cfg.extend({
                        mode: p,
                        padding: m
                    }),
                    reset: function() {
                        a.reset.call(this);
                        var t = this.cfg
                          , e = t.iv
                          , n = t.mode;
                        if (this._xformMode == this._ENC_XFORM_MODE)
                            var o = n.createEncryptor;
                        else
                            o = n.createDecryptor,
                            this._minBufferSize = 1;
                        this._mode && this._mode.__creator == o ? this._mode.init(this, e && e.words) : (this._mode = o.call(n, this, e && e.words),
                        this._mode.__creator = o)
                    },
                    _doProcessBlock: function(t, e) {
                        this._mode.processBlock(t, e)
                    },
                    _doFinalize: function() {
                        var t = this.cfg.padding;
                        if (this._xformMode == this._ENC_XFORM_MODE) {
                            t.pad(this._data, this.blockSize);
                            var e = this._process(!0)
                        } else
                            e = this._process(!0),
                            t.unpad(e);
                        return e
                    },
                    blockSize: 4
                }),
                e.CipherParams = n.extend({
                    init: function(t) {
                        this.mixIn(t)
                    },
                    toString: function(t) {
                        return (t || this.formatter).stringify(this)
                    }
                }))
                  , g = (t.format = {}).OpenSSL = {
                    stringify: function(t) {
                        var e = t.ciphertext
                          , n = t.salt;
                        if (n)
                            var r = o.create([1398893684, 1701076831]).concat(n).concat(e);
                        else
                            r = e;
                        return r.toString(s)
                    },
                    parse: function(t) {
                        var e = s.parse(t)
                          , n = e.words;
                        if (1398893684 == n[0] && 1701076831 == n[1]) {
                            var r = o.create(n.slice(2, 4));
                            n.splice(0, 4),
                            e.sigBytes -= 16
                        }
                        return y.create({
                            ciphertext: e,
                            salt: r
                        })
                    }
                }
                  , v = e.SerializableCipher = n.extend({
                    cfg: n.extend({
                        format: g
                    }),
                    encrypt: function(t, e, n, o) {
                        o = this.cfg.extend(o);
                        var r = t.createEncryptor(n, o)
                          , i = r.finalize(e)
                          , s = r.cfg;
                        return y.create({
                            ciphertext: i,
                            key: n,
                            iv: s.iv,
                            algorithm: t,
                            mode: s.mode,
                            padding: s.padding,
                            blockSize: t.blockSize,
                            formatter: o.format
                        })
                    },
                    decrypt: function(t, e, n, o) {
                        return o = this.cfg.extend(o),
                        e = this._parse(e, o.format),
                        t.createDecryptor(n, o).finalize(e.ciphertext)
                    },
                    _parse: function(t, e) {
                        return "string" == typeof t ? e.parse(t, this) : t
                    }
                })
                  , w = (t.kdf = {}).OpenSSL = {
                    execute: function(t, e, n, r) {
                        r = r || o.random(8);
                        var i = c.create({
                            keySize: e + n
                        }).compute(t, r)
                          , s = o.create(i.words.slice(e), 4 * n);
                        return i.sigBytes = 4 * e,
                        y.create({
                            key: i,
                            iv: s,
                            salt: r
                        })
                    }
                }
                  , _ = e.PasswordBasedCipher = v.extend({
                    cfg: v.cfg.extend({
                        kdf: w
                    }),
                    encrypt: function(t, e, n, o) {
                        var r = (o = this.cfg.extend(o)).kdf.execute(n, t.keySize, t.ivSize);
                        o.iv = r.iv;
                        var i = v.encrypt.call(this, t, e, r.key, o);
                        return i.mixIn(r),
                        i
                    },
                    decrypt: function(t, e, n, o) {
                        o = this.cfg.extend(o),
                        e = this._parse(e, o.format);
                        var r = o.kdf.execute(n, t.keySize, t.ivSize, e.salt);
                        return o.iv = r.iv,
                        v.decrypt.call(this, t, e, r.key, o)
                    }
                })
            }(),
            Lt.mode.CFB = ((ht = Lt.lib.BlockCipherMode.extend()).Encryptor = ht.extend({
                processBlock: function(t, e) {
                    var n = this._cipher
                      , o = n.blockSize;
                    Wt.call(this, t, e, o, n),
                    this._prevBlock = t.slice(e, e + o)
                }
            }),
            ht.Decryptor = ht.extend({
                processBlock: function(t, e) {
                    var n = this._cipher
                      , o = n.blockSize
                      , r = t.slice(e, e + o);
                    Wt.call(this, t, e, o, n),
                    this._prevBlock = r
                }
            }),
            ht),
            Lt.mode.ECB = ((ft = Lt.lib.BlockCipherMode.extend()).Encryptor = ft.extend({
                processBlock: function(t, e) {
                    this._cipher.encryptBlock(t, e)
                }
            }),
            ft.Decryptor = ft.extend({
                processBlock: function(t, e) {
                    this._cipher.decryptBlock(t, e)
                }
            }),
            ft),
            Lt.pad.AnsiX923 = {
                pad: function(t, e) {
                    var n = t.sigBytes
                      , o = 4 * e
                      , r = o - n % o
                      , i = n + r - 1;
                    t.clamp(),
                    t.words[i >>> 2] |= r << 24 - i % 4 * 8,
                    t.sigBytes += r
                },
                unpad: function(t) {
                    var e = 255 & t.words[t.sigBytes - 1 >>> 2];
                    t.sigBytes -= e
                }
            },
            Lt.pad.Iso10126 = {
                pad: function(t, e) {
                    var n = 4 * e
                      , o = n - t.sigBytes % n;
                    t.concat(Lt.lib.WordArray.random(o - 1)).concat(Lt.lib.WordArray.create([o << 24], 1))
                },
                unpad: function(t) {
                    var e = 255 & t.words[t.sigBytes - 1 >>> 2];
                    t.sigBytes -= e
                }
            },
            Lt.pad.Iso97971 = {
                pad: function(t, e) {
                    t.concat(Lt.lib.WordArray.create([2147483648], 1)),
                    Lt.pad.ZeroPadding.pad(t, e)
                },
                unpad: function(t) {
                    Lt.pad.ZeroPadding.unpad(t),
                    t.sigBytes--
                }
            },
            Lt.mode.OFB = (dt = (pt = Lt.lib.BlockCipherMode.extend()).Encryptor = pt.extend({
                processBlock: function(t, e) {
                    var n = this._cipher
                      , o = n.blockSize
                      , r = this._iv
                      , i = this._keystream;
                    r && (i = this._keystream = r.slice(0),
                    this._iv = void 0),
                    n.encryptBlock(i, 0);
                    for (var s = 0; s < o; s++)
                        t[e + s] ^= i[s]
                }
            }),
            pt.Decryptor = dt,
            pt),
            Lt.pad.NoPadding = {
                pad: function() {},
                unpad: function() {}
            },
            mt = Lt.lib.CipherParams,
            yt = Lt.enc.Hex,
            Lt.format.Hex = {
                stringify: function(t) {
                    return t.ciphertext.toString(yt)
                },
                parse: function(t) {
                    var e = yt.parse(t);
                    return mt.create({
                        ciphertext: e
                    })
                }
            },
            function() {
                var t = Lt
                  , e = t.lib.BlockCipher
                  , n = t.algo
                  , o = []
                  , r = []
                  , i = []
                  , s = []
                  , c = []
                  , a = []
                  , u = []
                  , l = []
                  , h = []
                  , f = [];
                !function() {
                    for (var t = [], e = 0; e < 256; e++)
                        t[e] = e < 128 ? e << 1 : e << 1 ^ 283;
                    var n = 0
                      , p = 0;
                    for (e = 0; e < 256; e++) {
                        var d = p ^ p << 1 ^ p << 2 ^ p << 3 ^ p << 4;
                        d = d >>> 8 ^ 255 & d ^ 99,
                        o[n] = d;
                        var m = t[r[d] = n]
                          , y = t[m]
                          , g = t[y]
                          , v = 257 * t[d] ^ 16843008 * d;
                        i[n] = v << 24 | v >>> 8,
                        s[n] = v << 16 | v >>> 16,
                        c[n] = v << 8 | v >>> 24,
                        a[n] = v,
                        v = 16843009 * g ^ 65537 * y ^ 257 * m ^ 16843008 * n,
                        u[d] = v << 24 | v >>> 8,
                        l[d] = v << 16 | v >>> 16,
                        h[d] = v << 8 | v >>> 24,
                        f[d] = v,
                        n ? (n = m ^ t[t[t[g ^ m]]],
                        p ^= t[t[p]]) : n = p = 1
                    }
                }();
                var p = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
                  , d = n.AES = e.extend({
                    _doReset: function() {
                        if (!this._nRounds || this._keyPriorReset !== this._key) {
                            for (var t = this._keyPriorReset = this._key, e = t.words, n = t.sigBytes / 4, r = 4 * (1 + (this._nRounds = 6 + n)), i = this._keySchedule = [], s = 0; s < r; s++)
                                if (s < n)
                                    i[s] = e[s];
                                else {
                                    var c = i[s - 1];
                                    s % n ? 6 < n && s % n == 4 && (c = o[c >>> 24] << 24 | o[c >>> 16 & 255] << 16 | o[c >>> 8 & 255] << 8 | o[255 & c]) : (c = o[(c = c << 8 | c >>> 24) >>> 24] << 24 | o[c >>> 16 & 255] << 16 | o[c >>> 8 & 255] << 8 | o[255 & c],
                                    c ^= p[s / n | 0] << 24),
                                    i[s] = i[s - n] ^ c
                                }
                            for (var a = this._invKeySchedule = [], d = 0; d < r; d++)
                                s = r - d,
                                c = d % 4 ? i[s] : i[s - 4],
                                a[d] = d < 4 || s <= 4 ? c : u[o[c >>> 24]] ^ l[o[c >>> 16 & 255]] ^ h[o[c >>> 8 & 255]] ^ f[o[255 & c]]
                        }
                    },
                    encryptBlock: function(t, e) {
                        this._doCryptBlock(t, e, this._keySchedule, i, s, c, a, o)
                    },
                    decryptBlock: function(t, e) {
                        var n = t[e + 1];
                        t[e + 1] = t[e + 3],
                        t[e + 3] = n,
                        this._doCryptBlock(t, e, this._invKeySchedule, u, l, h, f, r),
                        n = t[e + 1],
                        t[e + 1] = t[e + 3],
                        t[e + 3] = n
                    },
                    _doCryptBlock: function(t, e, n, o, r, i, s, c) {
                        for (var a = this._nRounds, u = t[e] ^ n[0], l = t[e + 1] ^ n[1], h = t[e + 2] ^ n[2], f = t[e + 3] ^ n[3], p = 4, d = 1; d < a; d++) {
                            var m = o[u >>> 24] ^ r[l >>> 16 & 255] ^ i[h >>> 8 & 255] ^ s[255 & f] ^ n[p++]
                              , y = o[l >>> 24] ^ r[h >>> 16 & 255] ^ i[f >>> 8 & 255] ^ s[255 & u] ^ n[p++]
                              , g = o[h >>> 24] ^ r[f >>> 16 & 255] ^ i[u >>> 8 & 255] ^ s[255 & l] ^ n[p++]
                              , v = o[f >>> 24] ^ r[u >>> 16 & 255] ^ i[l >>> 8 & 255] ^ s[255 & h] ^ n[p++];
                            u = m,
                            l = y,
                            h = g,
                            f = v
                        }
                        m = (c[u >>> 24] << 24 | c[l >>> 16 & 255] << 16 | c[h >>> 8 & 255] << 8 | c[255 & f]) ^ n[p++],
                        y = (c[l >>> 24] << 24 | c[h >>> 16 & 255] << 16 | c[f >>> 8 & 255] << 8 | c[255 & u]) ^ n[p++],
                        g = (c[h >>> 24] << 24 | c[f >>> 16 & 255] << 16 | c[u >>> 8 & 255] << 8 | c[255 & l]) ^ n[p++],
                        v = (c[f >>> 24] << 24 | c[u >>> 16 & 255] << 16 | c[l >>> 8 & 255] << 8 | c[255 & h]) ^ n[p++],
                        t[e] = m,
                        t[e + 1] = y,
                        t[e + 2] = g,
                        t[e + 3] = v
                    },
                    keySize: 8
                });
                t.AES = e._createHelper(d)
            }(),
            function() {
                var t = Lt
                  , e = t.lib
                  , n = e.WordArray
                  , o = e.BlockCipher
                  , r = t.algo
                  , i = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
                  , s = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
                  , c = [1, 2, 4, 6, 8, 10, 12, 14, 15, 17, 19, 21, 23, 25, 27, 28]
                  , a = [{
                    0: 8421888,
                    268435456: 32768,
                    536870912: 8421378,
                    805306368: 2,
                    1073741824: 512,
                    1342177280: 8421890,
                    1610612736: 8389122,
                    1879048192: 8388608,
                    2147483648: 514,
                    2415919104: 8389120,
                    2684354560: 33280,
                    2952790016: 8421376,
                    3221225472: 32770,
                    3489660928: 8388610,
                    3758096384: 0,
                    4026531840: 33282,
                    134217728: 0,
                    402653184: 8421890,
                    671088640: 33282,
                    939524096: 32768,
                    1207959552: 8421888,
                    1476395008: 512,
                    1744830464: 8421378,
                    2013265920: 2,
                    2281701376: 8389120,
                    2550136832: 33280,
                    2818572288: 8421376,
                    3087007744: 8389122,
                    3355443200: 8388610,
                    3623878656: 32770,
                    3892314112: 514,
                    4160749568: 8388608,
                    1: 32768,
                    268435457: 2,
                    536870913: 8421888,
                    805306369: 8388608,
                    1073741825: 8421378,
                    1342177281: 33280,
                    1610612737: 512,
                    1879048193: 8389122,
                    2147483649: 8421890,
                    2415919105: 8421376,
                    2684354561: 8388610,
                    2952790017: 33282,
                    3221225473: 514,
                    3489660929: 8389120,
                    3758096385: 32770,
                    4026531841: 0,
                    134217729: 8421890,
                    402653185: 8421376,
                    671088641: 8388608,
                    939524097: 512,
                    1207959553: 32768,
                    1476395009: 8388610,
                    1744830465: 2,
                    2013265921: 33282,
                    2281701377: 32770,
                    2550136833: 8389122,
                    2818572289: 514,
                    3087007745: 8421888,
                    3355443201: 8389120,
                    3623878657: 0,
                    3892314113: 33280,
                    4160749569: 8421378
                }, {
                    0: 1074282512,
                    16777216: 16384,
                    33554432: 524288,
                    50331648: 1074266128,
                    67108864: 1073741840,
                    83886080: 1074282496,
                    100663296: 1073758208,
                    117440512: 16,
                    134217728: 540672,
                    150994944: 1073758224,
                    167772160: 1073741824,
                    184549376: 540688,
                    201326592: 524304,
                    218103808: 0,
                    234881024: 16400,
                    251658240: 1074266112,
                    8388608: 1073758208,
                    25165824: 540688,
                    41943040: 16,
                    58720256: 1073758224,
                    75497472: 1074282512,
                    92274688: 1073741824,
                    109051904: 524288,
                    125829120: 1074266128,
                    142606336: 524304,
                    159383552: 0,
                    176160768: 16384,
                    192937984: 1074266112,
                    209715200: 1073741840,
                    226492416: 540672,
                    243269632: 1074282496,
                    260046848: 16400,
                    268435456: 0,
                    285212672: 1074266128,
                    301989888: 1073758224,
                    318767104: 1074282496,
                    335544320: 1074266112,
                    352321536: 16,
                    369098752: 540688,
                    385875968: 16384,
                    402653184: 16400,
                    419430400: 524288,
                    436207616: 524304,
                    452984832: 1073741840,
                    469762048: 540672,
                    486539264: 1073758208,
                    503316480: 1073741824,
                    520093696: 1074282512,
                    276824064: 540688,
                    293601280: 524288,
                    310378496: 1074266112,
                    327155712: 16384,
                    343932928: 1073758208,
                    360710144: 1074282512,
                    377487360: 16,
                    394264576: 1073741824,
                    411041792: 1074282496,
                    427819008: 1073741840,
                    444596224: 1073758224,
                    461373440: 524304,
                    478150656: 0,
                    494927872: 16400,
                    511705088: 1074266128,
                    528482304: 540672
                }, {
                    0: 260,
                    1048576: 0,
                    2097152: 67109120,
                    3145728: 65796,
                    4194304: 65540,
                    5242880: 67108868,
                    6291456: 67174660,
                    7340032: 67174400,
                    8388608: 67108864,
                    9437184: 67174656,
                    10485760: 65792,
                    11534336: 67174404,
                    12582912: 67109124,
                    13631488: 65536,
                    14680064: 4,
                    15728640: 256,
                    524288: 67174656,
                    1572864: 67174404,
                    2621440: 0,
                    3670016: 67109120,
                    4718592: 67108868,
                    5767168: 65536,
                    6815744: 65540,
                    7864320: 260,
                    8912896: 4,
                    9961472: 256,
                    11010048: 67174400,
                    12058624: 65796,
                    13107200: 65792,
                    14155776: 67109124,
                    15204352: 67174660,
                    16252928: 67108864,
                    16777216: 67174656,
                    17825792: 65540,
                    18874368: 65536,
                    19922944: 67109120,
                    20971520: 256,
                    22020096: 67174660,
                    23068672: 67108868,
                    24117248: 0,
                    25165824: 67109124,
                    26214400: 67108864,
                    27262976: 4,
                    28311552: 65792,
                    29360128: 67174400,
                    30408704: 260,
                    31457280: 65796,
                    32505856: 67174404,
                    17301504: 67108864,
                    18350080: 260,
                    19398656: 67174656,
                    20447232: 0,
                    21495808: 65540,
                    22544384: 67109120,
                    23592960: 256,
                    24641536: 67174404,
                    25690112: 65536,
                    26738688: 67174660,
                    27787264: 65796,
                    28835840: 67108868,
                    29884416: 67109124,
                    30932992: 67174400,
                    31981568: 4,
                    33030144: 65792
                }, {
                    0: 2151682048,
                    65536: 2147487808,
                    131072: 4198464,
                    196608: 2151677952,
                    262144: 0,
                    327680: 4198400,
                    393216: 2147483712,
                    458752: 4194368,
                    524288: 2147483648,
                    589824: 4194304,
                    655360: 64,
                    720896: 2147487744,
                    786432: 2151678016,
                    851968: 4160,
                    917504: 4096,
                    983040: 2151682112,
                    32768: 2147487808,
                    98304: 64,
                    163840: 2151678016,
                    229376: 2147487744,
                    294912: 4198400,
                    360448: 2151682112,
                    425984: 0,
                    491520: 2151677952,
                    557056: 4096,
                    622592: 2151682048,
                    688128: 4194304,
                    753664: 4160,
                    819200: 2147483648,
                    884736: 4194368,
                    950272: 4198464,
                    1015808: 2147483712,
                    1048576: 4194368,
                    1114112: 4198400,
                    1179648: 2147483712,
                    1245184: 0,
                    1310720: 4160,
                    1376256: 2151678016,
                    1441792: 2151682048,
                    1507328: 2147487808,
                    1572864: 2151682112,
                    1638400: 2147483648,
                    1703936: 2151677952,
                    1769472: 4198464,
                    1835008: 2147487744,
                    1900544: 4194304,
                    1966080: 64,
                    2031616: 4096,
                    1081344: 2151677952,
                    1146880: 2151682112,
                    1212416: 0,
                    1277952: 4198400,
                    1343488: 4194368,
                    1409024: 2147483648,
                    1474560: 2147487808,
                    1540096: 64,
                    1605632: 2147483712,
                    1671168: 4096,
                    1736704: 2147487744,
                    1802240: 2151678016,
                    1867776: 4160,
                    1933312: 2151682048,
                    1998848: 4194304,
                    2064384: 4198464
                }, {
                    0: 128,
                    4096: 17039360,
                    8192: 262144,
                    12288: 536870912,
                    16384: 537133184,
                    20480: 16777344,
                    24576: 553648256,
                    28672: 262272,
                    32768: 16777216,
                    36864: 537133056,
                    40960: 536871040,
                    45056: 553910400,
                    49152: 553910272,
                    53248: 0,
                    57344: 17039488,
                    61440: 553648128,
                    2048: 17039488,
                    6144: 553648256,
                    10240: 128,
                    14336: 17039360,
                    18432: 262144,
                    22528: 537133184,
                    26624: 553910272,
                    30720: 536870912,
                    34816: 537133056,
                    38912: 0,
                    43008: 553910400,
                    47104: 16777344,
                    51200: 536871040,
                    55296: 553648128,
                    59392: 16777216,
                    63488: 262272,
                    65536: 262144,
                    69632: 128,
                    73728: 536870912,
                    77824: 553648256,
                    81920: 16777344,
                    86016: 553910272,
                    90112: 537133184,
                    94208: 16777216,
                    98304: 553910400,
                    102400: 553648128,
                    106496: 17039360,
                    110592: 537133056,
                    114688: 262272,
                    118784: 536871040,
                    122880: 0,
                    126976: 17039488,
                    67584: 553648256,
                    71680: 16777216,
                    75776: 17039360,
                    79872: 537133184,
                    83968: 536870912,
                    88064: 17039488,
                    92160: 128,
                    96256: 553910272,
                    100352: 262272,
                    104448: 553910400,
                    108544: 0,
                    112640: 553648128,
                    116736: 16777344,
                    120832: 262144,
                    124928: 537133056,
                    129024: 536871040
                }, {
                    0: 268435464,
                    256: 8192,
                    512: 270532608,
                    768: 270540808,
                    1024: 268443648,
                    1280: 2097152,
                    1536: 2097160,
                    1792: 268435456,
                    2048: 0,
                    2304: 268443656,
                    2560: 2105344,
                    2816: 8,
                    3072: 270532616,
                    3328: 2105352,
                    3584: 8200,
                    3840: 270540800,
                    128: 270532608,
                    384: 270540808,
                    640: 8,
                    896: 2097152,
                    1152: 2105352,
                    1408: 268435464,
                    1664: 268443648,
                    1920: 8200,
                    2176: 2097160,
                    2432: 8192,
                    2688: 268443656,
                    2944: 270532616,
                    3200: 0,
                    3456: 270540800,
                    3712: 2105344,
                    3968: 268435456,
                    4096: 268443648,
                    4352: 270532616,
                    4608: 270540808,
                    4864: 8200,
                    5120: 2097152,
                    5376: 268435456,
                    5632: 268435464,
                    5888: 2105344,
                    6144: 2105352,
                    6400: 0,
                    6656: 8,
                    6912: 270532608,
                    7168: 8192,
                    7424: 268443656,
                    7680: 270540800,
                    7936: 2097160,
                    4224: 8,
                    4480: 2105344,
                    4736: 2097152,
                    4992: 268435464,
                    5248: 268443648,
                    5504: 8200,
                    5760: 270540808,
                    6016: 270532608,
                    6272: 270540800,
                    6528: 270532616,
                    6784: 8192,
                    7040: 2105352,
                    7296: 2097160,
                    7552: 0,
                    7808: 268435456,
                    8064: 268443656
                }, {
                    0: 1048576,
                    16: 33555457,
                    32: 1024,
                    48: 1049601,
                    64: 34604033,
                    80: 0,
                    96: 1,
                    112: 34603009,
                    128: 33555456,
                    144: 1048577,
                    160: 33554433,
                    176: 34604032,
                    192: 34603008,
                    208: 1025,
                    224: 1049600,
                    240: 33554432,
                    8: 34603009,
                    24: 0,
                    40: 33555457,
                    56: 34604032,
                    72: 1048576,
                    88: 33554433,
                    104: 33554432,
                    120: 1025,
                    136: 1049601,
                    152: 33555456,
                    168: 34603008,
                    184: 1048577,
                    200: 1024,
                    216: 34604033,
                    232: 1,
                    248: 1049600,
                    256: 33554432,
                    272: 1048576,
                    288: 33555457,
                    304: 34603009,
                    320: 1048577,
                    336: 33555456,
                    352: 34604032,
                    368: 1049601,
                    384: 1025,
                    400: 34604033,
                    416: 1049600,
                    432: 1,
                    448: 0,
                    464: 34603008,
                    480: 33554433,
                    496: 1024,
                    264: 1049600,
                    280: 33555457,
                    296: 34603009,
                    312: 1,
                    328: 33554432,
                    344: 1048576,
                    360: 1025,
                    376: 34604032,
                    392: 33554433,
                    408: 34603008,
                    424: 0,
                    440: 34604033,
                    456: 1049601,
                    472: 1024,
                    488: 33555456,
                    504: 1048577
                }, {
                    0: 134219808,
                    1: 131072,
                    2: 134217728,
                    3: 32,
                    4: 131104,
                    5: 134350880,
                    6: 134350848,
                    7: 2048,
                    8: 134348800,
                    9: 134219776,
                    10: 133120,
                    11: 134348832,
                    12: 2080,
                    13: 0,
                    14: 134217760,
                    15: 133152,
                    2147483648: 2048,
                    2147483649: 134350880,
                    2147483650: 134219808,
                    2147483651: 134217728,
                    2147483652: 134348800,
                    2147483653: 133120,
                    2147483654: 133152,
                    2147483655: 32,
                    2147483656: 134217760,
                    2147483657: 2080,
                    2147483658: 131104,
                    2147483659: 134350848,
                    2147483660: 0,
                    2147483661: 134348832,
                    2147483662: 134219776,
                    2147483663: 131072,
                    16: 133152,
                    17: 134350848,
                    18: 32,
                    19: 2048,
                    20: 134219776,
                    21: 134217760,
                    22: 134348832,
                    23: 131072,
                    24: 0,
                    25: 131104,
                    26: 134348800,
                    27: 134219808,
                    28: 134350880,
                    29: 133120,
                    30: 2080,
                    31: 134217728,
                    2147483664: 131072,
                    2147483665: 2048,
                    2147483666: 134348832,
                    2147483667: 133152,
                    2147483668: 32,
                    2147483669: 134348800,
                    2147483670: 134217728,
                    2147483671: 134219808,
                    2147483672: 134350880,
                    2147483673: 134217760,
                    2147483674: 134219776,
                    2147483675: 0,
                    2147483676: 133120,
                    2147483677: 2080,
                    2147483678: 131104,
                    2147483679: 134350848
                }]
                  , u = [4160749569, 528482304, 33030144, 2064384, 129024, 8064, 504, 2147483679]
                  , l = r.DES = o.extend({
                    _doReset: function() {
                        for (var t = this._key.words, e = [], n = 0; n < 56; n++) {
                            var o = i[n] - 1;
                            e[n] = t[o >>> 5] >>> 31 - o % 32 & 1
                        }
                        for (var r = this._subKeys = [], a = 0; a < 16; a++) {
                            var u = r[a] = []
                              , l = c[a];
                            for (n = 0; n < 24; n++)
                                u[n / 6 | 0] |= e[(s[n] - 1 + l) % 28] << 31 - n % 6,
                                u[4 + (n / 6 | 0)] |= e[28 + (s[n + 24] - 1 + l) % 28] << 31 - n % 6;
                            for (u[0] = u[0] << 1 | u[0] >>> 31,
                            n = 1; n < 7; n++)
                                u[n] = u[n] >>> 4 * (n - 1) + 3;
                            u[7] = u[7] << 5 | u[7] >>> 27
                        }
                        var h = this._invSubKeys = [];
                        for (n = 0; n < 16; n++)
                            h[n] = r[15 - n]
                    },
                    encryptBlock: function(t, e) {
                        this._doCryptBlock(t, e, this._subKeys)
                    },
                    decryptBlock: function(t, e) {
                        this._doCryptBlock(t, e, this._invSubKeys)
                    },
                    _doCryptBlock: function(t, e, n) {
                        this._lBlock = t[e],
                        this._rBlock = t[e + 1],
                        h.call(this, 4, 252645135),
                        h.call(this, 16, 65535),
                        f.call(this, 2, 858993459),
                        f.call(this, 8, 16711935),
                        h.call(this, 1, 1431655765);
                        for (var o = 0; o < 16; o++) {
                            for (var r = n[o], i = this._lBlock, s = this._rBlock, c = 0, l = 0; l < 8; l++)
                                c |= a[l][((s ^ r[l]) & u[l]) >>> 0];
                            this._lBlock = s,
                            this._rBlock = i ^ c
                        }
                        var p = this._lBlock;
                        this._lBlock = this._rBlock,
                        this._rBlock = p,
                        h.call(this, 1, 1431655765),
                        f.call(this, 8, 16711935),
                        f.call(this, 2, 858993459),
                        h.call(this, 16, 65535),
                        h.call(this, 4, 252645135),
                        t[e] = this._lBlock,
                        t[e + 1] = this._rBlock
                    },
                    keySize: 2,
                    ivSize: 2,
                    blockSize: 2
                });
                function h(t, e) {
                    var n = (this._lBlock >>> t ^ this._rBlock) & e;
                    this._rBlock ^= n,
                    this._lBlock ^= n << t
                }
                function f(t, e) {
                    var n = (this._rBlock >>> t ^ this._lBlock) & e;
                    this._lBlock ^= n,
                    this._rBlock ^= n << t
                }
                t.DES = o._createHelper(l);
                var p = r.TripleDES = o.extend({
                    _doReset: function() {
                        var t = this._key.words;
                        this._des1 = l.createEncryptor(n.create(t.slice(0, 2))),
                        this._des2 = l.createEncryptor(n.create(t.slice(2, 4))),
                        this._des3 = l.createEncryptor(n.create(t.slice(4, 6)))
                    },
                    encryptBlock: function(t, e) {
                        this._des1.encryptBlock(t, e),
                        this._des2.decryptBlock(t, e),
                        this._des3.encryptBlock(t, e)
                    },
                    decryptBlock: function(t, e) {
                        this._des3.decryptBlock(t, e),
                        this._des2.encryptBlock(t, e),
                        this._des1.decryptBlock(t, e)
                    },
                    keySize: 6,
                    ivSize: 2,
                    blockSize: 2
                });
                t.TripleDES = o._createHelper(p)
            }(),
            function() {
                var t = Lt
                  , e = t.lib.StreamCipher
                  , n = t.algo
                  , o = n.RC4 = e.extend({
                    _doReset: function() {
                        for (var t = this._key, e = t.words, n = t.sigBytes, o = this._S = [], r = 0; r < 256; r++)
                            o[r] = r;
                        r = 0;
                        for (var i = 0; r < 256; r++) {
                            var s = r % n
                              , c = e[s >>> 2] >>> 24 - s % 4 * 8 & 255;
                            i = (i + o[r] + c) % 256;
                            var a = o[r];
                            o[r] = o[i],
                            o[i] = a
                        }
                        this._i = this._j = 0
                    },
                    _doProcessBlock: function(t, e) {
                        t[e] ^= r.call(this)
                    },
                    keySize: 8,
                    ivSize: 0
                });
                function r() {
                    for (var t = this._S, e = this._i, n = this._j, o = 0, r = 0; r < 4; r++) {
                        n = (n + t[e = (e + 1) % 256]) % 256;
                        var i = t[e];
                        t[e] = t[n],
                        t[n] = i,
                        o |= t[(t[e] + t[n]) % 256] << 24 - 8 * r
                    }
                    return this._i = e,
                    this._j = n,
                    o
                }
                t.RC4 = e._createHelper(o);
                var i = n.RC4Drop = o.extend({
                    cfg: o.cfg.extend({
                        drop: 192
                    }),
                    _doReset: function() {
                        o._doReset.call(this);
                        for (var t = this.cfg.drop; 0 < t; t--)
                            r.call(this)
                    }
                });
                t.RC4Drop = e._createHelper(i)
            }(),
            Lt.mode.CTRGladman = (vt = (gt = Lt.lib.BlockCipherMode.extend()).Encryptor = gt.extend({
                processBlock: function(t, e) {
                    var n, o = this._cipher, r = o.blockSize, i = this._iv, s = this._counter;
                    i && (s = this._counter = i.slice(0),
                    this._iv = void 0),
                    0 === ((n = s)[0] = Ut(n[0])) && (n[1] = Ut(n[1]));
                    var c = s.slice(0);
                    o.encryptBlock(c, 0);
                    for (var a = 0; a < r; a++)
                        t[e + a] ^= c[a]
                }
            }),
            gt.Decryptor = vt,
            gt),
            _t = (wt = Lt).lib.StreamCipher,
            xt = wt.algo,
            bt = [],
            Ct = [],
            St = [],
            zt = xt.Rabbit = _t.extend({
                _doReset: function() {
                    for (var t = this._key.words, e = this.cfg.iv, n = 0; n < 4; n++)
                        t[n] = 16711935 & (t[n] << 8 | t[n] >>> 24) | 4278255360 & (t[n] << 24 | t[n] >>> 8);
                    var o = this._X = [t[0], t[3] << 16 | t[2] >>> 16, t[1], t[0] << 16 | t[3] >>> 16, t[2], t[1] << 16 | t[0] >>> 16, t[3], t[2] << 16 | t[1] >>> 16]
                      , r = this._C = [t[2] << 16 | t[2] >>> 16, 4294901760 & t[0] | 65535 & t[1], t[3] << 16 | t[3] >>> 16, 4294901760 & t[1] | 65535 & t[2], t[0] << 16 | t[0] >>> 16, 4294901760 & t[2] | 65535 & t[3], t[1] << 16 | t[1] >>> 16, 4294901760 & t[3] | 65535 & t[0]];
                    for (n = this._b = 0; n < 4; n++)
                        Kt.call(this);
                    for (n = 0; n < 8; n++)
                        r[n] ^= o[n + 4 & 7];
                    if (e) {
                        var i = e.words
                          , s = i[0]
                          , c = i[1]
                          , a = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8)
                          , u = 16711935 & (c << 8 | c >>> 24) | 4278255360 & (c << 24 | c >>> 8)
                          , l = a >>> 16 | 4294901760 & u
                          , h = u << 16 | 65535 & a;
                        for (r[0] ^= a,
                        r[1] ^= l,
                        r[2] ^= u,
                        r[3] ^= h,
                        r[4] ^= a,
                        r[5] ^= l,
                        r[6] ^= u,
                        r[7] ^= h,
                        n = 0; n < 4; n++)
                            Kt.call(this)
                    }
                },
                _doProcessBlock: function(t, e) {
                    var n = this._X;
                    Kt.call(this),
                    bt[0] = n[0] ^ n[5] >>> 16 ^ n[3] << 16,
                    bt[1] = n[2] ^ n[7] >>> 16 ^ n[5] << 16,
                    bt[2] = n[4] ^ n[1] >>> 16 ^ n[7] << 16,
                    bt[3] = n[6] ^ n[3] >>> 16 ^ n[1] << 16;
                    for (var o = 0; o < 4; o++)
                        bt[o] = 16711935 & (bt[o] << 8 | bt[o] >>> 24) | 4278255360 & (bt[o] << 24 | bt[o] >>> 8),
                        t[e + o] ^= bt[o]
                },
                blockSize: 4,
                ivSize: 2
            }),
            wt.Rabbit = _t._createHelper(zt),
            Lt.mode.CTR = (kt = (Pt = Lt.lib.BlockCipherMode.extend()).Encryptor = Pt.extend({
                processBlock: function(t, e) {
                    var n = this._cipher
                      , o = n.blockSize
                      , r = this._iv
                      , i = this._counter;
                    r && (i = this._counter = r.slice(0),
                    this._iv = void 0);
                    var s = i.slice(0);
                    n.encryptBlock(s, 0),
                    i[o - 1] = i[o - 1] + 1 | 0;
                    for (var c = 0; c < o; c++)
                        t[e + c] ^= s[c]
                }
            }),
            Pt.Decryptor = kt,
            Pt),
            At = (Bt = Lt).lib.StreamCipher,
            Tt = Bt.algo,
            Rt = [],
            Mt = [],
            Dt = [],
            Et = Tt.RabbitLegacy = At.extend({
                _doReset: function() {
                    for (var t = this._key.words, e = this.cfg.iv, n = this._X = [t[0], t[3] << 16 | t[2] >>> 16, t[1], t[0] << 16 | t[3] >>> 16, t[2], t[1] << 16 | t[0] >>> 16, t[3], t[2] << 16 | t[1] >>> 16], o = this._C = [t[2] << 16 | t[2] >>> 16, 4294901760 & t[0] | 65535 & t[1], t[3] << 16 | t[3] >>> 16, 4294901760 & t[1] | 65535 & t[2], t[0] << 16 | t[0] >>> 16, 4294901760 & t[2] | 65535 & t[3], t[1] << 16 | t[1] >>> 16, 4294901760 & t[3] | 65535 & t[0]], r = this._b = 0; r < 4; r++)
                        Gt.call(this);
                    for (r = 0; r < 8; r++)
                        o[r] ^= n[r + 4 & 7];
                    if (e) {
                        var i = e.words
                          , s = i[0]
                          , c = i[1]
                          , a = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8)
                          , u = 16711935 & (c << 8 | c >>> 24) | 4278255360 & (c << 24 | c >>> 8)
                          , l = a >>> 16 | 4294901760 & u
                          , h = u << 16 | 65535 & a;
                        for (o[0] ^= a,
                        o[1] ^= l,
                        o[2] ^= u,
                        o[3] ^= h,
                        o[4] ^= a,
                        o[5] ^= l,
                        o[6] ^= u,
                        o[7] ^= h,
                        r = 0; r < 4; r++)
                            Gt.call(this)
                    }
                },
                _doProcessBlock: function(t, e) {
                    var n = this._X;
                    Gt.call(this),
                    Rt[0] = n[0] ^ n[5] >>> 16 ^ n[3] << 16,
                    Rt[1] = n[2] ^ n[7] >>> 16 ^ n[5] << 16,
                    Rt[2] = n[4] ^ n[1] >>> 16 ^ n[7] << 16,
                    Rt[3] = n[6] ^ n[3] >>> 16 ^ n[1] << 16;
                    for (var o = 0; o < 4; o++)
                        Rt[o] = 16711935 & (Rt[o] << 8 | Rt[o] >>> 24) | 4278255360 & (Rt[o] << 24 | Rt[o] >>> 8),
                        t[e + o] ^= Rt[o]
                },
                blockSize: 4,
                ivSize: 2
            }),
            Bt.RabbitLegacy = At._createHelper(Et),
            Lt.pad.ZeroPadding = {
                pad: function(t, e) {
                    var n = 4 * e;
                    t.clamp(),
                    t.sigBytes += n - (t.sigBytes % n || n)
                },
                unpad: function(t) {
                    for (var e = t.words, n = t.sigBytes - 1; !(e[n >>> 2] >>> 24 - n % 4 * 8 & 255); )
                        n--;
                    t.sigBytes = n + 1
                }
            },
            Lt
        }()
    })
      , Bt = function() {
        function t() {}
        return t.encode = function(t, e, n) {
            return e = kt.enc.Utf8.parse(e),
            n = kt.enc.Utf8.parse(n),
            kt.AES.encrypt(t, e, {
                iv: n,
                mode: kt.mode.CBC
            }).toString()
        }
        ,
        t.decode = function(t, e, n) {
            return e = kt.enc.Utf8.parse(e),
            n = kt.enc.Utf8.parse(n),
            kt.AES.decrypt(t, e, {
                iv: n,
                mode: kt.mode.CBC
            }).toString(kt.enc.Utf8)
        }
        ,
        t
    }()
      , At = new (function() {
        function t() {}
        return t.prototype.getSetting = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.getSetting({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.openSetting = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.openSetting({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.authorize = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.authorize({
                    scopes: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getUserInfo = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.getAuthUserInfo({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.navigateBackMiniProgram = function(t) {
            return void 0 === t && (t = {}),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.navigateBackMiniProgram({
                    extraData: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.navigateToMiniProgram = function(t, e, n) {
            return void 0 === n && (n = {}),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(o, r) {
                my.navigateToMiniProgram({
                    appId: t,
                    path: e,
                    extraData: n,
                    success: function(t) {
                        return o(t)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.saveImage = function(t, e) {
            return void 0 === e && (e = !0),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.saveImage({
                    url: t,
                    showActionSheet: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.chooseImage = function(t, e, n) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(o, r) {
                my.chooseImage({
                    count: t,
                    sizeType: e,
                    sourceType: n,
                    success: function(t) {
                        return o(t)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getLocation = function(t, e) {
            return void 0 === t && (t = 30),
            void 0 === e && (e = 0),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.getLocation({
                    cacheTimeout: t,
                    type: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.chooseLocation = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.chooseLocation({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.openLocation = function(t, e, n, o, r) {
            return void 0 === r && (r = 15),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(i, s) {
                my.openLocation({
                    longitude: t,
                    latitude: e,
                    name: n,
                    address: o,
                    scale: r,
                    success: function(t) {
                        return i(t)
                    },
                    fail: function(t) {
                        return s(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.showSharePanel = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.showSharePanel({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.hideShareMenu = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.hideShareMenu({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getSystemInfo = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.getSystemInfo({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.setClipboard = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.setClipboard({
                    text: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getClipboard = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.getClipboard({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.vibrate = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.vibrate({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.vibrateShort = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.vibrateShort({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.vibrateLong = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.vibrateLong({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.onAccelerometerChange = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onAccelerometerChange(function(e) {
                t(e)
            })
        }
        ,
        t.prototype.offAccelerometerChange = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.offAccelerometerChange(function() {
                t()
            })
        }
        ,
        t.prototype.scan = function(t, e) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.scan({
                    type: t,
                    hideAlbum: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.onUserCaptureScreen = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onUserCaptureScreen(function() {
                t()
            })
        }
        ,
        t.prototype.offUserCaptureScreen = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.offUserCaptureScreen(function() {
                t()
            })
        }
        ,
        t.prototype.watchShake = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.watchShake({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.onDeviceMotionChange = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onDeviceMotionChange(function(e) {
                t(e)
            })
        }
        ,
        t.prototype.offDeviceMotionChange = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onDeviceMotionChange(function() {
                t && t()
            })
        }
        ,
        t.prototype.confirm = function(t, e, n, o) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(r, i) {
                my.confirm({
                    title: t,
                    content: e,
                    confirmButtonText: n,
                    cancelButtonText: o,
                    success: function(t) {
                        return r(t)
                    },
                    fail: function(t) {
                        return i(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.showLoading = function(t, e, n) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(o, r) {
                my.showLoading({
                    content: t,
                    delay: e,
                    mask: n,
                    success: function(t) {
                        return o(t)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.hideLoading = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.hideLoading({
                    page: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.showToast = function(t, e, n) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(o, r) {
                my.showToast({
                    content: t,
                    type: e,
                    duration: n,
                    success: function(t) {
                        return o(t)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.hideToast = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.hideToast({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.onAppShow = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onAppShow(function() {
                t && t()
            })
        }
        ,
        t.prototype.offAppShow = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.offAppShow(function() {
                t && t()
            })
        }
        ,
        t.prototype.onAppHide = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.onAppHide(function() {
                t && t()
            })
        }
        ,
        t.prototype.offAppHide = function(t) {
            xysz.runtime === xysz.C_Runtime.taobao && my.offAppHide(function() {
                t && t()
            })
        }
        ,
        t.prototype.loadPlugin = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.loadPlugin({
                    plugin: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getParentAppIdSync = function() {
            if (xysz.runtime === xysz.C_Runtime.taobao)
                return my.getParentAppIdSync().appId
        }
        ,
        t.prototype.toTempFilePath = function(t, e, n) {
            if (void 0 === e && (e = "png"),
            void 0 === n && (n = 1),
            xysz.runtime !== xysz.C_Runtime.taobao)
                return Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3");
            var o = t;
            return t instanceof cc.Node && (o = xysz.tool.convertToCanvasBox(t.getBoundingBoxToWorld())),
            new Promise(function(t, r) {
                var i = cc.game.canvas;
                console.log("ctx", i),
                i.toTempFilePath({
                    x: o.x,
                    y: o.y,
                    width: o.width,
                    height: o.height,
                    destWidth: o.width,
                    destHeight: o.width,
                    fileType: e,
                    quality: n,
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.exit = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.exit({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.getRunScene = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.getRunScene({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.addToDesktop = function(t, e, n, o) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(r, i) {
                my.tb.addToDesktop({
                    miniAppId: t,
                    iconName: e,
                    iconUrl: n,
                    targetUrl: o,
                    success: function(t) {
                        return r(t)
                    },
                    fail: function(t) {
                        return i(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.chooseAddress = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.chooseAddress({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.checkShopFavoredStatus = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.checkShopFavoredStatus({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.favorShop = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.favorShop({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.unFavorShop = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.unFavorShop({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.collectGoods = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.collectGoods({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.unCollectGoods = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.unCollectGoods({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.checkGoodsCollectedStatus = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.checkGoodsCollectedStatus({
                    id: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.openDetail = function(t, e) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.tb.openDetail({
                    itemId: t,
                    forceH5: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.openCart = function(t, e) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.tb.openCart({
                    cartType: t,
                    forceH5: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.addToCart = function(t, e) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.tb.addToCart({
                    itemIds: t,
                    exts: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.showSku = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.showSku({
                    itemId: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.hideSku = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.hideSku({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.confirmCustomOrder = function(t, e, n, o) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(r, i) {
                my.tb.confirmCustomOrder({
                    data: {
                        itemid: t,
                        skuId: e,
                        quantity: n,
                        customization: o
                    },
                    success: function(t) {
                        return r(t)
                    },
                    fail: function(t) {
                        return i(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.joinMemeber = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.joinMemeber({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.detailMember = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.detailMember({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.memberJudge = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.memberJudge({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.memberBaseinfo = function() {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(t, e) {
                my.tb.memberBaseinfo({
                    success: function(e) {
                        return t(e)
                    },
                    fail: function(t) {
                        return e(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.memeberPackageApply = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.memeberPackageApply({
                    activityId: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n("\u4f1a\u5458\u6743\u76ca\u9886\u53d6\u5931\u8d25-" + JSON.stringify(t))
                    }
                })
            }
            )
        }
        ,
        t.prototype.memeberActivityApply = function(t) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(e, n) {
                my.tb.memeberActivityApply({
                    activityId: t,
                    success: function(t) {
                        return e(t)
                    },
                    fail: function(t) {
                        return n(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.openMessage = function(t, e, n) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(o, r) {
                my.tb.openMessage({
                    sellerNick: t,
                    forceH5: e,
                    params: {
                        itemId: n
                    },
                    success: function(t) {
                        return o(t)
                    },
                    fail: function(t) {
                        return r(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.subscribe = function(t, e) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(n, o) {
                my.tb.subscribe({
                    domainKey: t,
                    resourceKeys: e,
                    success: function(t) {
                        return n(t)
                    },
                    fail: function(t) {
                        return o(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.addCalendarPlan = function(t, e, n, o, r) {
            return xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(i, s) {
                my.tb.addCalendarPlan({
                    startDate: t,
                    endDate: e,
                    title: n,
                    description: o,
                    remind: r,
                    success: function(t) {
                        return i(t)
                    },
                    fail: function(t) {
                        return s(t)
                    }
                })
            }
            )
        }
        ,
        t.prototype.navigateToTaobaoPage = function(t, e, n, o, r, i, s) {
            return void 0 === i && (i = "shopindex"),
            void 0 === s && (s = "shopindexbar"),
            xysz.runtime !== xysz.C_Runtime.taobao ? Promise.reject("\u8be5\u5e73\u53f0\u4e0d\u652f\u6301\u6b64\u63a5\u53e3") : new Promise(function(c, a) {
                my.tb.navigateToTaobaoPage({
                    appCode: t,
                    appParams: {
                        orderId: e,
                        shopId: n,
                        OrderListType: o,
                        tabType: r,
                        weexShopSubTab: i,
                        weexShopTab: s
                    },
                    success: function(t) {
                        return c(t)
                    },
                    fail: function(t) {
                        return a(t)
                    }
                })
            }
            )
        }
        ,
        t
    }());
    function Tt() {
        Object.defineProperty(Array.prototype, "ext_random", {
            value: function() {
                return this[Math.floor(Math.random() * this.length)]
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(Array.prototype, "ext_randoms", {
            value: function(t) {
                var e = this
                  , n = [];
                return this.forEach(function(t, e) {
                    return n.push(e)
                }),
                (n = (n = n.sort(function() {
                    return Math.random() - .5
                })).slice(0, t)).map(function(t) {
                    return e[t]
                })
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(Array.prototype, "ext_shuffle", {
            value: function() {
                return this.sort(function() {
                    return Math.random() - .5
                })
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(Array.prototype, "ext_last", {
            value: function() {
                return this[this.length - 1]
            },
            enumerable: !1,
            configurable: !0
        }),
        Object.defineProperty(Array.prototype, "ext_back", {
            value: function(t) {
                return this[this.length - 1 - t]
            },
            enumerable: !1,
            configurable: !0
        }),
        Date.prototype.ext_format = function(t) {
            var e = {
                "M+": this.getMonth() + 1,
                "d+": this.getDate(),
                "h+": this.getHours(),
                "m+": this.getMinutes(),
                "s+": this.getSeconds(),
                "q+": Math.floor((this.getMonth() + 3) / 3),
                S: this.getMilliseconds()
            };
            for (var n in /(y+)/.test(t) && (t = t.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length))),
            e)
                new RegExp("(" + n + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? e[n] : ("00" + e[n]).substr(("" + e[n]).length)));
            return t
        }
    }
    var Rt = a.other
      , Mt = window.navigator.userAgent.toLowerCase();
    window.tbCloud ? Rt = a.taobao : /micromessenger/i.test(Mt) && (Rt = a.browser_wx,
    /miniprogram/i.test(Mt) && (Rt = a.browser_wx));
    var Dt = window.xysz || {};
    return Dt.MSG_MAIN = c,
    Dt.MSG_SUB = s,
    Dt.ViewBase = p,
    Dt.C_Runtime = a,
    Dt.Pool = d,
    Dt.guide = g,
    Dt.tool = b,
    Dt.res = N,
    Dt.regex = {
        phone: /^(?:(?:\+|00)86)?1\d{10}$/,
        chineseName: /^(?:[\u4e00-\u9fa5\xb7]{2,16})$/,
        mail: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    },
    Dt.algorithm = m,
    Dt.anim = y,
    Dt.encrypt = {
        Md5: Q,
        Sha1: ct,
        Sha256: Pt,
        AES: Bt
    },
    Dt.saas = new D,
    Dt.time = new L,
    Dt.ui = new T,
    Dt.http = w,
    Dt.socket = B,
    Dt.sound = E,
    Dt.config = R,
    Dt.h5 = j,
    Dt.query = b.parseQuery((null === location || void 0 === location ? void 0 : location.search) || ""),
    Dt.runtime = Rt,
    Dt.env = "dev",
    Dt.tb = At,
    Dt.wx = {
        program: O,
        web: I
    },
    Dt.ext = Tt,
    Tt(),
    Dt
});
