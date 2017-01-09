
(function(window, undefined) {

	try {
		var send = function(url){
			var image = new Image();
			image.src = url;
			image.width = 1;
			image.height = 1;
			image.border = 0;
			image.style.display = "none";
			document.body.appendChild(image);
		}

		function addEvent(event, func, target) {
			if (typeof target === "undefined") {
				target = window;
			}
			if (target.addEventListener) {
				target.addEventListener(event, func, false);
			} else if (target.attachEvent) {
				target.attachEvent("on" + event, func);
			} else {
				throw new Error("can not add event");
			}
		}

		addEvent("load", function(){
			var url = location.href;
			var categories = document.getElementsByClassName("tagIcon_name");
			var params = "";
			if (typeof categories !== "undefined") {
				for (var i=0; i<categories.length; i++) {
					if (i != 0) {
						// パラメータを「,」区切りで結合
						params += ",";
					}
					params += categories[i].innerHTML;
				}
			}
			var send_url = "//bigmining.com/dmp";
			var param_text = "?url=" + encodeURIComponent(location.href) + "&rurl=" + encodeURIComponent(document.referrer);

			var qiita_data = {};
			qiita_data.server = document.domain;
			// 各パラメータの設定
			if (params != "") {
				qiita_data.categories = params;
			}
			param_text += "&qiita_data=" + encodeURIComponent(JSON.stringify(qiita_data)).replace(/%20/g, '+');

			send(send_url + param_text + "&action=pv");
			// global変数定義;
			window.dg_tag_data = window.dg_tag_data || {};
			window.dg_tag_data.qiita_search_categories = params;

			var script = document.createElement('script');
			script.innerHTML = "(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-58Z82M');";
			document.body.appendChild(script);

		});

	} catch (e) {
		//console.log(e);
	}

})(window);