const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;

function t(e) {
    return (t = "function" == typeof Symbol && "symbol" == typeof Symbol.A ? function (e) {
                return typeof e
            }
            : function (e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            }
    )(e)
}

Object.defineProperty(exports, "__esModule", {
    value: !0
});
var A = "2.0"
    , __g = {};

function s() {
}

function i(e) {
    this.t = (2048 & e) >> 11,
        this.s = (1536 & e) >> 9,
        this.i = 511 & e,
        this.h = 511 & e
}

function h(e) {
    this.s = (3072 & e) >> 10,
        this.h = 1023 & e
}

function a(e) {
    this.a = (3072 & e) >> 10,
        this.c = (768 & e) >> 8,
        this.n = (192 & e) >> 6,
        this.t = 63 & e
}

function c(e) {
    this.s = e >> 10 & 3,
        this.i = 1023 & e
}

function n() {
}

function e(e) {
    this.a = (3072 & e) >> 10,
        this.c = (768 & e) >> 8,
        this.n = (192 & e) >> 6,
        this.t = 63 & e
}

function o(e) {
    this.h = (4095 & e) >> 2,
        this.t = 3 & e
}

function r(e) {
    this.s = e >> 10 & 3,
        this.i = e >> 2 & 255,
        this.t = 3 & e
}

s.prototype.e = function (e) {
    e.o = !1
}
    ,
    i.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                e.r[this.s] = this.i;
                break;
            case 1:
                e.r[this.s] = e.k[this.h]
        }
    }
    ,
    h.prototype.e = function (e) {
        e.k[this.h] = e.r[this.s]
    }
    ,
    a.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                e.r[this.a] = e.r[this.c] + e.r[this.n];
                break;
            case 1:
                e.r[this.a] = e.r[this.c] - e.r[this.n];
                break;
            case 2:
                e.r[this.a] = e.r[this.c] * e.r[this.n];
                break;
            case 3:
                e.r[this.a] = e.r[this.c] / e.r[this.n];
                break;
            case 4:
                e.r[this.a] = e.r[this.c] % e.r[this.n];
                break;
            case 5:
                e.r[this.a] = e.r[this.c] == e.r[this.n];
                break;
            case 6:
                e.r[this.a] = e.r[this.c] >= e.r[this.n];
                break;
            case 7:
                e.r[this.a] = e.r[this.c] || e.r[this.n];
                break;
            case 8:
                e.r[this.a] = e.r[this.c] && e.r[this.n];
                break;
            case 9:
                e.r[this.a] = e.r[this.c] !== e.r[this.n];
                break;
            case 10:
                e.r[this.a] = t(e.r[this.c]);
                break;
            case 11:
                e.r[this.a] = e.r[this.c] in e.r[this.n];
                break;
            case 12:
                e.r[this.a] = e.r[this.c] > e.r[this.n];
                break;
            case 13:
                e.r[this.a] = -e.r[this.c];
                break;
            case 14:
                e.r[this.a] = e.r[this.c] < e.r[this.n];
                break;
            case 15:
                e.r[this.a] = e.r[this.c] & e.r[this.n];
                break;
            case 16:
                e.r[this.a] = e.r[this.c] ^ e.r[this.n];
                break;
            case 17:
                e.r[this.a] = e.r[this.c] << e.r[this.n];
                break;
            case 18:
                e.r[this.a] = e.r[this.c] >>> e.r[this.n];
                break;
            case 19:
                e.r[this.a] = e.r[this.c] | e.r[this.n];
                break;
            case 20:
                e.r[this.a] = !e.r[this.c]
        }
    }
    ,
    c.prototype.e = function (e) {
        e.Q.push(e.C),
            e.B.push(e.k),
            e.C = e.r[this.s],
            e.k = [];
        for (var t = 0; t < this.i; t++)
            e.k.unshift(e.f.pop());
        e.g.push(e.f),
            e.f = []
    }
    ,
    n.prototype.e = function (e) {
        e.C = e.Q.pop(),
            e.k = e.B.pop(),
            e.f = e.g.pop()
    }
    ,
    e.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                e.u = e.r[this.a] >= e.r[this.c];
                break;
            case 1:
                e.u = e.r[this.a] <= e.r[this.c];
                break;
            case 2:
                e.u = e.r[this.a] > e.r[this.c];
                break;
            case 3:
                e.u = e.r[this.a] < e.r[this.c];
                break;
            case 4:
                e.u = e.r[this.a] == e.r[this.c];
                break;
            case 5:
                e.u = e.r[this.a] != e.r[this.c];
                break;
            case 6:
                e.u = e.r[this.a];
                break;
            case 7:
                e.u = !e.r[this.a]
        }
    }
    ,
    o.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                e.C = this.h;
                break;
            case 1:
                e.u && (e.C = this.h);
                break;
            case 2:
                e.u || (e.C = this.h);
                break;
            case 3:
                e.C = this.h,
                    e.w = null
        }
        e.u = !1
    }
    ,
    r.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                for (var t = [], n = 0; n < this.i; n++)
                    t.unshift(e.f.pop());
                e.r[3] = e.r[this.s](t[0], t[1]);
                break;
            case 1:
                for (var r = e.f.pop(), i = [], o = 0; o < this.i; o++)
                    i.unshift(e.f.pop());
                e.r[3] = e.r[this.s][r](i[0], i[1]);
                break;
            case 2:
                for (var a = [], c = 0; c < this.i; c++)
                    a.unshift(e.f.pop());
                e.r[3] = new e.r[this.s](a[0], a[1])
        }
    }
