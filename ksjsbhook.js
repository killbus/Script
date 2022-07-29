function getSig3(str){
    var testStr = "12345678"
    var sig3 = ''
    Java.perform(
        function(){
            var IKSecurityExCls = Java.use("com.kuaishou.android.security.KSecurity");
            sig3 = IKSecurityExCls.atlasSign(testStr)
        }
    )
    console.log("sig3:",sig3)
    console.log("sig3Length:",sig3.length)
    return sig3;
}

setTimeout(getSig3)