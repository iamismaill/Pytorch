<!DOCTYPE html>
<!-- saved from url=(0035)https://captainteemo.tistory.com/15 -->
<html lang="en" class="translated-ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link rel="stylesheet" type="text/css" href="./Linearregression_files/lightbox.min.css"><link rel="stylesheet" type="text/css" href="./Linearregression_files/font.css"><link rel="stylesheet" type="text/css" href="./Linearregression_files/content.css"><!--[if lt IE 9]><script src="https://t1.daumcdn.net/tistory_admin/lib/jquery/jquery-1.12.4.min.js"></script><![endif]--><!--[if gte IE 9]>
<!--><script src="./Linearregression_files/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script><!--<![endif]-->
<script src="./Linearregression_files/lightbox-plus-jquery.min.js"></script>
<script>
lightbox.options.fadeDuration = 200;
lightbox.options.resizeDuration = 200;
lightbox.options.wrapAround = false;
lightbox.options.albumLabel = "%1 / %2";
</script>
<script>var tjQuery = jQuery.noConflict(true);</script><style type="text/css">.tt_article_useless_p_margin p {padding-top:0 !important;padding-bottom:0 !important;margin-top:0 !important;margin-bottom:0 !important;}</style><meta name="referrer" content="always"><link rel="icon" href="https://t1.daumcdn.net/tistory_admin/static/top/favicon_0630.ico"><link rel="apple-touch-icon" href="https://img1.daumcdn.net/thumb/C180x180/?fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F3539841%2Fattach%2Ff858cdedd49440208d1de927ef37da3e">
<link rel="apple-touch-icon" sizes="76x76" href="https://img1.daumcdn.net/thumb/C76x76/?fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F3539841%2Fattach%2Ff858cdedd49440208d1de927ef37da3e">
<link rel="apple-touch-icon" sizes="120x120" href="https://img1.daumcdn.net/thumb/C120x120/?fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F3539841%2Fattach%2Ff858cdedd49440208d1de927ef37da3e">
<link rel="apple-touch-icon" sizes="152x152" href="https://img1.daumcdn.net/thumb/C152x152/?fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F3539841%2Fattach%2Ff858cdedd49440208d1de927ef37da3e">
<meta name="google-adsense-platform-account" content="ca-host-pub-9691043933427338">
<meta name="google-adsense-platform-domain" content="tistory.com">
<meta name="description" content="ref : https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931 TypeError: ‘Tensor’ object is not callable Hello,everyone. Newbie here, trying to learn pytorch. Recently, I’m u..">

<!-- BEGIN OPENGRAPH -->
<link rel="canonical" href="https://captainteemo.tistory.com/15"><meta property="og:type" content="article"><meta property="og:url" content="https://captainteemo.tistory.com/15"><meta property="og:article:author" content="존버맨"><meta property="og:site_name" content="정리하는 블로그"><meta property="og:title" content="[error] TypeError: &#39;Tensor&#39; object is not callable in custom loss"><meta name="by" content="존버맨"><meta property="og:description" content="ref : https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931 TypeError: ‘Tensor’ object is not callable Hello,everyone. Newbie here, trying to learn pytorch. Recently, I’m u.."><meta property="og:image" content="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png">
<!-- END OPENGRAPH -->



<!-- BEGIN TWITTERCARD -->
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@TISTORY"><meta name="twitter:title" content="[error] TypeError: &#39;Tensor&#39; object is not callable in custom loss"><meta name="twitter:description" content="ref : https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931 TypeError: ‘Tensor’ object is not callable Hello,everyone. Newbie here, trying to learn pytorch. Recently, I’m u.."><meta property="twitter:image" content="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png">
<!-- END TWITTERCARD -->



<!-- BEGIN DAUMAPP -->
<meta property="dg:plink" content="https://captainteemo.tistory.com/15"><meta name="plink" content="https://captainteemo.tistory.com/15"><meta name="title" content="[error] TypeError: &#39;Tensor&#39; object is not callable in custom loss"><meta name="article:media_name" content="정리하는 블로그"><meta property="article:mobile_url" content="https://captainteemo.tistory.com/m/15"><meta property="article:pc_url" content="https://captainteemo.tistory.com/15"><meta property="article:mobile_view_url" content="https://captainteemo.tistory.com/m/15"><meta property="article:pc_view_url" content="https://captainteemo.tistory.com/15"><meta property="article:talk_channel_view_url" content="https://captainteemo.tistory.com/m/15"><meta property="article:pc_service_home" content="https://www.tistory.com"><meta property="article:mobile_service_home" content="https://www.tistory.com/m"><meta property="article:txid" content="3539841_15"><meta property="article:published_time" content="2021-05-24T18:27:01+09:00"><meta property="og:regDate" content="20210524182701"><meta property="article:modified_time" content="2021-05-24T18:27:01+09:00">
<!-- END DAUMAPP -->



<!-- BEGIN STRUCTURED_DATA -->
<script type="application/ld+json">{"@context":"http:\/\/schema.org","@type":"BlogPosting","mainEntityOfPage":{"@id":"https:\/\/captainteemo.tistory.com\/15"},"url":"https:\/\/captainteemo.tistory.com\/15","headline":"[error] TypeError: 'Tensor' object is not callable in custom loss","description":"ref : https:\/\/discuss.pytorch.org\/t\/typeerror-tensor-object-is-not-callable\/102931 TypeError: \u2018Tensor\u2019 object is not callable Hello,everyone. Newbie here, trying to learn pytorch. Recently, I\u2019m u..","author":{"@type":"Person","name":"\uc874\ubc84\ub9e8"},"image":{"@type":"ImageObject","url":"https:\/\/t1.daumcdn.net\/tistory_admin\/static\/images\/openGraph\/opengraph.png","width":"800px","height":"800px"},"datePublished":"20210524T18:27:01+09:00","dateModified":"20210524T18:27:01+09:00","publisher":{"@type":"Organization","name":"TISTORY","logo":{"@type":"ImageObject","url":"https:\/\/t1.daumcdn.net\/tistory_admin\/static\/images\/openGraph\/opengraph.png","width":"800px","height":"800px"}}}</script><meta name="robots" content="max-image-preview:large">
<!-- END STRUCTURED_DATA -->


  <title>[error] TypeError: 'Tensor' object is not callable in custom loss</title>
  <meta name="title" content="[error] TypeError: &#39;Tensor&#39; object is not callable in custom loss :: 정리하는 블로그">
  <meta name="description" content="">
  
  <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1, minimum-scale=1.0, maximum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
  <link rel="alternate" type="application/rss+xml" title="blog to organize" href="https://captainteemo.tistory.com/rss">
  <link rel="shortcut icon" href="https://captainteemo.tistory.com/favicon.ico">
  <link rel="stylesheet" href="./Linearregression_files/AvenirLTStd.css">
  <link rel="stylesheet" href="./Linearregression_files/SpoqaHanSans.css">
  <link rel="stylesheet" href="./Linearregression_files/icomoon.css">
  <link rel="stylesheet" href="./Linearregression_files/style.css">
  <link rel="stylesheet" href="./Linearregression_files/slick.css">
  <script src="./Linearregression_files/jquery.js"></script>
  <script src="./Linearregression_files/slick.js"></script>
  <script src="./Linearregression_files/common.js"></script>
  <script src="./Linearregression_files/vh-check.min.js"></script>
  <script>
    (function () {
      // initialize the test
      var test = vhCheck();
    }());
  </script>