;
var k = function (e) {
    for (var t = 66, n = [], r = 0; r < e.length; r++) {
        var i = 24 ^ e.charCodeAt(r) ^ t;
        n.push(String.fromCharCode(i)),
            t = i
    }
    return n.join("")
};

function Q(e) {
    this.t = (4095 & e) >> 10,
        this.s = (1023 & e) >> 8,
        this.i = 1023 & e,
        this.h = 63 & e
}

function C(e) {
    this.t = (4095 & e) >> 10,
        this.a = (1023 & e) >> 8,
        this.c = (255 & e) >> 6
}

function B(e) {
    this.s = (3072 & e) >> 10,
        this.h = 1023 & e
}

function f(e) {
    this.h = 4095 & e
}

function g(e) {
    this.s = (3072 & e) >> 10
}

function u(e) {
    this.h = 4095 & e
}

function w(e) {
    this.t = (3840 & e) >> 8,
        this.s = (192 & e) >> 6,
        this.i = 63 & e
}

function G() {
    this.r = [0, 0, 0, 0],
        this.C = 0,
        this.Q = [],
        this.k = [],
        this.B = [],
        this.f = [],
        this.g = [],
        this.u = !1,
        this.G = [],
        this.b = [],
        this.o = !1,
        this.w = null,
        this.U = null,
        this.F = [],
        this.R = 0,
        this.J = {
            0: s,
            1: i,
            2: h,
            3: a,
            4: c,
            5: n,
            6: e,
            7: o,
            8: r,
            9: Q,
            10: C,
            11: B,
            12: f,
            13: g,
            14: u,
            15: w
        }
}

