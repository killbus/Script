
function getSig3(){

    var sig3 = '123456'
    Java.perform(
        function(){
            var IKSecurityExCls = Java.use("com.kuaishou.android.security.KSecurity");
            sig3 = IKSecurityExCls.atlasSign(str)
            console.log(sig)
        }
    )
}

setTimeout(getSig3)