<style type="text/css">
		#daumSearchBox {
			height: 21px;
			background-image : url(//i1.daumcdn.net/imgsrc.search/search_all/show/tistory/plugin/bg_search2_2.gif);
			margin: 5px auto ;
			padding: 0;
		}
		#daumSearchBox input {
			background: none;
			margin : 0;
			padding : 0;
			border : 0;
		}
		#daumSearchBox #daumLogo {
			width: 34px;
			height: 21px;
			float: left;
			margin-right: 5px;
			background-image : url(//i1.daumcdn.net/img-media/tistory/img/bg_search1_2_2010ci.gif);
		}
		#daumSearchBox #show_q {
			background-color: transparent;
			border: none;
			font: 12px Gulim, Sans-serif;
			color: #555;
			margin-top: 4px;
			margin-right: 15px;
			float: left;
		}

		#daumSearchBox #show_btn {
			background-image : url(//i1.daumcdn.net/imgsrc.search/search_all/show/tistory/plugin/bt_search_2.gif);
			width: 37px;
			height: 21px;
			float: left;
			margin:0;
			cursor:pointer;
			text-indent:-1000em;
		}
	</style>
<link rel="stylesheet" type="text/css" href="./Linearregression_files/style(1).css">
<script type="text/javascript" src="./Linearregression_files/profile.js"></script>
	<style type="text/css">
		.another_category { border: 1px solid #E5E5E5; padding: 10px 10px 5px; margin:10px 0; clear: both; }
		.another_category h4 { font-size: 12px !important; margin: 0 !important; border-bottom: 1px solid #E5E5E5 !important; padding: 2px 0 6px !important; }
		.another_category h4 a { font-weight: bold !important; }
		.another_category table { table-layout: fixed; border-collapse: collapse; width: 100% !important; margin-top: 10px !important; }
		* html .another_category table { width: auto !important; }
		*:first-child+html .another_category table { width: auto !important; }
		.another_category th, .another_category td { padding: 0 0 4px !important; }
		.another_category th { text-align: left; font-size: 12px !important; font-weight: normal;  word-break: break-all; overflow: hidden; line-height: 1.5; }
		.another_category td { text-align: right; width: 80px; font-size: 11px; }
		.another_category th a { font-weight: normal; text-decoration: none; border: none !important; }
		.another_category th a.current{ font-weight: bold; text-decoration: none !important; border-bottom: 1px solid !important; }
		.another_category th span { font-weight: normal; text-decoration: none; font: 10px Tahoma, Sans-serif; border: none !important; }

		.another_category_color_gray, .another_category_color_gray h4 { border-color: #E5E5E5 !important; }
		.another_category_color_gray * { color: #909090 !important; }
		.another_category_color_gray th a.current{border-color:#909090 !important;}
		.another_category_color_gray h4, .another_category_color_gray h4 a { color: #737373 !important; }


		.another_category_color_red, .another_category_color_red h4 { border-color: #F6D4D3 !important;  }
		.another_category_color_red * { color: #E86869 !important; }
		.another_category_color_red th a.current{border-color:#E86869 !important;}
		.another_category_color_red h4, .another_category_color_red h4 a { color: #ED0908 !important; }


		.another_category_color_green, .another_category_color_green h4 { border-color: #CCE7C8 !important; }
		.another_category_color_green * { color: #64C05B !important; }
		.another_category_color_green th a.current{border-color:#64C05B !important;}
		.another_category_color_green h4, .another_category_color_green h4 a { color: #3EA731 !important; }


		.another_category_color_blue, .another_category_color_blue h4 { border-color: #C8DAF2 !important; }
		.another_category_color_blue * { color: #477FD6 !important; }
		.another_category_color_blue th a.current{border-color:#477FD6 !important;}
		.another_category_color_blue h4, .another_category_color_blue h4 a { color: #1960CA !important; }


		.another_category_color_violet, .another_category_color_violet h4 { border-color: #E1CEEC !important;  }
		.another_category_color_violet * { color:#9D64C5 !important; }
		.another_category_color_violet th a.current{border-color:#9D64C5 !important;}
		.another_category_color_violet h4, .another_category_color_violet h4 a { color: #7E2CB5 !important; }
	</style>
<script type="text/javascript">
        
        window.TistoryBlog = {
            basePath: "",
            url: "https://captainteemo.tistory.com",
            tistoryUrl: "https://captainteemo.tistory.com",
			manageUrl: 'https://captainteemo.tistory.com/manage',
            token: '+itbthsK2ybsAulVGxpxBQ=='
        };
        var servicePath = "";
        var blogURL = "";
    </script>

	<script> (function() { window.orgjQuery = window.jQuery; window.jQuery = tjQuery })()</script>
    <script type="text/javascript" defer="" src="./Linearregression_files/reaction-button-container.min.js"></script>
    <script> (function() { window.jQuery = window.orgjQuery; delete window.orgjQuery })()</script>
        <script type="text/javascript" src="./Linearregression_files/base.js"></script>
        <link rel="stylesheet" type="text/css" href="./Linearregression_files/dialog.css">
            <link rel="stylesheet" type="text/css" href="./Linearregression_files/font(1).css">
    <link rel="stylesheet" type="text/css" href="./Linearregression_files/postBtn.css">
        <link rel="stylesheet" type="text/css" href="./Linearregression_files/tistory.css">
        <script type="text/javascript" src="./Linearregression_files/kakao.min.js"></script><style type="text/css">#DragSchLayer{display:block;position:absolute;z-index:1000;width:61px;height:31px;margin:-30px 0px 0px -5px;background:url(//search1.daumcdn.net/search/statics/common/pi/btn_drag_rect.png);cursor:pointer}             @media             only screen and (-webkit-min-device-pixel-ratio: 1.5),             only screen and (min-device-pixel-ratio: 1.5),             only screen and (min-resolution: 1.5dppx) {             #DragSchLayer{background-image:url(//search1.daumcdn.net/search/statics/common/pi/r2/btn_drag_rect.png);background-size:61px 31px}}            </style><link type="text/css" rel="stylesheet" charset="UTF-8" href="./Linearregression_files/translateelement.css"></head>

<body id="tt-body-page" class="theme_pink">
  <script type="text/javascript">
	(function() {
		if (!window.T) {
			window.T = {}
		}
		window.T.config = {"TOP_SSL_URL":"https:\/\/www.tistory.com","PREVIEW":false,"ROLE":"guest","PREV_PAGE":"\/16","NEXT_PAGE":"\/14","BLOG":{"isDormancy":false,"title":"\uc815\ub9ac\ud558\ub294 \ube14\ub85c\uadf8"},"NEED_COMMENT_LOGIN":false,"COMMENT_LOGIN_CONFIRM_MESSAGE":"","LOGIN_URL":"https:\/\/www.tistory.com\/auth\/login\/?redirectUrl=http%3A%2F%2Fcaptainteemo.tistory.com%2F15","DEFAULT_URL":"https:\/\/captainteemo.tistory.com","USER":{"name":null,"homepage":null},"ROLE_GROUP":"visitor","SUBSCRIPTION":{"status":"none","isConnected":false,"isProcessing":false,"isPending":false,"isWait":false,"isNone":true},"IS_LOGIN":false,"HAS_BLOG":false,"TOP_URL":"https:\/\/www.tistory.com","JOIN_URL":"https:\/\/www.tistory.com\/member\/join"};
		window.appInfo = {"domain":"tistory.com","topUrl":"https:\/\/www.tistory.com","loginUrl":"https:\/\/www.tistory.com\/auth\/login","logoutUrl":"https:\/\/www.tistory.com\/auth\/logout"};

        window.initData = {};
        
	})();
</script>

<script type="text/javascript" src="./Linearregression_files/common(1).js"></script>
<div style="margin:0; padding:0; border:none; background:none; float:none; clear:none; z-index:0"></div>
    <!-- warp / 테마 변경시 theme_pink / theme_blue / theme_green / theme_gray-->
    <div id="wrap" class="white">

      
      <!-- box_header -->
      <header class="box_header">
        <h1 class="title_logo">
          <a href="https://captainteemo.tistory.com/" title="blog to organize" class="link_logo"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            
              blog to organize
            
          </font></font></a>
        </h1>

        <!-- <h1 class="title_logo" style="background-image:url('https://tistory3.daumcdn.net/tistory/0/xf_Portfolio/images/logo.jpg')"></h1> -->
        <button class="btn_search"></button>

        <!-- 메뉴 및 검색 버튼 클릭시 area_sidebar / area_popup 논처리 삭제 / body 에 style="overflow:hidden" 추가 -->
        <button type="button" class="btn_menu" title="menu"><span class="blind"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">menu</font></font></span></button>
      </header>
      <!-- // box_header -->

      <!-- container -->
      <div id="container">

        <!-- area_sidebar -->
        <aside class="area_sidebar thema_apply" style="display: none;">

          <div class="inner_sidebar">
            <div class="sidebar_header">
              <h1 class="title_logo">
                <a href="https://captainteemo.tistory.com/" title="정리하는 블로그" class="link_logo"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                  
                  
                    blog to organize
                  
                </font></font></a>
              </h1>
              <button type="button" class="btn_close" title="닫기"><span class="icon-Close"></span></button>
            </div>

            <div class="sidebar_contents">
              <div class="sidebar_menu">
                
                    <div class="sidebar_left">
                      <!-- 카테고리 메뉴 -->
                      <div class="box_gnb">
                        <nav>
                          <ul class="tt_category">
	<li class="">
		<a class="link_tit" href="https://captainteemo.tistory.com/category"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
			View all categories							 </font></font><span class="c_cnt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">(24)</font></font></span>
			
					</a>

				<ul class="category_list">
							<li class="">
					<a class="link_item" href="https://captainteemo.tistory.com/category/%EA%B5%AC%EB%A7%A4%ED%95%9C%20%EA%B2%83%20%20%EC%A0%95%EB%A6%AC"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
						Purchases													 </font></font><span class="c_cnt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">(0)</font></font></span>
						
											</a>

					
				</li>
							<li class="">
					<a class="link_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
						Organize what you have studied													 </font></font><span class="c_cnt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">(13)</font></font></span>
						
											</a>

										<ul class="sub_category_list">
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B0%80%EA%B3%B5">
									데이터 가공
																			<span class="c_cnt">(2)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EC%9D%BD%EC%96%B4%EB%B3%B4%EC%9E%90%20%EB%85%BC%EB%AC%B8">
									읽어보자 논문
																			<span class="c_cnt">(0)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91%EC%A4%80%EB%B9%84">
									기술면접준비
																			<span class="c_cnt">(0)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95">
									개발환경설정
																			<span class="c_cnt">(9)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%AC">
									자연어처리
																			<span class="c_cnt">(0)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/CV">
									CV
																			<span class="c_cnt">(0)</span>
									
																	</a>
							</li>
													<li class="">
								<a class="link_sub_item" href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EC%8B%9C%EA%B3%84%EC%97%B4%EC%B2%98%EB%A6%AC">
									시계열처리
																			<span class="c_cnt">(0)</span>
									
																	</a>
							</li>
											</ul>
					
				</li>
							<li class="">
					<a class="link_item" href="https://captainteemo.tistory.com/category/%EC%82%B4%EB%A9%B4%EC%84%9C%20%EA%B0%80%EB%81%94%20%ED%95%84%EC%9A%94%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC">
						살면서 가끔 필요한 것 정리													<span class="c_cnt">(5)</span>
						
											</a>

					
				</li>
							<li class="">
					<a class="link_item" href="https://captainteemo.tistory.com/category/%EA%B2%BD%ED%97%98%2C%20%EC%8B%9C%ED%97%98%2C%20%ED%9B%84%EA%B8%B0">
						경험, 시험, 후기													<span class="c_cnt">(6)</span>
						
											</a>

					
				</li>
					</ul>
			</li>
</ul>
                        </nav>
                      </div>
                  
                    <!-- 메인 메뉴 -->
                    <div class="box_gnb">
                      <ul>		<li class="t_menu_home first">
			<a href="https://captainteemo.tistory.com/">홈</a>
		</li>
		</ul>
                    </div>
              </div>
              
                <div class="sidebar_right">
                  <!-- 링크 -->
                  <div class="box_sns">
                    <ul class="list_sns">
                      
                    </ul>
                  </div>
              
                <!-- RSS 피드 -->
                <div class="add_link">
                  <a href="https://captainteemo.tistory.com/rss" target="_blank" class="link_add">RSS 피드</a>
                </div>
            </div>
            
          </div>

          <!-- 관리 -->
          <div class="box_tool">
            <div class="btn-for-guest" style="display: block;">
              <a href="https://captainteemo.tistory.com/15#" class="link_tool" data-action="login">로그인</a>
            </div>
            <div class="btn-for-user">
              <a href="https://captainteemo.tistory.com/15#" class="link_tool" data-action="logout">로그아웃</a>
              <a href="https://captainteemo.tistory.com/manage/entry/post" class="link_tool">글쓰기</a>
              <a href="https://captainteemo.tistory.com/manage" class="link_tool">관리</a>
            </div>
          </div>
      </div>
    </div>

    <div class="dimmed_sidebar"></div>
    </aside>

    <!-- // area_sidebar -->

    <!-- area_popup -->
    <div class="area_popup" style="display: none;">
      <div class="area_search thema_apply">
        <div class="search_header">
          <h1 class="title_logo">
            <a href="https://captainteemo.tistory.com/" title="정리하는 블로그" class="link_logo">
              
              
                정리하는 블로그
              
            </a>
          </h1>
          <button type="button" class="btn_close" title="닫기"><span class="icon-Close"></span></button>
        </div>

        <div class="search_content">
          <form action="https://captainteemo.tistory.com/15" method="get">
            <legend><span class="blind">컨텐츠 검색</span></legend>
            <div class="box_form">
              <span class="icon-Search"></span>
              
                <input type="text" name="search" title="검색어 입력" placeholder="SEARCH" value="" class="inp_search" onkeypress="if (event.keyCode == 13) { try{window.location.href=&#39;/search/&#39;+looseURIEncode(document.getElementsByName(&#39;search&#39;)[0].value);document.getElementsByName(&#39;search&#39;)[0].value=&#39;&#39;;return false;}catch(e){} }">
              
              <button type="button" title="검색어 삭제" class="btn_search_del">
                <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 0 36 36" class="img_svg">
                  <defs>
                    <path id="textDelBtnSvg" d="M20 2C10.059 2 2 10.059 2 20s8.059 18 18 18 18-8.059 18-18S29.941 2 20 2zm8 24.6L26.6 28 20 21.4 13.4 28 12 26.6l6.6-6.6-6.6-6.6 1.4-1.4 6.6 6.6 6.6-6.6 1.4 1.4-6.6 6.6 6.6 6.6z"></path>
                  </defs>
                  <g fill="none" fill-rule="evenodd" transform="translate(-2 -2)">
                    <path d="M0 0h40v40H0z"></path>
                    <mask id="textDelBtnSvgMask" fill="#fff">
                      <use xlink:href="#textDelBtnSvg"></use>
                    </mask>
                    <g fill="#000" fill-opacity="1" mask="url(#textDelBtnSvgMask)" class="svg_bg">
                      <path d="M0 0h40v40H0z"></path>
                    </g>
                  </g>
                </svg>
              </button>
            </div>
          </form>

          
              <!-- 태그 -->
              <div class="tag_zone">
                <h3 class="title_sidebar">태그</h3>
                <div class="box_tag">
                  <a href="https://captainteemo.tistory.com/tag/.to%28device%29%20%EB%AC%B4%ED%95%9C%EB%A1%9C%EB%94%A9" class="cloud5"> .to(device) 무한로딩</a><a href="https://captainteemo.tistory.com/tag/mysql%20%EC%97%B0%EC%8A%B5%20%EC%82%AC%EC%9D%B4%ED%8A%B8" class="cloud5"> mysql 연습 사이트</a><a href="https://captainteemo.tistory.com/tag/%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%20%EC%84%A4%EC%A0%95%EC%98%A4%EB%A5%98" class="cloud5"> 환경변수 설정오류</a><a href="https://captainteemo.tistory.com/tag/boj%202579%20python" class="cloud5"> boj 2579 python</a><a href="https://captainteemo.tistory.com/tag/%ED%86%A0%EC%9D%B5%EC%8A%A4%ED%94%BC%ED%82%B9%20%EB%8B%A8%EA%B8%B0%EC%99%84%EC%84%B1" class="cloud5"> 토익스피킹 단기완성</a><a href="https://captainteemo.tistory.com/tag/LINK%20%3A%20fatal%20error%20LNK1181%3A%20%27C%3A%5CProgram.obj%27%20%EC%9E%85%EB%A0%A5%20%ED%8C%8C%EC%9D%BC%EC%9D%84%20%EC%97%B4%20%EC%88%98%20%EC%97%86%EC%8A%B5%EB%8B%88%EB%8B%A4" class="cloud5"> LINK : fatal error LNK1181: 'C:\Program.obj' 입력 파일을 열 수 없습니다</a><a href="https://captainteemo.tistory.com/tag/.to%28%29%20%EC%98%A4%EB%A5%98" class="cloud5"> .to() 오류</a><a href="https://captainteemo.tistory.com/tag/%ED%8C%8C%EC%9D%B4%ED%86%A0%EC%B9%98%20.to%28%29%20%EC%98%A4%EB%A5%98" class="cloud5"> 파이토치 .to() 오류</a><a href="https://captainteemo.tistory.com/tag/sql%20%EC%BD%94%ED%85%8C%20%EB%8C%80%EB%B9%84" class="cloud5"> sql 코테 대비</a><a href="https://captainteemo.tistory.com/tag/%EC%BD%94%ED%85%8C%20sql%EB%8C%80%EB%B9%84" class="cloud5"> 코테 sql대비</a><a href="https://captainteemo.tistory.com/tag/%ED%86%A0%EC%8A%A4%20%ED%9B%84%EA%B8%B0" class="cloud5"> 토스 후기</a><a href="https://captainteemo.tistory.com/tag/.to%28gpu%29%20%EC%98%A4%EB%A5%98" class="cloud5"> .to(gpu) 오류</a><a href="https://captainteemo.tistory.com/tag/boj%202579" class="cloud5"> boj 2579</a><a href="https://captainteemo.tistory.com/tag/%ED%86%A0%EC%9D%B5%EC%8A%A4%ED%94%BC%ED%82%B9%20%EB%B2%BC%EB%9D%BD%EC%B9%98%EA%B8%B0" class="cloud5"> 토익스피킹 벼락치기</a><a href="https://captainteemo.tistory.com/tag/sql%20%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C" class="cloud5"> sql 문제모음</a><a href="https://captainteemo.tistory.com/tag/%EB%B0%B1%EC%A4%80%202579%20%ED%8C%8C%EC%9D%B4%EC%8D%AC" class="cloud5"> 백준 2579 파이썬</a><a href="https://captainteemo.tistory.com/tag/sql%EB%AC%B8%EC%A0%9C%20%EC%82%AC%EC%9D%B4%ED%8A%B8" class="cloud5"> sql문제 사이트</a><a href="https://captainteemo.tistory.com/tag/%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EB%9D%84%EC%96%B4%EC%93%B0%EA%B8%B0" class="cloud5"> 환경변수띄어쓰기</a><a href="https://captainteemo.tistory.com/tag/2579%20python" class="cloud5"> 2579 python</a><a href="https://captainteemo.tistory.com/tag/%ED%86%A0%EC%9D%B5%EC%8A%A4%ED%94%BC%ED%82%B9%20%ED%9B%84%EA%B8%B0" class="cloud5"> 토익스피킹 후기</a>
                </div>
              </div>
            
              <!-- 최근글 -->
              <div class="tag_board">
                <h3 class="title_sidebar">최근글</h3>
                <ul class="list_sidebar">
                  
                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/32"> 토익스피킹 2일 lev6 150점⋯</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/31"> [boj] 2579 계단 오르기 python</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/30"> [mySQL] 코테 대비 SQL 연습⋯</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/29"> [mySQL] 프로그래머스 고양이⋯</a></li>
                  
                </ul>
              </div>
            
              <!-- 최근 댓글 -->
              <div class="tag_board">
                <h3 class="title_sidebar">댓글</h3>
                <ul class="list_sidebar">
                  
                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/8#comment13068804">이제봤네요ㅠㅠ 제기억엔 룸메이트 신청⋯</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/8#comment13011454">이번에 3기 지원해보려고 하는데 조 편⋯</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/8#comment12672396">수학적인 부분보다는 이론부분이 더 많⋯</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/8#comment12656737">안녕하세요 2기 프리코스중인 사람입니⋯</a></li>
                  
                </ul>
              </div>
            
              <!-- 공지사항 -->
              
                <div class="tag_board">
                  <h3 class="title_sidebar">공지사항</h3>
                  <ul class="list_sidebar">
                    
                  </ul>
                </div>
              
            
              <!-- 글 보관함 -->
              <div class="tag_board">
                <h3 class="title_sidebar">아카이브</h3>
                <ul class="list_sidebar">
                  
                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/archive/202204">2022/04</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/archive/202202">2022/02</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/archive/202201">2022/01</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/archive/202112">2021/12</a></li>
                  

                    <li class="item_sidebar"><a href="https://captainteemo.tistory.com/archive/202111">2021/11</a></li>
                  
                </ul>
              </div>
            
        </div>

      </div>
    </div>
    <!-- // area_popup -->

    <main id="main">
      <!-- area_cover -->
      
      <!-- // area_cover -->

      

      <!-- area_view -->
      <div class="area_view">
        

          

            <!-- article_content -->
            <div class="area_article">

              <!-- 뷰페이지 상단 type css 구분 / type_article_header_common or type_article_header_cover -->
              <div class="article_header type_article_header_cover">
                <div class="inner_header">
                  <div class="info_text">
                    <strong class="title_post"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[error] TypeError: 'Tensor' object is not callable in custom loss</font></font></strong>
                    <p class="info"><span class="date"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2021. 5. 24. 18:27</font></font></span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> ㆍ Organize </font></font><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">what you have studied/Set up the development environment</font></font></span></p>
                  </div>
                </div>
              </div>

              <!-- 에디터 영역 -->
              <div class="article_view">
                <div class="tt_article_useless_p_margin contents_style"><p data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ref:</font></font><a href="https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931" target="_blank" rel="noopener"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931</font></font></a></p>
<figure id="og_1621848276682" contenteditable="false" data-ke-type="opengraph" data-ke-align="alignCenter" data-og-type="website" data-og-title="TypeError: ‘Tensor’ object is not callable" data-og-description="Hello,everyone. Newbie here, trying to learn pytorch. Recently, I’m using lstm or gru to do failure prediction. This is a binary classification problem ,so I use BCEWithLogitsLoss as the loss function, but finally, it is wrong. %matplotlib notebook impor" data-og-host="discuss.pytorch.org" data-og-source-url="https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931" data-og-url="https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931" data-og-image="https://scrap.kakaocdn.net/dn/F02bm/hyKjHBnxXn/uMbkCfJhVewtiOeSgJtN8k/img.png?width=512&amp;height=512&amp;face=0_0_512_512,https://scrap.kakaocdn.net/dn/tEtNb/hyKjMQcMes/oWRrfXex6HLS0h3W78ocjk/img.png?width=512&amp;height=512&amp;face=0_0_512_512,https://scrap.kakaocdn.net/dn/UJw6Y/hyKjHg3DY5/yeunBb8oe7waRu406k7Wak/img.png?width=1025&amp;height=205&amp;face=0_0_1025_205"><a href="https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931" target="_blank" rel="noopener" data-source-url="https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931">
<div class="og-image" style="background-image: url(&#39;https://scrap.kakaocdn.net/dn/F02bm/hyKjHBnxXn/uMbkCfJhVewtiOeSgJtN8k/img.png?width=512&amp;height=512&amp;face=0_0_512_512,https://scrap.kakaocdn.net/dn/tEtNb/hyKjMQcMes/oWRrfXex6HLS0h3W78ocjk/img.png?width=512&amp;height=512&amp;face=0_0_512_512,https://scrap.kakaocdn.net/dn/UJw6Y/hyKjHg3DY5/yeunBb8oe7waRu406k7Wak/img.png?width=1025&amp;height=205&amp;face=0_0_1025_205&#39;);">&nbsp;</div>
<div class="og-text">
<p class="og-title" data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">TypeError: 'Tensor' object is not callable</font></font></p>
<p class="og-desc" data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Hello, everyone. </font><font style="vertical-align: inherit;">Newbie here, trying to learn pytorch. </font><font style="vertical-align: inherit;">Recently, I'm using lstm or gru to do failure prediction. </font><font style="vertical-align: inherit;">This is a binary classification problem ,so I use BCEWithLogitsLoss as the loss function, but finally, it is wrong. </font><font style="vertical-align: inherit;">%matplotlib notebook import</font></font></p>
<p class="og-host" data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">discuss.pytorch.org</font></font></p>
</div>
</a></figure>
<p data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">I create and use a custom loss, but a </font></font><span style="background-color: #f8f8f8; color: #ff0000;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">TypeError: 'Tensor' object is not callable</font></font></span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> occurs</font></font></p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Cause: Occurs because the name of the loss function and the name of the returned argument value are the same.</font></font></p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">loss = loss(pred, ground_truth ) must not be done because the name must not be the same</font></font></p>
<p data-ke-size="size16"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">loss = custom_loss(pred, ground_truth )</font></font></p><div class="container_postbtn #post_button_group">
    <div class="postbtn_like">
        
<script>
    window.ReactionButtonType = 'reaction';
    window.ReactionApiUrl = '//captainteemo.tistory.com/reaction';
    window.ReactionReqBody = {
        entryId: 15    }
</script>
<div class="wrap_btn" id="reaction-15"><button class="btn_post uoc-icon"><div class="uoc-icon"><span class="ico_postbtn ico_like"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">like</font></font></span><span class="txt_like uoc-count"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sympathy</font></font></span></div></button></div>
<script src="./Linearregression_files/reaction-button-container.min.js"></script>
        <div class="wrap_btn wrap_btn_share">
    <button type="button" class="btn_post sns_btn btn_share" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="[error] TypeError: &#39;Tensor&#39; object is not callable in custom loss" data-description="ref : https://discuss.pytorch.org/t/typeerror-tensor-object-is-not-callable/102931 TypeError: ‘Tensor’ object is not callable Hello,everyone. Newbie here, trying to learn pytorch. Recently, I’m u.." data-profile-image="https://tistory3.daumcdn.net/tistory/3539841/attach/f858cdedd49440208d1de927ef37da3e" data-profile-name="존버맨" data-pc-url="https://captainteemo.tistory.com/15" data-relative-pc-url="/15" data-blog-title="정리하는 블로그">
        <span class="ico_postbtn ico_share"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">share</font></font></span>
    </button>
</div>
                <div class="wrap_btn wrap_btn_etc" data-entry-id="15" data-entry-visibility="public" data-category-visibility="public">
    <button type="button" class="btn_post btn_etc2"><span class="ico_postbtn ico_etc"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">text element</font></font></span></button>
</div>
    </div>
    <button type="button" class="btn_menu_toolbar btn_subscription  #subscribe" data-blog-id="3539841" data-url="https://captainteemo.tistory.com/15" data-device="web_pc">
    <em class="txt_state"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Subscribe</font></font></em>
    <strong class="txt_tool_id">정리하는 블로그</strong>
    <span class="img_common_tistory ico_check_type1"></span>
</button>
    <div class="postbtn_ccl" data-ccl-type="">
    <a href="https://creativecommons.org/licenses//4.0/deed.ko" target="_blank" class="link_ccl" rel="license">
        <span class="bundle_ccl">
                    </span>
    </a>
</div>
    <!--
<rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <Work rdf:about="">
        <license rdf:resource="http://creativecommons.org/licenses/by-/2.0/kr/" />
    </Work>
    <License rdf:about="http://creativecommons.org/licenses/by-/">
        <permits rdf:resource="http://web.resource.org/cc/Reproduction"/>
        <permits rdf:resource="http://web.resource.org/cc/Distribution"/>
        <requires rdf:resource="http://web.resource.org/cc/Notice"/>
        <requires rdf:resource="http://web.resource.org/cc/Attribution"/>
                    </License>
</rdf:RDF>
-->
</div><div class="another_category another_category_color_gray">
<h4>'<a href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC">공부한 것 정리</a>&nbsp;&gt;&nbsp;<a href="https://captainteemo.tistory.com/category/%EA%B3%B5%EB%B6%80%ED%95%9C%20%EA%B2%83%20%EC%A0%95%EB%A6%AC/%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95">개발환경설정</a>' 카테고리의 다른 글</h4>
<div class="table-overflow"><table>
<tbody><tr>
<th>
<a href="https://captainteemo.tistory.com/24?category=1202962">[Error] cv2.error: OpenCV(4.5.3) C:\Users\runneradmin\AppData\Local\Temp\pip-req-build-z4706ql7\opencv\modules\highgui\src\window.cpp:1274: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Coco..</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.11.24</td>
</tr>
<tr>
<th>
<a href="https://captainteemo.tistory.com/23?category=1202962">[Error] RuntimeError: CUDA error: no kernel image is available for execution on the deviceCUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.10.18</td>
</tr>
<tr>
<th>
<a href="https://captainteemo.tistory.com/22?category=1202962">우분투 듀얼부팅과 기본환경설정 / / dev/nvme0n1p3 : clean, xxx/xxx files, xxx/xxx blocks 오류 // 설치 후 검은 화면 오류</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.09.03</td>
</tr>
<tr>
<th>
<a href="https://captainteemo.tistory.com/16?category=1202962">Error handling</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.05.31</td>
</tr>
<tr>
<th>
<a href="https://captainteemo.tistory.com/15?category=1202962" class="current">[error] TypeError: 'Tensor' object is not callable in custom loss</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.05.24</td>
</tr>
<tr>
<th>
<a href="https://captainteemo.tistory.com/14?category=1202962">FLOPS란</a>&nbsp;&nbsp;<span>(0)</span>
</th>
<td>
2021.05.23</td>
</tr>
</tbody></table></div></div></div>
              </div>

              <!-- article_content -->
              <div class="article_content">
                <!-- <ul class="list_share list_sns">
                                        <li class="item_share"><a href="#" class="link_share link_facebook" data-service="facebook"><span class="icon-Facebook"></span><span class="blind">페이스북</span></a></li>
                                        <li class="item_share"><a href="#" class="link_share link_twitter" data-service="twitter"><span class="icon-Twitter"></span><span class="blind">트위터</span></a></li>
                                        <li class="item_share"><a href="#" class="link_share link_story" data-service="kakaostory"><span class="icon-Story"></span><span class="blind">카카오스토리</span></a></li>
                                        <li class="item_share"><a href="#" class="link_share link_kakao" data-service="kakaotalk"><span class="icon-Kakao"></span><span class="blind">카카오톡</span></a></li>
                                    </ul> -->

                

                
                  <!-- area_related -->
                  <div class="area_related">
                    <h3 class="title_related"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Related articles</font></font></h3>
                    <ul class="list_related">
                      
                        <li class="item_related">
                          <a href="https://captainteemo.tistory.com/23?category=1202962" class="link_related">
                            <span class="thumnail item-thumbnail" style="background-image:url(&#39;&#39;)"></span>
                            <div class="box_content">
                              <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[Error] RuntimeError: CUDA error: no kernel image is available for execution on the deviceCUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.</font></font></strong>
                              <span class="info"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2021.10.18</font></font></span>
                            </div>
                          </a>
                        </li>
                      
                        <li class="item_related">
                          <a href="https://captainteemo.tistory.com/22?category=1202962" class="link_related">
                            <span class="thumnail item-thumbnail" style="background-image:url(&#39;https://blog.kakaocdn.net/dn/FdRSp/btrdSdGtdol/7wltWHqdUgbUsyZd3fCh6k/img.jpg&#39;)"></span>
                            <div class="box_content">
                              <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ubuntu dual boot and basic configuration // dev/nvme0n1p3 : clean, xxx/xxx files, xxx/xxx blocks error // black screen error after installation</font></font></strong>
                              <span class="info"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2021.09.03</font></font></span>
                            </div>
                          </a>
                        </li>
                      
                        <li class="item_related">
                          <a href="https://captainteemo.tistory.com/16?category=1202962" class="link_related">
                            <span class="thumnail item-thumbnail" style="background-image:url(&#39;&#39;)"></span>
                            <div class="box_content">
                              <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Error handling</font></font></strong>
                              <span class="info"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2021.05.31</font></font></span>
                            </div>
                          </a>
                        </li>
                      
                        <li class="item_related">
                          <a href="https://captainteemo.tistory.com/14?category=1202962" class="link_related">
                            <span class="thumnail item-thumbnail" style="background-image:url(&#39;&#39;)"></span>
                            <div class="box_content">
                              <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What is FLOPS?</font></font></strong>
                              <span class="info"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2021.05.23</font></font></span>
                            </div>
                          </a>
                        </li>
                      
                    </ul>
                  </div>
                  <!-- // area_related -->
                

                <!-- area_reply -->
                <div class="area_reply">

                  <div class="box_reply_info">
                    <a href="https://captainteemo.tistory.com/15#rp" onclick="" class="reply_events"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">comment</font></font><span></span></a>
                  </div>

                  <!-- reply_content -->
                  <div class="reply_content">
                    <button type="button" class="btn_more btn_replymore" style="display:none;">+ 이전 댓글 더보기</button>

                    <div id="entry15Comment">
                      <!-- box_comment_list -->
                      <div class="box_comment_list">
                        
                      </div>
                      <!-- // box_comment_list -->

                      <form method="post" action="https://captainteemo.tistory.com/comment/add/15" onsubmit="return false" style="margin: 0">
                        <!-- reply_write -->
                        
                          <div class="reply_write">
                            
                              
                                <div class="form_guest">
                                  <!-- name -->
                                  <div class="box_inp">
                                    <div class="inner_inp">
                                      <input type="text" name="name" value="" title="name" placeholder="name" class="inp_comment inp_name">
                                    </div>
                                  </div>
                                  <!-- password -->
                                  <div class="box_inp">
                                    <div class="inner_inp">
                                      <input type="password" name="password" value="" title="password" maxlength="12" placeholder="password" class="inp_comment inp_password">
                                    </div>
                                  </div>
                                </div>
                              
                            
                            <div class="form_content">
                              <textarea id="comment" name="comment" placeholder="Please enter a comment."></textarea>
                            </div>

                            <div class="form_reg thema_apply">
                              <label><input type="checkbox" name=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Private</font></font></label>
                              <button type="button" class="btn_register" onclick="addComment(this, 15); return false;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Leave a comment</font></font></button>
                            </div>

                          </div>
                        </form>
                        <!-- // reply_write -->
                      
                    </div><script type="text/javascript">loadedComments[15]=true;findFragmentAndHighlight(15)</script>

                  </div>
                  <!-- // reply_content -->

                </div>
                <!-- // area_reply -->
              </div>
              <!-- // article_content -->

            </div>
            <!-- article_content -->


          
        
      </div>
      <!-- // area_view -->

      

      

      

      

      

      

      
        <!-- area_paging -->
        <div class="area_paging">
          <a href="https://captainteemo.tistory.com/16" class="link_page link_prev "><span class="icon-Keyboard-Arrow---Left"></span></a>
          <div class="paging_num thema_apply">
            
              <a href="https://captainteemo.tistory.com/32" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">One</font></font></span></a>
            
              <a class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">...</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/21" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">12</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/18" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">13</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/17" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">14</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/16" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">15</font></font></span></a>
            
              <a class="link_num"><span class="selected"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">16</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/14" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">17</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/11" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">18</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/10" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">19</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/9" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">20</font></font></span></a>
            
              <a class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">...</font></font></span></a>
            
              <a href="https://captainteemo.tistory.com/4" class="link_num"><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">24</font></font></span></a>
            
          </div>
          <a href="https://captainteemo.tistory.com/14" class="link_page link_next "><span class="icon-Keyboard-Arrow---Right"></span></a>
        </div>
        <!-- // area_paging -->
      
    </main>

    </div>
    <!-- // container -->

    

    <!-- footer -->
    <footer id="footer">
      <div class="inner_footer">
        
          <a href="https://www.tistory.com/" class="link_footer"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">tea story</font></font></a>
        
        
        
        
      </div>
      <div>
        <address><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">© 2018 TISTORY. </font><font style="vertical-align: inherit;">All rights reserved.</font></font></address>
      </div>

    </footer>
    <!-- // footer -->

    </div>
    <!-- // wrap -->
  
<script src="./Linearregression_files/search_dragselection.min.js"></script>

	<script>
	    lightbox.option({
			"fadeDuration": 200,
		    "resizeDuration": 200,
		    "wrapAround": false,
			"albumLabel": "%1 / %2",
			"fitImagesInViewport":true ,
			"stopEvent": false
	    })
	</script>            <script type="text/javascript" src="./Linearregression_files/tiara.min.js"></script>
            <script type="text/javascript">window.tiara = {"svcDomain":"user.tistory.com","section":"\uae00\ubdf0","trackPage":"\uae00\ubdf0_\ubcf4\uae30","page":"\uae00\ubdf0","key":"3539841-15","customProps":{"userId":0,"blogId":"3539841","role":"guest","filterTarget":false,"trackPage":"\uae00\ubdf0_\ubcf4\uae30","entryId":"15"},"entry":{"entryId":"15","categoryName":"\uac1c\ubc1c\ud658\uacbd\uc124\uc815","categoryId":"1202962","author":"4146351","authorId":"4146351","image":"4146351","plink":"\/15","tags":[],"key":"3539841-15"},"sentryDsn":"https:\/\/a53520229cd744e798d42900d76b0e2a@aem-ingest.onkakao.net\/713","kakaoAppKey":"b8aef3eeb03fa312b81795386484f051","appUserId":null};</script>
            <script type="text/javascript" src="./Linearregression_files/tiara.min(1).js" defer=""></script>
                        <script type="text/javascript">
                window.roosevelt_params_queue = window.roosevelt_params_queue || [{channel_id: 'dk', channel_label: 'tistory'}];
            </script>
            <script type="text/javascript" src="./Linearregression_files/roosevelt_dk_bt.js" async=""></script><script type="text/javascript">if(window.console!=undefined){setTimeout(console.log.bind(console,"%cTISTORY","font:8em Arial;color:#EC6521;font-weight:bold"),0);setTimeout(console.log.bind(console,"%c  나를 표현하는 블로그","font:2em sans-serif;color:#333;"),0);}</script><iframe style="position:absolute;width:1px;height:1px;left:-100px;top:-100px" src="./Linearregression_files/api.html" id="editEntry"></iframe><div id="tistoryEtcLayer" class="layer_post"></div><div id="tistorySnsLayer" class="layer_post"><div class="bundle_post"><a href="https://captainteemo.tistory.com/15#none" class="btn_mark" data-service="facebook"><span class="ico_sns ico_fb"></span>페이스북으로 공유</a><a href="https://captainteemo.tistory.com/15#none" class="btn_mark" data-service="kakaotalk"><span class="ico_sns ico_kt"></span>카카오톡으로 공유</a><a href="https://captainteemo.tistory.com/15#none" class="btn_mark" data-service="kakaostory"><span class="ico_sns ico_ks"></span>카카오스토리로 공유</a><a href="https://captainteemo.tistory.com/15#none" class="btn_mark" data-service="twitter"><span class="ico_sns ico_tw"></span>트위터로 공유</a><a href="https://captainteemo.tistory.com/15#none" class="btn_mark" data-service="url"><span class="ico_sns ico_url"></span>URL 복사</a><span class="ico_postbtn ico_arrbt"></span></div></div>
<script>
  $('.article_view').find('table').each(function (idx, el) {
    $(el).wrap('<div class="table-overflow">')
  })
</script>


<div id="lightboxOverlay" class="lightboxOverlay" style="display: none;"></div><div id="goog-gt-tt" class="skiptranslate" dir="ltr"><div style="padding: 8px;"><div><div class="logo"><img src="./Linearregression_files/translate_24dp.png" width="20" height="20" alt="Google 번역"></div></div></div><div class="top" style="padding: 8px; float: left; width: 100%;"><h1 class="title gray">원본 텍스트</h1></div><div class="middle" style="padding: 8px;"><div class="original-text"></div></div><div class="bottom" style="padding: 8px;"><div class="activity-links"><span class="activity-link">번역 제안하기</span><span class="activity-link"></span></div><div class="started-activity-container"><hr style="color: #CCC; background-color: #CCC; height: 1px; border: none;"><div class="activity-root"></div></div></div><div class="status-message" style="display: none;"></div></div><div id="lightbox" class="lightbox" style="display: none;"><div class="lb-outerContainer"><div class="lb-container"><img class="lb-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="><div class="lb-nav"><a class="lb-prev" href="https://captainteemo.tistory.com/15"></a><a class="lb-next" href="https://captainteemo.tistory.com/15"></a></div><div class="lb-loader"><a class="lb-cancel"></a></div></div></div><div class="lb-dataContainer"><div class="lb-data"><div class="lb-details"><span class="lb-caption"></span><span class="lb-number"></span></div><div class="lb-closeContainer"><a class="lb-close"></a></div></div></div></div><div class="goog-te-spinner-pos"><div class="goog-te-spinner-animation"><svg xmlns="http://www.w3.org/2000/svg" class="goog-te-spinner" width="96px" height="96px" viewBox="0 0 66 66"><circle class="goog-te-spinner-path" fill="none" stroke-width="6" stroke-linecap="round" cx="33" cy="33" r="30"></circle></svg></div></div></body></html>