Q.prototype.e = function (e) {
    switch (this.t) {
        case 0:
            e.f.push(e.r[this.s]);
            break;
        case 1:
            e.f.push(this.i);
            break;
        case 2:
            e.f.push(e.k[this.h]);
            break;
        case 3:
            e.f.push(k(e.b[this.h]))
    }
}
    ,
    C.prototype.e = function (A) {
        switch (this.t) {
            case 0:
                var t = A.f.pop();
                A.r[this.a] = A.r[this.c][t];
                break;
            case 1:
                var s = A.f.pop()
                    , i = A.f.pop();
                A.r[this.c][s] = i;
                break;
            case 2:
                var h = A.f.pop();
                A.r[this.a] = eval(h)
        }
    }
    ,
    B.prototype.e = function (e) {
        e.r[this.s] = k(e.b[this.h])
    }
    ,
    f.prototype.e = function (e) {
        e.w = this.h
    }
    ,
    g.prototype.e = function (e) {
        throw e.r[this.s]
    }
    ,
    u.prototype.e = function (e) {
        var t = this
            , n = [0];
        e.k.forEach((function (e) {
                n.push(e)
            }
        ));
        var r = function (r) {
            var i = new G;
            return i.k = n,
                i.k[0] = r,
                i.v(e.G, t.h, e.b, e.F),
                i.r[3]
        };
        r.toString = function () {
            return "() { [native code] }"
        }
            ,
            e.r[3] = r
    }
    ,
    w.prototype.e = function (e) {
        switch (this.t) {
            case 0:
                for (var t = {}, n = 0; n < this.i; n++) {
                    var r = e.f.pop();
                    t[e.f.pop()] = r
                }
                e.r[this.s] = t;
                break;
            case 1:
                for (var i = [], o = 0; o < this.i; o++)
                    i.unshift(e.f.pop());
                e.r[this.s] = i
        }
    }
    ,
    G.prototype.D = function (e) {
        for (var t = window.atob(e), n = t.charCodeAt(0) << 8 | t.charCodeAt(1), r = [], i = 2; i < n + 2; i += 2)
            r.push(t.charCodeAt(i) << 8 | t.charCodeAt(i + 1));
        this.G = r;
        for (var o = [], a = n + 2; a < t.length;) {
            var c = t.charCodeAt(a) << 8 | t.charCodeAt(a + 1)
                , u = t.slice(a + 2, a + 2 + c);
            o.push(u),
                a += c + 2
        }
        this.b = o
    }
    ,
    G.prototype.v = function (e, t, n) {
        for (t = t || 0,
                 n = n || [],
                 this.C = t,
                 "string" == typeof e ? this.D(e) : (this.G = e,
                     this.b = n),
                 this.o = !0,
                 this.R = Date.now(); this.o;) {
            var r = this.G[this.C++];
            if ("number" != typeof r)
                break;
            var i = Date.now();
            if (500 < i - this.R)
                return;
            this.R = i;
            try {
                this.e(r)
            } catch (e) {
                this.U = e,
                this.w && (this.C = this.w)
            }
        }
    }
    ,
    G.prototype.e = function (e) {
        var t = (61440 & e) >> 12;
        new this.J[t](e).e(this)
    }
    ,
