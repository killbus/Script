
function getSig3(str){

    var sig3 = ''
    Java.perform(
        function(){
            var IKSecurityExCls = Java.use("com.kuaishou.android.security.KSecurity");
            sig3 = IKSecurityExCls.atlasSign(str)
        }
    )
    
    return sig3;
}

rpc.export = {
    getSig3: function(str){
        return getSig3(str);
    }
}