var _itm_ = function(cvid){
    var g={},w=window,d=document,sc='script',pr=w.location.protocol,st;
    g.cf={"6638": {"gid": "GTM-5SNCW4"}};
    g.cid=6638;
    g.cf=g.cf[g.cid];
    g.ld=function(url){
        var e=d.createElement(sc);
        e.type='text/javascript';e.async = true;e.src=url;
        st=d.getElementsByTagName(sc)[0];
        st.parentNode.insertBefore(e,st);
    };
    g.fo=function(cid,dat){
        w._fout_queue = w._fout_queue || {};
        if(w._fout_queue.segment === void 0) w._fout_queue.segment = {};
        if(w._fout_queue.segment.queue === void 0) w._fout_queue.segment.queue = [];
        var p = {'user_id': cid };
        if(dat){ p.dat = dat; }
        w._fout_queue.segment.queue.push(p);
        g.ld(pr+'//js.fout.jp/segmentation.js');
    };
    g.gt=function(gid, s, dl){
        w[dl] = w[dl] || [];
        w[dl].push({SegmentsString:s});
        w[dl].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
        g.ld(pr+'//www.googletagmanager.com/gtm.js?id='+gid+"&l="+dl);
    };
    g.yt=function(yid){
        g.ld(pr+'//s.yjtag.jp/tag.js#site='+yid);
    };
    g.sa_cb=function(p){
        _itm_.aid = "-";
        _itm_.sids = "";
        if(p.audience_id){
            _itm_.aid = p.audience_id;
            var s = ',';
            p = p.segments;
            for(var i=0,len=p.length;i<len;i++){
                s += p[i].segment_id + ',';
            }
            _itm_.sids = s;
        }
        if(g.cf.gid){ g.gt(g.cf.gid,s,"itm_dl1"); }
        if(g.cf.gid2){ g.gt(g.cf.gid2,s,"itm_dl2"); }
        if(g.cf.yid){ g.yt(g.cf.yid); }
    };
    if(g.cf.fo){ g.fo(g.cid,w._itm_dat_); }
    g.ld(pr+'//cnt.fout.jp/segapi/audience?callback=_itm_.sa_cb&cvid='+cvid);
    return g;
}("mHDmdffSCFxfWgmjsQ");