1 && (new G).v("AxjgB5MAnACoAJwBpAAAABAAIAKcAqgAMAq0AzRJZAZwUpwCqACQACACGAKcBKAAIAOcBagAIAQYAjAUGgKcBqFAuAc5hTSHZAZwqrAIGgA0QJEAJAAYAzAUGgOcCaFANRQ0R2QGcOKwChoANECRACQAsAuQABgDnAmgAJwMgAGcDYwFEAAzBmAGcSqwDhoANECRACQAGAKcD6AAGgKcEKFANEcYApwRoAAxB2AGcXKwEhoANECRACQAGAKcE6AAGgKcFKFANEdkBnGqsBUaADRAkQAkABgCnBagAGAGcdKwFxoANECRACQAGAKcGKAAYAZx+rAZGgA0QJEAJAAYA5waoABgBnIisBsaADRAkQAkABgCnBygABoCnB2hQDRHZAZyWrAeGgA0QJEAJAAYBJwfoAAwFGAGcoawIBoANECRACQAGAOQALAJkAAYBJwfgAlsBnK+sCEaADRAkQAkABgDkACwGpAAGAScH4AJbAZy9rAiGgA0QJEAJACwI5AAGAScH6AAkACcJKgAnCWgAJwmoACcJ4AFnA2MBRAAMw5gBnNasCgaADRAkQAkABgBEio0R5EAJAGwKSAFGACcKqAAEgM0RCQGGAYSATRFZAZzshgAtCs0QCQAGAYSAjRFZAZz1hgAtCw0QCQAEAAgB7AtIAgYAJwqoAASATRBJAkYCRIANEZkBnYqEAgaBxQBOYAoBxQEOYQ0giQKGAmQABgAnC6ABRgBGgo0UhD/MQ8zECALEAgaBxQBOYAoBxQEOYQ0gpEAJAoYARoKNFIQ/zEPkAAgChgLGgkUATmBkgAaAJwuhAUaCjdQFAg5kTSTJAsQCBoHFAE5gCgHFAQ5hDSCkQAkChgBGgo0UhD/MQ+QACAKGAsaCRQCOYGSABoAnC6EBRoKN1AUEDmRNJMkCxgFGgsUPzmPkgAaCJwvhAU0wCQFGAUaCxQGOZISPzZPkQAaCJwvhAU0wCQFGAUaCxQMOZISPzZPkQAaCJwvhAU0wCQFGAUaCxQSOZISPzZPkQAaCJwvhAU0wCQFGAkSAzRBJAlz/B4FUAAAAwUYIAAIBSITFQkTERwABi0GHxITAAAJLwMSGRsXHxMZAAk0Fw8HFh4NAwUABhU1EBceDwAENBcUEAAGNBkTGRcBAAFKAAkvHg4PKz4aEwIAAUsACDIVHB0QEQ4YAAsuAzs7AAoPKToKDgAHMx8SGQUvMQABSAALORoVGCQgERcCAxoACAU3ABEXAgMaAAsFGDcAERcCAxoUCgABSQAGOA8LGBsPAAYYLwsYGw8AAU4ABD8QHAUAAU8ABSkbCQ4BAAFMAAktCh8eDgMHCw8AAU0ADT4TGjQsGQMaFA0FHhkAFz4TGjQsGQMaFA0FHhk1NBkCHgUbGBEPAAFCABg9GgkjIAEmOgUHDQ8eFSU5DggJAwEcAwUAAUMAAUAAAUEADQEtFw0FBwtdWxQTGSAACBwrAxUPBR4ZAAkqGgUDAwMVEQ0ACC4DJD8eAx8RAAQ5GhUYAAFGAAAABjYRExELBAACWhgAAVoAQAg/PTw0NxcQPCQ5C3JZEBs9fkcnDRcUAXZia0Q4EhQgXHojMBY3MWVCNT0uDhMXcGQ7AUFPHigkQUwQFkhaAkEACjkTEQspNBMZPC0ABjkTEQsrLQ==");

var b = function (e) {
    return __g._encrypt(encodeURIComponent(e))
};

module.exports = {
    Q: b
}


var t2 = '2.0'
var tv = {}
tv.ZP = function (tt) {
    return __g._encrypt(encodeURIComponent(tt))
};
var tJ = function (tt) {
    return tt && tt.version && "function" == typeof tt.encrypt ? tt : {
        encrypt: tv.ZP,
        version: tv.XL
    }
};
var tr = {
    "zse93": "101_3_3.0",
    "dc0": "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\"",
    "xZst81": null
}


var tu = tr.dc0
var t4 = function (tt) {
    var te = new URL(tt, "https://www.zhihu.com");
    return "" + te.pathname + te.search
}

var t6 = function (tt) {
    return null == tt ? "" : "string" == typeof tt ? tt : "undefined" != typeof URLSearchParams && (0,
        tc._)(tt, URLSearchParams) ? tt.toString() : tm()(tt) ? JSON.stringify(tt) : t3(tt) ? String(tt) : ""
}

var t8 = function (tt, te) {
    return void 0 === te && (te = 4096),
    !!tt && t7(tt) <= te
}

var ta = '101_3_3.0'


const CryptoJS = require("crypto-js");


const ty = (aaa) => {
    return CryptoJS.MD5(aaa).toString();
}


/*
*
* ta = tr.zse93   #版本号
tu = tr.dc0     #d_c0这个cookie的值
tc = tr.xZst81  #null
tl = t5(tt)     #tl评论url
tf = t3(te)     #""
*
*
* */


