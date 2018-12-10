# coding:utf8
"""
"""
import execjs

js = """
var t = "9mUAW%+CegnrI1s%1+2-9745806.,3";
var e = "g%CA+1gC++m1+Aesg1+CA%s1+snrn1+Cgmm1gsrss1%s+r+1ggCmr1r+grA1r%Am%1r+sng1+emCs1+rrgm1gCeeA1++e%r1rAr++1rA%+C1rAr+e1rA+eA1+mn+%1g%mA+1gCesr1rs%+r1rCCes1rm+Ar1rmsrm1rrmsC1+ge%+1+mg+A";
var decrypt = function(t, e) {
    for (var n = t.split(""), i = e.split(""), a = {}, r = [], o = 0; o < n.length / 2; o++)
        a[n[o]] = n[n.length / 2 + o];
    for (var s = 0; s < e.length; s++)
        r.push(a[i[s]]);
    return r.join("")
};
function test(){
    return decrypt(t, e)
}
"""

ctx = execjs.compile(js)
print(ctx.call("test"))
"""
输出为: 
89427,84771,72538,74293,73060,74811,83633,93767,88416,67862,69219,67308,75143,76681,84552,77596,62677,62974,62675,62752,71079,89127,84536,63976,64453,61726,61361,66134,78597,71872
"""


def decrypt(t, e):
    """待补充"""
    pass


t = "9mUAW%+CegnrI1s%1+2-9745806.,3"
e = "g%CA+1gC++m1+Aesg1+CA%s1+snrn1+Cgmm1gsrss1%s+r+1ggCmr1r+grA1r%Am%1r+sng1+emCs1+rrgm1gCeeA1++e%r1rAr++1rA%+C1rAr+e1rA+eA1+mn+%1g%mA+1gCesr1rs%+r1rCCes1rm+Ar1rmsrm1rrmsC1+ge%+1+mg+A"

print(decrypt(t, e))
