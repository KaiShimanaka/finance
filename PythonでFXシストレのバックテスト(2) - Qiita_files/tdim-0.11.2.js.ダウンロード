(function(n,w,d){
    "use strict";
    var sdk={};
    sdk.version = "0.11.2";
    /* static functions */
    sdk.get_cookies = function(){
        var c=d.cookie.split(";"),r={};
        for(var i=0,len=c.length;i<len;i++){
            c[i] = c[i].replace(/^\s+|\s+$/g, "");
            r[c[i].split("=")[0]] = c[i].split("=")[1];
        }
        return r;
    };
    sdk.set_cookie = function(name,value,days){
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
        d.cookie = name+"="+value+expires+"; path=/";
    };
    sdk.generate_uuid = function(){
        // http://stackoverflow.com/a/8809472
        var d = new Date().getTime();
        var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            var r = (d + Math.random()*16)%16 | 0;
            d = Math.floor(d/16);
            return (c==='x' ? r : (r&0x7|0x8)).toString(16);
        });
        return uuid;
    };
    sdk.get_client_id = function(){
        var uuid = sdk.get_cookies()["_tdim"] || sdk.generate_uuid();
        sdk.set_cookie("_tdim",uuid,365);
        return uuid;
    };
    sdk.base64_encode = function(e){
        // https://gist.github.com/ncerminara/11257943
        var ks = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        e = unescape(encodeURIComponent(e));
        var t = "", n, r, i, s, o, u, a, f = 0;
        while (f < e.length) {
            n = e.charCodeAt(f++);
            r = e.charCodeAt(f++);
            i = e.charCodeAt(f++);
            s = n >> 2;
            o = (n & 3) << 4 | r >> 4;
            u = (r & 15) << 2 | i >> 6;
            a = i & 63;
            if(isNaN(r)){ u = a = 64; }else if(isNaN(i)){ a = 64; }
            t = t + ks.charAt(s) + ks.charAt(o) + ks.charAt(u) + ks.charAt(a);
        }
        return t;
    };
    sdk.stringify = function(obj){
        var str;
        if(w["JSON"] && w["JSON"]["stringify"]){
            str = JSON.stringify(obj);
        }else{
            // http://stackoverflow.com/questions/3326893/is-json-stringify-supported-by-ie-8
            var stringify = function (obj) {
                var t = typeof (obj);
                if (t != "object" || obj === null) {
                    // simple data type
                    if (t == "string") obj = '"'+obj.split('"').join('\\"')+'"';
                        return String(obj);
                }else{
                    // recurse array or object
                    var n, v, json = [], arr = (obj && obj.constructor == Array);
                    for(n in obj){
                            v = obj[n]; t = typeof(v);
                            if (t == "string") v = '"'+v.split('"').join('\\"')+'"';
                            else if (t == "object" && v !== null) v = stringify(v);
                            json.push((arr ? "" : '"' + n + '":') + String(v));
                    }
                    return (arr ? "[" : "{") + String(json) + (arr ? "]" : "}");
                }
            };
            str = stringify(obj);
        }
        return str;
    };
    sdk.create_script_tag = function(url){
        var e = d.createElement("script");
        e.type = "text/javascript";
        e.async = true;
        e.src = url;
        var st = d.getElementsByTagName("script")[0];
        st.parentNode.insertBefore(e,st);
    };
    sdk.fire_gtm_event = function(dl,ev){
        var tmp;
        for(var k in ev){
            if(ev.hasOwnProperty(k)){
                tmp = {}; tmp[k] = ev[k];
                w[dl].push(tmp);
            }
        }
    };

    w[n].callback = w[n]["callback"] || {};
    /* instance functions */
    w[n].prototype.init = function(){
        var defaults = {
            ts: (new Date()).getTime(),
            id: "tij" + (new Date()).getTime() + "" + (1000+Math.floor(9000*Math.random())),
            data: {},
            debug: false,
            imid: undefined,
            sids: [],
            td_host: "in.treasuredata.com",
            td_api_key: undefined,
            td_db: undefined,
            td_tb: "pageviews",
            gtm_dl: undefined,
            gtm_ev_name: "im-ready",
            im_api_token: undefined
        };
        for(var k in defaults){
            if(defaults.hasOwnProperty(k)){
                this[k] = this[k] || defaults[k];
            }
        }
        w[n].callback[this.id] = this;
    };
    w[n].prototype.log = function(str){
        if(this.debug){
            str = "[debug]["+this.id+"]"+str;
            if(w["console"]){
                w.console.log(str);
            }else{
                //alert(str);
            }
        }
    };
    w[n].prototype.td_send_imid = function(td_tb,custom_data){
        this.td_tb = td_tb || this.td_tb;
        custom_data = custom_data || {};
        if(!this.im_api_token){
            this.log("[error] im_api_token not found");
            return;
        }
        for(var k in custom_data){
            if(custom_data.hasOwnProperty(k)){
                this.data[k] = custom_data[k];
            }
        }
        var url = "//sync.im-apps.net/imid/segment?token="+this.im_api_token+"&callback="+encodeURIComponent(n+".callback."+this.id+".im_callback");
        sdk.create_script_tag(url);
        this.log("loading imid,sids");
    };
    w[n].prototype.im_callback = function(res){
        this.log("loaded imid,sids");
        if(res.imid){
            this.imid = res.imid;
            this.data.imid = res.imid;
            this.log("imid:"+this.data.imid);
        }
        if(res.segment_eids){
            this.sids = res.segment_eids;
            this.data.segment_eids = res.segment_eids.join("|");
            this.log("sids:"+this.data.segment_eids);
        }
        if(this.gtm_dl && w[this.gtm_dl]){
            var ev = {
                imid: this.imid,
                segment_eids: this.sids.join("|"),
                event: this.gtm_ev_name
            };
            this.log("fire gtm event");
            sdk.fire_gtm_event(this.gtm_dl,ev);
        }
        this.td_send(this.td_tb,this.data);
    };
    w[n].prototype.td_send = function(td_tb,custom_data){
        this.td_tb = td_tb || this.td_tb;
        custom_data = custom_data || {};
        if(!(this.td_api_key && this.td_db && this.td_tb)){
            this.log("[error] td_api_key,td_db,td_tb are required");
            return;
        }
        var data = this.data;
        for(var k in custom_data){
            if(custom_data.hasOwnProperty(k)){
                data[k] = custom_data[k];
            }
        }
        data.td_client_id = sdk.get_client_id();
        data.td_charset = (d.characterSet || d.charset || '-').toLowerCase();
        data.td_language = (function(){
            var nav = w.navigator;
            return (nav && (nav.language || nav.browserLanguage) || '-').toLowerCase();
        })();
        data.td_color = w.screen ? w.screen.colorDepth + '-bit' : '-';
        data.td_screen = w.screen ? w.screen.width + 'x' + w.screen.height : '-';
        data.td_title = d.title;
        data.td_url = (function(){
            var url = d.location.href;
            var i = url.indexOf('#');
            return -1 === i ? url : url.slice(0, i);
        })();
        data.td_host = d.location.host;
        data.td_path = d.location.pathname;
        data.td_referer = d.referrer;
        data.td_ip = "td_ip";
        data.td_browser = "td_browser";
        data.td_browser_version = "td_browser_version";
        data.td_os = "td_os";
        data.td_os_version = "td_os_version";
        data.td_viewport = "-";
        this.log("sending td");
        var data_str = sdk.stringify(data);
        this.log(data_str);
        var url = "//"+this.td_host+"/js/v3/event/"+this.td_db+"/"+this.td_tb;
        url = url + "?api_key="+encodeURIComponent(this.td_api_key)+"&data="+encodeURIComponent(sdk.base64_encode(data_str));
        url = url + "&modified="+this.ts+"&callback="+encodeURIComponent(n+".callback."+this.id+".td_callback");
        sdk.create_script_tag(url);
    };
    w[n].prototype.td_callback = function(res){
        if(res.created){
            this.log("td send success!");
        }else{
            this.log("td send failed!!");
        }
    };

    (function(){
        var inst,tmp_ar,oid;
        for(var i=0;i<w[n].instances.length;i++){
            inst = w[n].instances[i];
            inst.init();
            for(var j=0,ms=["td_send","td_send_imid"];j<ms.length;j++){
                tmp_ar = "tmp_"+ms[j];
                if(inst[tmp_ar]){
                    for(var k=0;k<inst[tmp_ar].length;k++){
                        inst[ms[j]].apply(inst,inst[tmp_ar][k]);
                    }
                }
            }
        }
    })();
})("TDIM",window,document);