function ed(tt, te, tr, ti) {
    var ta = tr.zse93
        , tu = tr.dc0
        , tc = tr.xZst81
        , tf = t4(tt)
        , td = t6(te)
        , tp = [ta, tf, tu, t8(td) && td, tc].filter(Boolean).join("+");
    return {
        source: tp,
        // (0,tJ(ti).encrypt)  ƒ (tt){return __g._encrypt(encodeURIComponent(tt))}
        // signature: (0,tJ(ti).encrypt)(ty(tp))
        signature: b(ty(tp))
    }
}

function tT() {
    if ("undefined" == typeof Reflect || !Reflect.construct || Reflect.construct.sham)
        return !1;
    if ("function" == typeof Proxy)
        return !0;
    try {
        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {
        })),
            !0
    } catch (tt) {
        return !1
    }
}


// tC = td.xZst81 || tp.get("x-zst-81")

tC = null

tf = {
    "headers": {
        "x-requested-with": "fetch",
        "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZ8TY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHHmWgwyThwGOGFxrhLy-upLr0pqtBOBJwFM6hYKfGHKtqOpfUpMmwpCVwSTv4NsNGFLvCNOJcCm8vemnCH9JrO1rQoBb9OsoBXBsMXB-bpCOqSsUu2LlvXqivrMoMYm2G21E9NBgBOyOBHpB9CmqC2mtbeL9cn_wBx1GQOL_D9_fUF9CqfzwDOBJ6H0gDwp3bOCJCH8XU30AGSxAUS06h2GxUxMTCOYL9cLFJO8kH31_gFV1qoqXGwGeHw9HgC8oHtOAgHOVJC_c4SYy9wC87O9BJuYAqgKwhLCGBLC"
    },
    "credentials": "include"
}
var document = {
    // cookie: 'SESSIONID=KWTqqpxR7cCzmRy2Rr1mOfC4Y1PpE9Bq07VtxH8YAnI; JOID=V1EWC0vVmb9XGhqeTtig4weUa4lQ-rCXfDw1t2bztpZ_MTyxZ0AdRT8THJ9NxGl1iVVnmmZMZEaZnAGRfGp8dTI=; osd=Ul8RA0PQl7hfEh-QSdCo5gmTY4FV9LefdDk7sG77s5h4OTS0aUcVTTodG5dFwWdygV1ilGFEbEOXmwmZeWR7fTo=; __snaker__id=dYwBey4J0WjOTTHJ; _zap=3ac25dde-c84d-4d65-bf3b-c9a16dadabfd; d_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"; _xsrf=18c24249-a564-44c0-8f7c-591b1b5f8879; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1709559246,1710670146,1710772602,1710851457; gdxidpyhxdE=86GTGZPw2QP045cXHEhk9N%5CMXGtLsyqXlwhEDPHb4%2BBuCo0fcUBY0TwUzRQyIhZq%5CdUTzIuQxAyJUHrbRIv6ZM28TwK78nicsOvjutrLLXAsBpAEdLVhdnE7orepNxZge6Ike9oGNOBGxNNuKkcrReAI8wetxbxP01eDbfr%2FUG2RcHUh%3A1710854275482; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1710853391; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1710853407|1710851454'
    cookie: 'd_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521";'
}
t9 = RegExp("d_c0=([^;]+)")
er = function () {
    var tt = t9.exec(document.cookie);
    return tt && tt[1]
}
var tA = undefined
var tE = er()
var tb = '101_3_3.0'
//te:url
// var te = '/api/v4/members/d53b74e344eed04badd1167d0fd5fe83?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics'

var te = '/api/v4/comment_v5/questions/616391683/root_comment?order_by=score&limit=20&offset='

var tT = ed(te, tf.body, {
    zse93: tb,
    dc0: tE,
    xZst81: tC
}, tA)

var tO = tT.signature
var xzse = t2 + '_' + tO

console.log(xzse)